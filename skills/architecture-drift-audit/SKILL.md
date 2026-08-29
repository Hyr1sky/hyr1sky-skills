---
name: architecture-drift-audit
description: "Compare intended architecture with the as-built system, preserve original design intent, map module responsibilities and contracts, and classify consequential drift. Use for architecture conformance reviews, erosion audits, blueprint recovery, or checking whether implementation still matches decisions. Do not use for ordinary code review, bug diagnosis, or greenfield architecture design."
---

# Architecture Drift Audit

Make original architectural intent and the current system visible at the same time. Determine whether differences are harmful implementation drift, legitimate evolution, missing implementation, or stale intent.

## Boundary

- Use only when comparison between intended and as-built architecture is central.
- Do not substitute this for general code quality review, dependency cleanup, bug diagnosis, or greenfield design.
- If no intended architecture exists, recover a provisional blueprint from the strongest available evidence and label it as reconstructed; do not present it as original intent.
- Use `software-system-mastery` first when the system is not understood well enough to establish either side of the comparison.

## Workflow

1. **Set the audit question and scope**
   - Identify the decision, concern, quality attribute, or change that makes drift relevant.
   - Choose the architectural boundaries and time horizon. Avoid auditing the entire system when one relationship is consequential.

2. **Recover intended architecture**
   - Gather architecture descriptions, ADRs, requirements, diagrams, interface specifications, module documentation, ownership rules, and historically important decisions.
   - Record each source's status, authority, date, and scope. Keep `proposed`, `accepted`, `deprecated`, and `superseded` intent distinct.
   - Record the stakeholder concern, constraint, responsibility, contract, dependency rule, and quality attribute each source expresses.
   - Preserve conflicting or superseded intent instead of silently selecting a preferred version.

3. **Map the as-built system**
   - Inspect code dependencies, public interfaces, schemas, events, runtime flows, deployment topology, configuration, tests, and operational evidence.
   - Describe modules by responsibility, owned state, provided contract, required contract, and allowed dependencies.
   - Separate reachable behavior from dead, disabled, generated, experimental, or planned code.
   - Include runtime and quality evidence when structural conformance alone cannot show whether the original concern is still satisfied.

4. **Create an intent-to-implementation mapping**
   - Map each intended element and relationship to observed implementation evidence.
   - Give each finding one primary classification using [references/drift-model.md](references/drift-model.md). Record uncertainty, confidence, or secondary consequences separately instead of stacking competing classifications.
   - Report mapping coverage and unmapped elements; a visually plausible diagram is not evidence of full coverage.
   - Treat uncertainty as `unresolved`; do not force a conformance verdict without evidence.

5. **Assess consequence, not cosmetic difference**
   - Explain how each material difference affects stakeholder concerns and quality attributes such as modifiability, reliability, security, performance, consistency, operability, and team ownership.
   - Identify causal chains and blast radius. A dependency direction is important only because of what it permits, couples, or prevents.
   - Check whether interfaces leak implementation knowledge or turn local changes into cross-module coordination, even when named layers still appear intact.
   - Distinguish accepted architectural evolution from accidental erosion.

6. **Reconcile blueprint and system**
   - Recommend one action for each material finding: change implementation, update the blueprint, record an ADR, clarify a contract or owner, add an automated fitness function, accept time-bounded debt, or gather more evidence.
   - Never erase historical intent. When intent changes, preserve the old decision, reason, replacement, and effective scope.

## Deliverables

Provide the minimum useful set:

- intended blueprint with source and confidence;
- as-built responsibility and contract map;
- intent-to-implementation mapping;
- prioritized drift findings with evidence, consequence, and classification;
- reconciled target blueprint;
- decision and enforcement backlog.

Lead with the few differences that can alter system behavior or future change cost. Keep speculative improvements separate from proven drift.
