# External Research Guide

Use this guide when the user asks for related work, papers, repos, issues, forums, or when external context would materially improve the wiki.

## Search Strategy

1. Derive search terms from local code facts:
   - method names,
   - model names,
   - dataset names,
   - domain terms,
   - paper-style phrases in prompts or comments,
   - library names.

2. Search in this order:
   - Papers: arXiv, ACL Anthology, OpenReview, IEEE/ACM pages, project pages.
   - Official repos: GitHub organization or paper-linked repository.
   - Official docs: library/framework/model documentation.
   - Issues/discussions: GitHub issues, discussions, release notes.
   - Forums/blogs: Reddit, StackOverflow, Hugging Face discussions, project forums.

3. Prefer primary sources:
   - paper PDF or abstract page,
   - official implementation,
   - official docs,
   - benchmark leaderboard,
   - maintainers' comments.

## What To Extract

For papers:

- Task and dataset.
- Method summary.
- Metric and reported results.
- Claimed contribution.
- Relationship to this repo.

For repos:

- Implementation overlap.
- Differences in architecture, data handling, evaluation, or scale.
- Reproducibility signals: install docs, checkpoints, tests, issues.

For issues/forums:

- Recurring failure modes.
- Installation pain.
- Model/data compatibility issues.
- Performance or scalability complaints.
- User-requested features.

## Reporting Rules

- Clearly mark issue/forum evidence as "community feedback" or "anecdotal".
- Do not overgeneralize from a single issue.
- Cite every external source used.
- If sources conflict, describe the conflict and favor primary sources.
- Keep quotes short; paraphrase instead of copying long passages.

## Comparison Table

| Source | Type | Core Idea | Evidence | Relation To Local Repo |
|---|---|---|---|---|

## Suggested Search Queries

Use combinations like:

```text
"<method term>" GitHub
"<method term>" arXiv
"<dataset name>" benchmark
"<model name>" issue
"<library>" "<error or feature>"
"chain of thought" "retrieval augmented generation"
"knowledge graph" "RAG" "<domain>"
```
