---
name: research-codebase-to-wiki
description: Convert an unfamiliar codebase, paper implementation, or research repo into a sourced explanatory wiki with Task/Method/Dataset/Metric/Result, diagrams, core code or pseudocode, artifact profiling, and related-work comparison. Use when the user asks to understand a project, create an explanatory wiki/HTML overview, analyze a CS paper repo, compare with related papers/repos, or investigate issues/forum feedback around a method.
---

# Research Codebase To Wiki

Use this skill to turn a repo into a clear technical explainer. Treat the repo as the source of truth first, then optionally enrich with external sources.

## Workflow

1. **Scope the artifact**
   - Identify repo type: paper implementation, product codebase, dataset pipeline, experiment repo, or mixed.
   - Read README, docs, config files, entry scripts, notebooks, and dependency manifests.
   - For cross-file behavior, use codegraph first when available; otherwise use `rg`, `rg --files`, and focused file reads.

2. **Map the local system**
   - Find execution paths: data ingestion, preprocessing, training/indexing, inference/evaluation, visualization/output.
   - Record concrete files and symbols for every major claim.
   - Identify generated artifacts and data files. Run `scripts/profile_artifacts.py` when useful.

3. **Extract paper-style sections**
   - Task: what problem is solved, for whom, with what inputs/outputs.
   - Method: algorithms, models, retrieval/indexing, training/inference, prompts, graph schemas, control flow.
   - Dataset: raw inputs, intermediate datasets, final indexes/models, scale, splits if present.
   - Metric: evaluation scripts, reported metrics, logs, result tables, or absence of formal evaluation.
   - Result: generated outputs, checkpoints, reports, visualizations, observed behavior.

4. **Explain the method with implementation anchors**
   - Include short core code excerpts only when they clarify the method. Keep snippets small and cite file paths.
   - Prefer pseudocode for longer flows or when exact code is noisy.
   - Show input/output tables for key pipeline stages.
   - Make uncertainty explicit: distinguish implemented behavior from intended/commented/planned behavior.

5. **External research pass, if relevant or requested**
   - Search for related papers, official repos, benchmark pages, library docs, issues/discussions, and forum feedback.
   - Use primary sources first. Treat forums/issues as anecdotal evidence and label them as such.
   - Compare: what this repo borrows, changes, omits, or innovates relative to related work.
   - Cite links in the final wiki.

6. **Generate the wiki**
   - Default to Markdown unless the user asks for HTML or visual presentation.
   - Use `references/wiki-template.md` for structure.
   - Use `references/external-research-guide.md` for web-search rules.
   - Use `assets/overview-template.html` as a starting point for static HTML deliverables.

## Output Requirements

- Lead with the repo's actual goal and main pipeline.
- Include a workflow diagram for non-trivial systems.
- Include a Task/Method/Dataset/Metric/Result table.
- Include data scale and artifact scale when discoverable.
- Include at least one small pseudocode block or core-code block for CS/research methods when it improves understanding.
- Cite local files with paths and line numbers when possible.
- Cite external web sources with links when web research is used.
- Add a "Gaps / Risks / Open Questions" section for missing metrics, dead code, hardcoded paths, commented features, or unverified claims.

## Useful Commands

```bash
python3 /path/to/skill/scripts/profile_artifacts.py .
rg --files
rg -n "train|eval|infer|retriev|search|dataset|metric|result|embedding|graph|index|rerank|loss|accuracy|f1|auc|bleu|rouge|pass@"
```

## Guardrails

- Do not infer results from paper claims unless the repo contains those outputs or an external cited source confirms them.
- Do not let related papers override local code facts.
- Do not paste large copyrighted passages from papers, docs, issues, or forums.
- Do not present issue/forum comments as consensus; summarize patterns and link sources.
