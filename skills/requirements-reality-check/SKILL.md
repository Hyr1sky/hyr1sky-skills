---
name: requirements-reality-check
description: "Stress-test a proposed requirement against the real business workflow, users, hardware, software, data, integrations, operations, ownership, and failure conditions before specification or implementation. Use for feasibility and reality checks, discovery, premortems, and uncovering assumptions. Do not use for already-settled implementation tasks or general architecture design."
---

# Requirements Reality Check

Determine whether a proposed requirement corresponds to a real need and can survive the environment in which it must operate. The goal is a decision-ready requirement, not a more polished version of an untested request.

## Boundary

- Use before commitment, specification, estimation, or implementation when the need, operating reality, feasibility, or ownership is uncertain.
- Do not activate merely because ordinary implementation has constraints. If the requirement and acceptance criteria are already settled, proceed with implementation.
- Do not design a complete architecture. Recommend targeted discovery, experiments, or requirement changes only as needed to resolve reality gaps.
- If the main question is whether an existing implementation still matches architectural intent, use `architecture-drift-audit`.

## Workflow

1. **Separate need from proposed solution**
   - Restate the desired outcome, affected actor, current pain, and consequence of doing nothing.
   - Describe current state, target state, and the evidenced gap between them.
   - Identify which statements are outcomes, solution choices, constraints, preferences, assumptions, and acceptance claims.
   - Preserve the user's words, but do not treat confident wording as evidence.

2. **Reconstruct the operating reality**
   - Examine the current business workflow, actors, incentives, handoffs, workarounds, volumes, timing, and exception handling.
   - Establish the actual baseline: hardware, software, networks, data, integrations, identity, environments, operational skills, budgets, governance, and ownership.
   - Identify upstream inputs, downstream consumers, external contracts, and who must change behavior.
   - For a broad or high-risk request, read [references/reality-check-lenses.md](references/reality-check-lenses.md).

3. **Exercise lifecycle scenarios**
   - Walk through normal, peak, degraded, recovery, and maintenance/change scenarios.
   - Trace inputs, decisions, state changes, side effects, user-visible outcomes, and accountable owners.
   - Include physical and organizational failure modes when software is not the whole system.

4. **Build the evidence and assumption ledger**
   - Label material claims as `fact`, `assumption`, `unknown`, or `conflict`.
   - For each uncertainty, record its impact and the cheapest reliable way to test it.
   - Distinguish missing information from an actual contradiction.

5. **Find forward risks**
   - Look for latent problems in value, adoption, workflow fit, data quality, capacity, compatibility, security, compliance, operability, support, recovery, ownership, and change management.
   - Use a premortem: assume the requirement shipped and failed; explain plausible causal chains from current conditions to failure.
   - Prioritize by decision impact and irreversibility, not by how many risks can be listed.

6. **Reframe and decide**
   - Rewrite the requirement around verified outcomes, explicit constraints, measurable acceptance conditions, and named unresolved assumptions.
   - Separate verification evidence (the solution meets the stated requirement) from validation evidence (the requirement and resulting solution meet the real intended use).
   - Give one readiness state: `ready to specify`, `conditionally ready`, `discovery required`, or `not justified`.
   - State what evidence would move the requirement to the next state, who needs to supply it, and what must not yet be promised.

## Output Contract

Produce a compact reality brief containing:

- real need and affected actors;
- current-state workflow and technical/environmental baseline;
- scenario findings;
- facts, assumptions, unknowns, and conflicts;
- highest-impact latent risks and causal chains;
- reframed requirement and acceptance conditions;
- readiness decision, required experiments, owners, and explicit non-commitments.

Do not hide uncertainty behind precise estimates. Do not turn every unknown into a blocking question; block only when the answer can materially reverse the decision.
