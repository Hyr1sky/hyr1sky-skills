#!/usr/bin/env python3
"""Validate an offline codebase wiki and its provenance manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_FILES = {"README.md", "index.html", "wiki.css", "wiki.js", "wiki-manifest.json"}
REQUIRED_HASHED_FILES = {"README.md", "index.html", "wiki.css", "wiki.js"}
REQUIRED_MANIFEST_KEYS = {
    "schema_version",
    "generated_by",
    "skill_revision",
    "profile",
    "source_root_name",
    "source_commit",
    "source_dirty",
    "generated_at",
    "authority_files",
    "evidence_status",
    "unverified_claims",
    "output_files",
}
EVIDENCE_STATUSES = {
    "implemented",
    "partial",
    "planned",
    "declared",
    "inferred",
    "unknown",
    "superseded",
}
ACTIVE_RESOURCE_ATTRS = {
    "script": "src",
    "link": "href",
    "img": "src",
    "iframe": "src",
    "audio": "src",
    "video": "src",
    "source": "src",
    "object": "data",
}


class WikiParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.anchor_hrefs: list[str] = []
        self.active_resources: list[tuple[str, str]] = []
        self.source_paths: list[str] = []
        self.inline_scripts = 0
        self.event_handlers: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "script" and not values.get("src"):
            self.inline_scripts += 1
        for name, _value in attrs:
            if name.lower().startswith("on"):
                self.event_handlers.append((tag, name))
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        href = values.get("href")
        if tag == "a" and href:
            self.anchor_hrefs.append(href)
        resource_attr = ACTIVE_RESOURCE_ATTRS.get(tag)
        if resource_attr and values.get(resource_attr):
            self.active_resources.append((tag, values[resource_attr] or ""))
        source_path = values.get("data-source-path")
        if source_path:
            self.source_paths.append(source_path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def is_remote(value: str) -> bool:
    parsed = urlparse(value)
    return value.startswith("//") or parsed.scheme in {"http", "https", "data"}


def local_target(base: Path, value: str) -> Path | None:
    parsed = urlparse(value)
    if parsed.scheme or value.startswith("#"):
        return None
    return (base / parsed.path).resolve()


def within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wiki_dir", type=Path)
    parser.add_argument("--source-root", type=Path)
    args = parser.parse_args()

    wiki_dir = args.wiki_dir.resolve()
    source_root = args.source_root.resolve() if args.source_root else None
    errors: list[str] = []
    if not wiki_dir.is_dir():
        parser.error(f"wiki directory does not exist: {wiki_dir}")
    missing = sorted(name for name in REQUIRED_FILES if not (wiki_dir / name).is_file())
    if missing:
        errors.append(f"missing required files: {', '.join(missing)}")

    text_files = [
        path
        for path in wiki_dir.rglob("*")
        if path.is_file() and path.suffix in {".html", ".css", ".js", ".md", ".json"}
    ]
    placeholder_pattern = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        matches = sorted(set(placeholder_pattern.findall(text)))
        if matches:
            errors.append(f"unresolved template markers in {path.name}: {', '.join(matches)}")
        if path.suffix == ".css" and re.search(
            r"(?:@import\s+|url\(\s*['\"]?)(?:https?:)?//", text, re.IGNORECASE
        ):
            errors.append(f"remote CSS resource is forbidden: {path.name}")
        if path.suffix == ".js" and re.search(
            r"\b(?:fetch|XMLHttpRequest|WebSocket|EventSource)\s*\(", text
        ):
            errors.append(f"active JavaScript networking is forbidden: {path.name}")

    index_path = wiki_dir / "index.html"
    if index_path.is_file():
        document = index_path.read_text(encoding="utf-8")
        html_parser = WikiParser()
        html_parser.feed(document)
        if html_parser.inline_scripts:
            errors.append("inline scripts are forbidden; use the local wiki.js asset")
        for tag, name in html_parser.event_handlers:
            errors.append(f"inline event handler is forbidden: <{tag}> {name}")
        for href in html_parser.anchor_hrefs:
            if href.startswith("#") and href[1:] not in html_parser.ids:
                errors.append(f"broken internal anchor: {href}")
            target = local_target(wiki_dir, href)
            if target is not None and (not within(target, wiki_dir) or not target.exists()):
                errors.append(f"missing or escaping local link: {href}")
        for tag, value in html_parser.active_resources:
            if is_remote(value):
                errors.append(f"remote active resource is forbidden: <{tag}> {value}")
                continue
            target = local_target(wiki_dir, value)
            if target is not None and (not within(target, wiki_dir) or not target.is_file()):
                errors.append(f"missing or escaping active resource: <{tag}> {value}")
        if source_root is not None:
            if not html_parser.source_paths:
                errors.append("index.html must declare at least one data-source-path")
            for value in html_parser.source_paths:
                target = (source_root / value).resolve()
                if not within(target, source_root) or not target.is_file():
                    errors.append(f"missing or escaping data-source-path: {value}")

    manifest_path = wiki_dir / "wiki-manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"invalid wiki-manifest.json: {exc}")
            manifest = None
        if isinstance(manifest, dict):
            absent = sorted(REQUIRED_MANIFEST_KEYS - manifest.keys())
            if absent:
                errors.append(f"manifest missing keys: {', '.join(absent)}")
            if manifest.get("generated_by") != "research-codebase-to-wiki":
                errors.append("manifest generated_by is not research-codebase-to-wiki")
            if manifest.get("profile") not in {"product-architecture", "research-implementation"}:
                errors.append("manifest profile is invalid")
            statuses = manifest.get("evidence_status")
            if not isinstance(statuses, dict) or set(statuses) != EVIDENCE_STATUSES:
                errors.append("manifest evidence_status must contain the seven supported statuses")
            elif any(not isinstance(value, int) or value < 0 for value in statuses.values()):
                errors.append("manifest evidence_status values must be non-negative integers")
            if source_root is not None:
                authority_files = manifest.get("authority_files")
                if not isinstance(authority_files, list):
                    errors.append("manifest authority_files must be a list")
                else:
                    for value in authority_files:
                        if not isinstance(value, str):
                            errors.append("manifest authority file names must be strings")
                            continue
                        target = (source_root / value).resolve()
                        if not within(target, source_root) or not target.is_file():
                            errors.append(f"manifest authority file does not exist: {value}")
            hashes = manifest.get("output_files")
            if not isinstance(hashes, dict):
                errors.append("manifest output_files must be an object")
            else:
                missing_hashes = sorted(REQUIRED_HASHED_FILES - hashes.keys())
                if missing_hashes:
                    errors.append(
                        "manifest output_files missing required hashes: "
                        + ", ".join(missing_hashes)
                    )
                for name, expected in hashes.items():
                    if not isinstance(name, str) or not isinstance(expected, str):
                        errors.append("manifest output file hashes must be string pairs")
                        continue
                    target = (wiki_dir / name).resolve()
                    if not within(target, wiki_dir) or not target.is_file():
                        errors.append(f"manifest output file does not exist: {name}")
                    elif sha256(target) != expected:
                        errors.append(f"manifest hash mismatch: {name}")

    if errors:
        print("Wiki validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Wiki validation passed: {wiki_dir}")


if __name__ == "__main__":
    main()
