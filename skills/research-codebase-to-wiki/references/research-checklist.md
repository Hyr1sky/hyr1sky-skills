# Research Checklist

Use this checklist while investigating a repo.

## Local Discovery

- [ ] README and docs identify project purpose.
- [ ] Dependency manifests identify framework and model stack.
- [ ] Entry points found: CLI, main scripts, notebooks, service routes, tests.
- [ ] Data flow found from raw input to final output.
- [ ] Generated artifacts identified.
- [ ] Evaluation or result files identified.
- [ ] Hardcoded paths, credentials, or environment assumptions noted.
- [ ] Commented/dead/planned code separated from active implementation.

## Task

- [ ] Input modality and output label/structure.
- [ ] User or research problem.
- [ ] Baseline implied or explicit.
- [ ] Scope limits.

## Method

- [ ] Main algorithms and models.
- [ ] Training/indexing/inference split.
- [ ] Retrieval/indexing details if present.
- [ ] Prompting or rule logic if present.
- [ ] Core code or pseudocode extracted.
- [ ] Complexity/scaling bottlenecks noted when obvious.

## Dataset

- [ ] Raw data count and size.
- [ ] Intermediate artifact count and size.
- [ ] Final artifact count and size.
- [ ] Schema samples for key artifacts.
- [ ] Splits and labels if present.

## Metric And Result

- [ ] Metric scripts or result files located.
- [ ] Reported metrics copied with source.
- [ ] If no metrics exist, state that clearly.
- [ ] Visualizations/checkpoints/output examples summarized.

## Final Wiki Quality

- [ ] Claims are backed by local file refs or external citations.
- [ ] Pipeline diagram included.
- [ ] Task/Method/Dataset/Metric/Result table included.
- [ ] Code/pseudocode included for CS methods.
- [ ] External related work separated from local facts.
- [ ] Gaps/risks/open questions included.
