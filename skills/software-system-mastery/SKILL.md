---
name: software-system-mastery
description: "Build an evidence-backed mental model of an existing software system across domain, runtime, data, module, deployment, and quality-attribute views. Use when the user needs to understand, explain, onboard to, or reason safely about a system before changing it. Do not use when the main deliverable is a static codebase wiki or a quiz on one document."
---

# Software System Mastery

Help the user become able to reason about an existing software system, not merely receive a catalog of files. Organize investigation around the decision or task the understanding must support.

## Boundary

- Use this skill for system comprehension, onboarding, change preparation, technical handoff, and cross-layer reasoning.
- Use `research-codebase-to-wiki` instead when the requested product is a sourced, static repository wiki. That skill selects a Product Architecture or Research Implementation profile based on the codebase.
- Use `deep-reading-tutor` instead when the learning object is one paper or document and the user wants staged reading and grilling.
- Do not turn this into an architecture conformance audit unless the user asks to compare intended and implemented architecture; that belongs to `architecture-drift-audit`.

## Workflow

1. **Frame the mastery target**
   - Identify the system boundary and the decision the user needs to make: explain it, modify it, operate it, review it, debug it, or take ownership of it.
   - Ask only for missing context that would materially change the investigation. Otherwise state a provisional scope and proceed.
   - Define observable mastery criteria, such as being able to trace one critical scenario, explain state ownership, or predict the blast radius of a change.

2. **Build an evidence ledger**
   - Prefer executable code, tests, configuration, schemas, deployment files, and runtime evidence over prose that may be stale.
   - Record important claims as `observed`, `reported`, `inferred`, or `unknown`.
   - Keep intended, implemented, partially implemented, and merely planned behavior distinct.

3. **Construct the smallest useful system model**
   - Start with purpose, users, environment, external systems, and success conditions.
   - Identify core domain concepts and their bounded meanings before treating packages, services, or repositories as architectural boundaries. Allow the same term to mean different things in different contexts.
   - Select only the views needed for the mastery target: domain, context, runtime scenarios, data/state, modules and contracts, deployment/operations, and design decisions.
   - Select relevant quality attributes from the evidence instead of forcing a fixed checklist. Common examples are availability, performance, security, observability, recoverability, consistency, and evolvability.
   - For multi-layer or ambiguous systems, read [references/system-model-lenses.md](references/system-model-lenses.md).

4. **Trace critical scenarios end to end**
   - Choose at least one scenario whose success or failure matters to the user's goal.
   - Follow triggers, control flow, data transformations, state transitions, dependencies, failure handling, and externally visible outcomes.
   - Use concrete files, symbols, configuration keys, logs, or commands as anchors when available.

5. **Reconcile the views**
   - Check whether domain language, runtime behavior, data ownership, module responsibilities, and deployment topology tell a coherent story.
   - Surface hidden coupling, ambiguous ownership, leaky contracts, operational assumptions, and quality-attribute tradeoffs.
   - Test for change amplification, excessive cognitive load, and unknown unknowns. Identify which interfaces hide complexity well and which force callers to understand internal choices.
   - Treat contradictions as questions to resolve, not as facts to smooth over.

6. **Verify and deliver mastery**
   - Ask the user to explain, predict, or plan one task when interactive verification would help. Prefer a critical-scenario teach-back, impact prediction, or small practical investigation over a fixed quiz sequence.
   - Use exposed misunderstandings to revise the model. Do not confuse a polished explanation produced by the agent with understanding held by the user.
   - Lead with the system's purpose and one end-to-end explanation.
   - Include the minimum useful combination of system map, scenario trace, domain glossary, module/contract table, state lifecycle, decision rationale, and open-question ledger.
   - End with what the user can now explain or change safely, what remains uncertain, and the next evidence that would reduce the most uncertainty.

## Operating Rules

- Explain causality and responsibility boundaries; do not substitute file enumeration for understanding.
- Change abstraction levels deliberately. Connect business purpose to runtime behavior and runtime behavior to implementation evidence.
- Separate a missing understanding from a system defect.
- Do not claim mastery while a critical scenario, state owner, or external dependency remains unexplained.
- Do not require user testing when the user asked only for an initial orientation; label the result as a provisional model rather than completed mastery.
- Produce a durable artifact only when the user asks for one or when the work is long enough that persistence prevents rediscovery.
