# Evidence Discipline

Use a small evidence ledger while researching. It can remain an internal working artifact, but consequential uncertainty must survive into the final wiki and manifest.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| `implemented` | Verifiable in executable code, schema, configuration, tests, or runtime evidence. |
| `partial` | Only part of the claimed behavior exists, or it works only on a subset of paths/environments. |
| `planned` | A current plan or proposed decision exists without implementation evidence. |
| `declared` | A document or comment states the claim, but authority or implementation is unverified. |
| `inferred` | A reasoned conclusion from evidence; record the reasoning and confidence. |
| `unknown` | Available evidence cannot support a safe conclusion. |
| `superseded` | Previously true intent or behavior replaced by a later decision or implementation. |

## Evidence priority

Use the source appropriate to the claim:

- current behavior: executable code, tests, schemas, configuration, runtime evidence;
- intended behavior: accepted decisions, domain vocabulary, architecture documents;
- current commitment: current plan or issue tracker selected by the repository;
- historical rationale: Git history, archived plans, superseded decisions;
- external comparison: primary papers, official repos, and official documentation.

No source category automatically overrides another category because they answer different questions.

## Ledger shape

| Claim | Status | Evidence | Snapshot | Confidence | Notes |
| --- | --- | --- | --- | --- | --- |

Record file and symbol anchors rather than only filenames. For generated artifacts or runtime reports, record the producing command and content hash when practical.

## Claims that require explicit uncertainty

- performance or scale without a benchmark;
- reliability without failure-path evidence;
- a feature described only in roadmap or comments;
- external integration not exercised in the observed environment;
- security or privacy claims based only on absence of obvious defects;
- inferred ownership where several modules can mutate the same state.

## Snippet discipline

- Use the smallest excerpt that proves the explanation.
- Preserve enough surrounding context to avoid reversing its meaning.
- Prefer pseudocode when exact code is long or incidental.
- Do not copy secrets, private payloads, large data samples, or copyrighted text.
- Record the source commit so line drift does not silently invalidate the explanation.
