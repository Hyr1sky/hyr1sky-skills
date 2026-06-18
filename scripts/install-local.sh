#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src_dir="$repo_root/skills"
dest_dir="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$dest_dir"

for skill_dir in "$src_dir"/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  rm -rf "$dest_dir/$skill_name"
  cp -a "$skill_dir" "$dest_dir/$skill_name"
  echo "Installed $skill_name -> $dest_dir/$skill_name"
done
