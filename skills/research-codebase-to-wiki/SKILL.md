---
name: research-codebase-to-wiki
description: Generate an evidence-backed, offline browsable wiki for an existing codebase. Use when the requested deliverable is a durable repository explainer, whether the repo is a product system or a research implementation. Do not use when the goal is interactive system mastery, architecture conformance auditing, or ordinary code review.
---

# Research Codebase To Wiki

Turn a repository snapshot into a sourced, offline wiki. The wiki is the deliverable: it explains what exists, anchors important claims in evidence, and preserves uncertainty.

## Choose one profile

- **Product Architecture** — a product, runtime, platform, application, or multi-interface system. Read [references/product-architecture-profile.md](references/product-architecture-profile.md).
- **Research Implementation** — a paper implementation, algorithm repo, benchmark, dataset pipeline, or experiment repository. Read [references/research-implementation-profile.md](references/research-implementation-profile.md).

If the repository mixes both, choose the profile that matches the user's question and add only the few sections needed from the other profile. Do not produce two complete wikis.

Use `software-system-mastery` instead when success means the user can reason about and safely change the system. Use `architecture-drift-audit` when the task is to compare accepted intent with the implementation. A wiki may later become evidence for either workflow, but this skill does not perform their completion checks.

## Workflow

1. **Freeze the source snapshot**
   - Identify the repository root, current commit, dirty state, intended audience, profile, and output directory.
   - Read repository instructions and authority documents before broad exploration.
   - Do not silently mix facts from different commits or local worktrees.

2. **Build an evidence ledger**
   - Prefer executable code, tests, schemas, configuration, runtime artifacts, and accepted decisions over summaries.
   - Mark consequential claims as `implemented`, `partial`, `planned`, `declared`, `inferred`, `unknown`, or `superseded` using [references/evidence-discipline.md](references/evidence-discipline.md).
   - Use codegraph first for cross-file behavior when available; otherwise use `rg`, `rg --files`, Git history, and focused reads.

3. **Trace the smallest useful system model**
   - Follow at least one critical scenario end to end.
   - Identify inputs, transformations, state owners, side effects, failure paths, and externally visible results.
   - Record concrete file or symbol anchors for every load-bearing claim.

4. **Compose for navigation, not file enumeration**
   - Lead with purpose and a one-picture system map.
   - Organize around domain concepts, decisions, flows, and evidence. Use folders only to explain dependency direction or ownership.
   - Include short code excerpts or pseudocode only when they clarify responsibility or control flow.

5. **Render an offline wiki**
   - Follow [references/output-contract.md](references/output-contract.md).
   - Start from `assets/wiki-shell/` via `scripts/scaffold_wiki.py`; adapt the visual language to the repository without removing offline, accessibility, or provenance constraints.
   - External sources may be cited as links, but the wiki must not load remote scripts, fonts, styles, images, or other active resources.

6. **Validate before delivery**
   - Run `scripts/validate_wiki.py <wiki-dir> --source-root <repo-root>`.
   - Open the final wiki locally and inspect desktop and narrow layouts, search, navigation, theme, code copy, and any tabs or filters actually included.
   - Report the source commit, profile, output path, validation result, and unresolved claims.

## Output rules

- Generate `README.md`, `index.html`, `wiki.css`, `wiki.js`, and `wiki-manifest.json` in one directory.
- Keep generated output outside the source repository unless the user explicitly requests it be tracked.
- The manifest records the generating skill, profile, source snapshot, authority files, evidence counts, unresolved claims, and output hashes.
- Distinguish current implementation from intention and roadmap. Do not turn `planned` into `implemented` for narrative completeness.
- Never expose secrets, credentials, private runtime payloads, or large copyrighted passages.
- Preserve repo-specific vocabulary. Do not force research terminology onto a product system or product terminology onto a research implementation.

## Supporting tools

```bash
# Optional: profile research/data artifacts.
python3 scripts/profile_artifacts.py /path/to/repo

# Render the standard offline shell around completed HTML sections.
python3 scripts/scaffold_wiki.py OUTPUT_DIR \
  --title "Project Wiki" \
  --profile product-architecture \
  --source-root /path/to/repo \
  --content-file /path/to/sections.html \
  --authority-file CONTEXT.md \
  --evidence-count implemented=24 \
  --unverified-claim "Deployment topology was not exercised locally"

# Validate provenance, offline safety, anchors, files, and hashes.
python3 scripts/validate_wiki.py OUTPUT_DIR --source-root /path/to/repo
```

For external research rules, read [references/external-research-guide.md](references/external-research-guide.md) only when external context materially improves the requested wiki.
