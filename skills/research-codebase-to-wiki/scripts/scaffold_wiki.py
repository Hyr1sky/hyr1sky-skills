#!/usr/bin/env python3
"""Render the reusable offline wiki shell around completed HTML sections."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import shutil
import subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

PROFILES = {"product-architecture", "research-implementation"}
EVIDENCE_STATUSES = (
    "implemented",
    "partial",
    "planned",
    "declared",
    "inferred",
    "unknown",
    "superseded",
)


class SectionCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sections: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "section":
            return
        values = dict(attrs)
        section_id = values.get("id")
        title = values.get("data-title")
        if section_id and title:
            self.sections.append((section_id, title))


def run_git(root: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def git_snapshot(root: Path) -> tuple[str, bool]:
    commit = run_git(root, "rev-parse", "HEAD") or "unversioned"
    dirty = bool(run_git(root, "status", "--porcelain") or "")
    return commit, dirty


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def replace(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def evidence_count(value: str) -> tuple[str, int]:
    status, separator, raw_count = value.partition("=")
    if not separator or status not in EVIDENCE_STATUSES:
        supported = ", ".join(sorted(EVIDENCE_STATUSES))
        raise argparse.ArgumentTypeError(
            f"expected STATUS=COUNT where STATUS is one of: {supported}"
        )
    try:
        count = int(raw_count)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("evidence COUNT must be an integer") from exc
    if count < 0:
        raise argparse.ArgumentTypeError("evidence COUNT must be non-negative")
    return status, count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--summary",
        default="An evidence-backed guide to the current repository snapshot.",
    )
    parser.add_argument("--profile", required=True, choices=sorted(PROFILES))
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--content-file", required=True, type=Path)
    parser.add_argument("--authority-file", action="append", default=[])
    parser.add_argument(
        "--evidence-count",
        action="append",
        default=[],
        type=evidence_count,
        metavar="STATUS=COUNT",
    )
    parser.add_argument("--unverified-claim", action="append", default=[])
    parser.add_argument("--skill-revision", default="working-tree")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    content_file = args.content_file.resolve()
    output_dir = args.output_dir.resolve()
    if not source_root.is_dir():
        parser.error(f"source root is not a directory: {source_root}")
    if not content_file.is_file():
        parser.error(f"content file does not exist: {content_file}")
    missing_authority = [name for name in args.authority_file if not (source_root / name).is_file()]
    if missing_authority:
        parser.error(f"authority files do not exist: {', '.join(missing_authority)}")
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        parser.error(
            f"output directory is not empty: {output_dir}; pass --force to replace generated files"
        )
    output_dir.mkdir(parents=True, exist_ok=True)

    shell_dir = Path(__file__).resolve().parents[1] / "assets" / "wiki-shell"
    template = (shell_dir / "index.html").read_text(encoding="utf-8")
    content = content_file.read_text(encoding="utf-8").strip()
    collector = SectionCollector()
    collector.feed(content)
    if not collector.sections:
        parser.error("content must include at least one <section id=... data-title=...>")
    ids = [section_id for section_id, _ in collector.sections]
    if len(ids) != len(set(ids)):
        parser.error("section ids must be unique")
    evidence_status = dict.fromkeys(EVIDENCE_STATUSES, 0)
    for status, count in args.evidence_count:
        evidence_status[status] = count

    source_commit, source_dirty = git_snapshot(source_root)
    nav = "\n".join(
        f'<a href="#{html.escape(section_id, quote=True)}">{html.escape(title)}</a>'
        for section_id, title in collector.sections
    )
    index = replace(
        template,
        {
            "TITLE": html.escape(args.title, quote=True),
            "SUMMARY": html.escape(args.summary, quote=True),
            "PROFILE": html.escape(args.profile, quote=True),
            "SOURCE_COMMIT": html.escape(source_commit, quote=True),
            "NAV": nav,
            "CONTENT": content,
        },
    )
    (output_dir / "index.html").write_text(index, encoding="utf-8")
    shutil.copyfile(shell_dir / "wiki.css", output_dir / "wiki.css")
    shutil.copyfile(shell_dir / "wiki.js", output_dir / "wiki.js")

    reading_route = "\n".join(
        f"{index}. {title}" for index, (_section_id, title) in enumerate(collector.sections, 1)
    )
    evidence_limits = (
        "\n".join(f"- {claim}" for claim in args.unverified_claim)
        if args.unverified_claim
        else "- No unresolved claims were declared at scaffold time."
    )

    readme = f"""# {args.title}

Offline `{args.profile}` wiki for `{source_root.name}` at `{source_commit}`.

## Open

Open `index.html` directly, or run:

```bash
python3 -m http.server 8765 --directory {output_dir}
```

Then visit `http://127.0.0.1:8765/`.

## Recommended reading route

{reading_route}

## Evidence limits

{evidence_limits}

The wiki does not load remote active resources. Theme and reading progress remain in
browser localStorage. See `wiki-manifest.json` for provenance and unresolved claims.
"""
    (output_dir / "README.md").write_text(readme, encoding="utf-8")

    output_files = {
        name: sha256(output_dir / name)
        for name in ("README.md", "index.html", "wiki.css", "wiki.js")
    }
    manifest = {
        "schema_version": 1,
        "generated_by": "research-codebase-to-wiki",
        "skill_revision": args.skill_revision,
        "profile": args.profile,
        "source_root_name": source_root.name,
        "source_commit": source_commit,
        "source_dirty": source_dirty,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "authority_files": args.authority_file,
        "evidence_status": evidence_status,
        "unverified_claims": args.unverified_claim,
        "output_files": output_files,
    }
    (output_dir / "wiki-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Rendered {len(collector.sections)} sections to {output_dir}")


if __name__ == "__main__":
    main()
