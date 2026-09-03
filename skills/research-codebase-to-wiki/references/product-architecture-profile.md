# Product Architecture Profile

Use this profile for an application, platform, runtime, developer tool, or other product system. The goal is a navigable factual model of the current repository, not a paper-style survey and not proof that the user has mastered the system.

## Start from authority and reality

Read repository instructions, domain vocabulary, accepted decisions, architecture documents, current plans, release notes, manifests, schemas, entrypoints, and tests. Treat prose as intended meaning and executable artifacts as implementation evidence; preserve contradictions instead of smoothing them over.

## Recommended information architecture

Choose only sections supported by the system and the user's purpose. A mature system often benefits from this order:

1. **One-picture system map** — product loop, runtime spine, and improvement/control loop.
2. **Load-bearing design decisions** — the few choices that explain most module placement.
3. **Modules and dependency direction** — responsibility, interface, implementation, seam, and adapter where those terms are useful.
4. **Domain and identity model** — entities, stable identifiers, versioning, state machines, and anti-confusions.
5. **Critical scenarios** — trigger → control flow → state changes → result → failure behavior.
6. **Events and observability** — event source, span/trace shape, projections, retries, and debugging value.
7. **Persistence and sources of truth** — stores, ownership, retention, migrations, derived projections, and transaction semantics.
8. **Evaluation and reliability** — tests, replay, evals, human gates, quality attributes, and what remains unproved.
9. **Interfaces and deployment** — user channels, adapters, process topology, external dependencies, and runtime constraints.
10. **Glossary and stable fields** — terms whose confusion would cause incorrect changes.
11. **Code tour** — a small set of real excerpts that demonstrate ownership and control flow.
12. **Debugging path** — a symptom-to-evidence sequence using the repository's actual tools.
13. **Architecture explanation** — how to explain the system as problem → decision → mechanism → evidence → limit.
14. **Current / next / closed** — implementation status without reinterpreting the roadmap.
15. **Learning route** — optional; include only when the user wants onboarding or self-study.

Do not force all fifteen sections. Small systems should remain small.

## Critical scenario template

For each selected scenario capture:

| Field | Question |
| --- | --- |
| Trigger | What starts the scenario? |
| Input | What trusted and untrusted data enters? |
| Control | Which module owns orchestration? |
| Decisions | What is deterministic, model-driven, or human-gated? |
| State | What is committed, projected, or ephemeral? |
| Events | What proves progress and terminal status? |
| Failure | What fails closed, retries, or remains recoverable? |
| Result | What can the user observe? |

## Diagrams

Use diagrams to explain relationships that prose cannot show compactly:

- system/context map for major modules and external systems;
- sequence diagram for one critical scenario;
- state diagram for a lifecycle with meaningful transitions;
- data lineage for source-of-truth and projection relationships.

Keep each diagram tied to repository evidence. Label inferred edges and omit decorative architecture that has no current implementation.

## Code tour

Prefer 3–7 excerpts. Each excerpt should answer a responsibility question such as:

- Where is the invariant enforced?
- Who owns the transaction or background task?
- Where does an external adapter become a domain value?
- Which event proves the state transition?
- What prevents a retry from duplicating a side effect?

Do not use snippets merely because they are central files.

## Completion check

The wiki is ready when a reader can locate the source of truth, trace at least one important scenario, distinguish current behavior from plans, identify the main failure evidence, and follow every load-bearing claim back to a file, symbol, test, decision, or runtime artifact.
