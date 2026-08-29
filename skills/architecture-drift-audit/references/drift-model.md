# Architecture Drift Model

Use this reference to compare architectural intent with implementation without assuming that either side is automatically correct.

## Comparison Unit

Express both intended and as-built elements with the same fields:

```text
Element or relationship:
Responsibility or rule:
Owned state:
Provided contract:
Required contract:
Allowed dependencies:
Relevant quality attribute or stakeholder concern:
Source and confidence:
```

Compare at the smallest architectural unit that can support a consequential claim. Avoid line-level findings unless they demonstrate a boundary violation.

## Classifications

| Classification | Meaning | Typical action |
| --- | --- | --- |
| Convergence | Implementation realizes the intended responsibility or relationship. | Preserve; consider an enforcement check if critical. |
| Divergence | Both sides exist, but implementation violates or materially changes the intended relationship. | Fix implementation or deliberately revise intent through a decision. |
| Absence | Intended element, contract, or rule has no implementation evidence. | Implement, descope explicitly, or mark as future intent. |
| Unplanned | Implementation contains an architectural element or relationship not represented in intent. | Model and decide whether to adopt, isolate, or remove it. |
| Unmapped | An implementation or intent element has not yet been reliably mapped at the chosen abstraction level. | Refine the mapping before making a conformance claim. |
| Stale intent | The documented intent no longer reflects an accepted and beneficial system evolution. | Supersede the old decision while preserving history. |
| Unresolved | Evidence is incomplete, contradictory, or at incompatible abstraction levels. | Gather the specific evidence needed before deciding. |

Drift is the set of consequential `divergence`, `absence`, and `unplanned` mappings that have not been deliberately accepted. `Unmapped` and `unresolved` are limits on the audit's knowledge, not drift findings. `Stale intent` is a documentation and governance problem, not automatically an implementation defect.

## Classification Priority

Choose one primary classification for each finding:

1. Use `Divergence` when an explicit intended responsibility, contract, or allowed relationship exists and the implementation contradicts it.
2. Use `Absence` when intent expects an element or relationship and there is sufficient coverage to say it is missing.
3. Use `Unplanned` only when an implemented architectural element or relationship has no counterpart or governing rule in the intent baseline. Do not use it as a second label for an explicit violation already classified as `Divergence`.
4. Use `Stale intent` only when there is evidence that the implementation change was deliberately accepted and the old baseline no longer expresses the desired architecture.
5. Use `Unmapped` or `Unresolved` when the audit cannot yet support one of the above claims.

Confidence, evidence gaps, and unresolved consequences are qualifiers, not extra primary classifications.

## Finding Shape

```text
Finding:
Classification:
Original intent and source:
As-built evidence:
Affected responsibility or contract:
Causal consequence:
Affected stakeholders / quality attributes:
Severity and confidence:
Recommended reconciliation:
Possible fitness function:
```

## Severity

Judge severity from consequence and reversibility:

- Critical: can violate safety, security, legal, data-integrity, or core availability expectations.
- High: breaks a major responsibility or contract and creates broad or costly blast radius.
- Medium: increases coupling, operational fragility, or change cost in a bounded area.
- Low: limited consequence, localized inconsistency, or primarily documentation debt.

Do not inflate severity solely because a named pattern or layer rule was violated.

## Fitness Functions

Recommend an automated or review-time constraint only when it protects a material architectural property. Examples include:

- forbidden dependency or import direction;
- API or event schema compatibility;
- data ownership and write-path restriction;
- latency, availability, or recovery objective;
- deployment isolation or network boundary;
- observability coverage for a critical scenario.

State the protected property, measurement, threshold, scope, and failure response. Avoid tests that merely freeze the current implementation shape.

Also state when the check runs, who owns the rule, and the likely false-positive or gaming risk. A fitness function should protect an accepted architectural property, not turn an analyst's preference into a gate.
