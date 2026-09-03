# Research Implementation Profile

Use this profile for a paper implementation, algorithm repository, benchmark, model experiment, dataset pipeline, or mixed research artifact.

## Evidence order

Read the README and paper claims, then verify them against dependency manifests, entry scripts, notebooks, configuration, dataset code, evaluation scripts, checkpoints, logs, and result artifacts. Do not infer a reproduced result merely because a paper reports it.

Run `scripts/profile_artifacts.py` when the repository contains substantial datasets, checkpoints, indexes, graphs, or result files.

## Recommended information architecture

1. **Executive summary** — problem, core method, and what is actually implemented.
2. **System/pipeline map** — raw input through preprocessing, training/indexing, inference, evaluation, and outputs.
3. **Task / Method / Dataset / Metric / Result** — use the evidence table below.
4. **Data and artifact scale** — count, size, split, schema, and whether numbers are exact or sampled.
5. **Method walkthrough** — stages with input, process, output, and source anchors.
6. **Core algorithm** — concise pseudocode mapped back to implementation.
7. **Evaluation and reproducibility** — commands, seeds, environment, baselines, metrics, and missing evidence.
8. **External context** — only when requested or materially useful; separate papers, official repos, docs, and anecdotal community evidence.
9. **Innovations and differences** — local evidence first; do not repeat paper marketing.
10. **Limitations, risks, and open questions**.
11. **How to reproduce or extend** — only verified commands or clearly marked inferences.

## Evidence table

| Section | Required finding | Evidence examples |
| --- | --- | --- |
| Task | Inputs, outputs, user/research problem, baseline, scope | README plus entrypoint or tests |
| Method | Algorithm, models, retrieval/indexing, prompts, control flow | implementation and config |
| Dataset | raw/intermediate/final artifacts, schema, scale, splits | loaders, manifests, local artifacts |
| Metric | computation, aggregation, thresholds, missing metrics | evaluation scripts and reports |
| Result | reproduced outputs versus externally reported claims | logs, tables, checkpoints, cited paper |

## Method stage template

For each stage record:

- purpose;
- input and trust assumptions;
- transformation or algorithm;
- output and persisted artifacts;
- configuration/model identity;
- key files and symbols;
- known scaling or reproducibility constraints.

## External research

Read [external-research-guide.md](external-research-guide.md) when external comparison is in scope. Prefer primary sources. Label issue, discussion, and forum findings as anecdotal; never use them to overwrite local implementation facts.

## Completion check

The wiki is ready when it distinguishes reported from reproduced results, maps the method to executable source, accounts for important artifacts and scales, explains evaluation provenance, and makes absent evidence explicit.
