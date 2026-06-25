#!/usr/bin/env python3
"""Profile common research/codebase artifacts for wiki generation.

Usage:
  python3 profile_artifacts.py /path/to/repo

The script prints Markdown tables for file sizes, row/object counts, and
NetworkX GML graph type counts when networkx is installed.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from collections import Counter
from pathlib import Path
from typing import Any


SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
}

DEFAULT_EXTS = {
    ".json",
    ".jsonl",
    ".csv",
    ".tsv",
    ".gml",
    ".parquet",
    ".pkl",
    ".pickle",
    ".pt",
    ".pth",
    ".bin",
    ".safetensors",
    ".npy",
    ".npz",
}


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{size} B"


def iter_files(root: Path, exts: set[str]) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() in exts:
                files.append(p)
    return sorted(files)


def json_count(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8") as f:
            obj: Any = json.load(f)
        if isinstance(obj, list):
            return f"{len(obj)} list items"
        if isinstance(obj, dict):
            return f"{len(obj)} dict keys"
        return type(obj).__name__
    except Exception as exc:
        return f"unreadable JSON: {type(exc).__name__}"


def jsonl_count(path: Path) -> str:
    rows = 0
    valid = 0
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                rows += 1
                try:
                    json.loads(line)
                    valid += 1
                except Exception:
                    pass
        if valid == rows:
            return f"{rows} rows"
        return f"{rows} rows, {valid} valid JSON"
    except Exception as exc:
        return f"unreadable JSONL: {type(exc).__name__}"


def delimited_count(path: Path, delimiter: str) -> str:
    try:
        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter=delimiter)
            rows = sum(1 for _ in reader)
        return f"{max(rows - 1, 0)} data rows"
    except Exception as exc:
        return f"unreadable table: {type(exc).__name__}"


def gml_count(path: Path) -> tuple[str, str | None]:
    try:
        import networkx as nx  # type: ignore

        graph = nx.read_gml(path)
        node_types = Counter(attrs.get("type", "Unknown") for _, attrs in graph.nodes(data=True))
        edge_types = Counter(attrs.get("relation", "Unknown") for *_, attrs in graph.edges(data=True))
        summary = f"{graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges"
        detail = (
            f"Node types: {dict(node_types)}\n\n"
            f"Edge types: {dict(edge_types)}"
        )
        return summary, detail
    except Exception as exc:
        return f"unreadable GML: {type(exc).__name__}", None


def describe_file(path: Path, root: Path) -> tuple[str, str, str, str | None]:
    rel = str(path.relative_to(root))
    suffix = path.suffix.lower()
    size = human_size(path.stat().st_size)
    detail = None

    if suffix == ".json":
        count = json_count(path)
    elif suffix == ".jsonl":
        count = jsonl_count(path)
    elif suffix == ".csv":
        count = delimited_count(path, ",")
    elif suffix == ".tsv":
        count = delimited_count(path, "\t")
    elif suffix == ".gml":
        count, detail = gml_count(path)
    else:
        count = "binary or unprofiled"

    return rel, size, count, detail


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile common project artifacts.")
    parser.add_argument("root", nargs="?", default=".", help="Project root.")
    parser.add_argument(
        "--ext",
        action="append",
        default=[],
        help="Extra extension to include, e.g. --ext .txt",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    exts = set(DEFAULT_EXTS)
    for ext in args.ext:
        exts.add(ext if ext.startswith(".") else f".{ext}")

    files = iter_files(root, exts)
    print("| Artifact | Size | Count / Shape |")
    print("|---|---:|---|")
    details: list[tuple[str, str]] = []
    for path in files:
        rel, size, count, detail = describe_file(path, root)
        print(f"| `{rel}` | {size} | {count} |")
        if detail:
            details.append((rel, detail))

    if details:
        print("\n## Graph Details\n")
        for rel, detail in details:
            print(f"### `{rel}`\n")
            print("```text")
            print(detail)
            print("```\n")


if __name__ == "__main__":
    main()
