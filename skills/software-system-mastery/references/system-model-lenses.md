# System Model Lenses

Use this reference when the system spans several abstraction levels, the investigation is broad, or the correct view is unclear. Select lenses according to the user's mastery target; do not complete every section mechanically.

## Lens Menu

| Lens | Question it answers | Typical evidence |
| --- | --- | --- |
| Mission and outcomes | Why does this system exist, for whom, and what counts as success? | requirements, product docs, user flows, SLIs/SLOs |
| Domain model | What concepts, rules, invariants, and boundaries organize the problem? | schemas, types, commands, policies, domain services, vocabulary |
| System context | What actors and external systems interact with it, and through which boundaries? | APIs, events, auth, integrations, network config |
| Runtime scenarios | What happens from trigger to visible outcome in normal and failure paths? | entry points, call chains, traces, logs, tests |
| Data and state | Who owns each state, how does it change, and how long does it live? | schemas, migrations, caches, queues, storage, retention rules |
| Modules and contracts | What responsibility is hidden behind each boundary, and what is promised? | public interfaces, dependency graph, tests, error models |
| Deployment and operations | Where does the system run and how is it configured, observed, recovered, and changed? | manifests, CI/CD, topology, runbooks, dashboards |
| Decisions and tradeoffs | Why is the design this way, and which alternatives or constraints shaped it? | ADRs, commit history, comments, issue discussions |

## Cross-Cutting Quality Attributes

Choose attributes by asking which property would make the user's target scenario succeed or fail. Translate agent-specific concepts into general software concerns:

| Specific mechanism | General concern |
| --- | --- |
| evaluations | verification, validation, and quality evidence |
| traces | observability and execution evidence |
| model or service timeout | dependency failure, availability, and degradation |
| tool idempotency | consistency and retry safety |
| task resume | state persistence, replay, and recovery |
| memory | state and data lifecycle |

For each selected attribute, capture the stimulus, affected part of the system, expected response, measurable response, and evidence that the response is actually achieved.

## Domain and Complexity Checks

- Identify the core domain and give it more analytical attention than generic or supporting capabilities.
- Treat a bounded context as the scope in which a model and language are consistent. Do not infer it from a folder or deployment unit without corroborating evidence.
- When contexts interact, record upstream/downstream expectations and any translation or anti-corruption responsibility.
- Look for deep modules: a small, stable contract that hides substantial implementation knowledge.
- Record change amplification when a conceptually local change requires edits or coordination across many boundaries.
- Record cognitive load when callers must understand unrelated internals to use a contract correctly.
- Record unknown unknowns when the system gives no clear place to discover the impact of a change.

## Evidence Discipline

Use these labels consistently:

- `observed`: directly supported by code, configuration, tests, runtime output, or measured artifacts.
- `reported`: stated by a person or document but not independently verified.
- `inferred`: best explanation of available evidence; include the inference chain.
- `unknown`: important but unsupported; state the next useful evidence.

Also distinguish lifecycle status:

- implemented and active;
- implemented but unused or unreachable;
- partially implemented;
- configured only;
- documented or planned only;
- deprecated or abandoned.

## Useful Deliverable Shapes

Choose only what reduces uncertainty:

- Context map: actors, system boundary, and external dependencies.
- Critical-scenario trace: trigger → decisions → state changes → side effects → response.
- Responsibility map: module, responsibility, owned state, inbound contract, outbound dependency.
- State lifecycle: creation, transitions, persistence, expiration, replay, deletion.
- Decision map: constraint → decision → benefit → cost → evidence.
- Mastery ledger: question, current answer, confidence, evidence, remaining gap.

End with two lists: `Safe reasoning now` and `Still unsafe to assume`. When the goal is genuine ownership rather than orientation, also record the user's teach-back or impact-prediction result and the remaining blind spots.
