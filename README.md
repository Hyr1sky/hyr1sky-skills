# hyr1sky-skills

Personal Codex skills repository.

## Structure

```text
skills/
  deep-reading-tutor/
    SKILL.md
    agents/
      openai.yaml
```

Each folder under `skills/` is a standalone Codex skill. Keep individual skill folders minimal: `SKILL.md` is required, `agents/openai.yaml` is recommended, and `references/`, `scripts/`, or `assets/` should be added only when the skill needs them.

## Local Install

Install or update all skills into `~/.codex/skills`:

```bash
./scripts/install-local.sh
```

This copies each folder under `skills/` into `~/.codex/skills/`.

## Validate

Validate a skill with Codex's skill creator validator:

```bash
python3 /Users/hyriskyhe/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/deep-reading-tutor
```

## GitHub

```bash
git init
git add .
git commit -m "Initial skills repo"
git remote add origin git@github.com:<you>/hyr1sky-skills.git
git push -u origin main
```
