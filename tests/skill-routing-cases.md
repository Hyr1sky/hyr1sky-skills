# Skill Routing Cases

These cases test selection boundaries, not exact wording. A passing result chooses the expected primary skill, avoids the excluded skills, and sequences multiple skills only when their jobs are genuinely distinct.

## Primary Decision Rule

| Center object | Primary skill | Completion condition |
| --- | --- | --- |
| One paper or document as a learning object | `deep-reading-tutor` | The user has navigated, been tested on, and reinforced weak points in the source. |
| A codebase as a sourced explanatory artifact | `research-codebase-to-wiki` | A factual wiki explains the repo and anchors claims in code or sources. |
| An existing software system as a mental model | `software-system-mastery` | The user can reason across relevant views and trace critical scenarios. |
| An unconfirmed requirement as a decision | `requirements-reality-check` | Need, operating reality, assumptions, risks, and readiness are explicit. |
| Established project truth as communication | `project-narrative-builder` | A specific audience can understand, decide, or act. |
| Intended versus as-built architecture as a comparison | `architecture-drift-audit` | Consequential differences are evidenced, classified, and reconciled. |

## Software System Mastery

### Should select

1. “I take ownership of this payments service next week. Help me understand how a refund travels from API request through ledger state, events, retries, and reconciliation so I can change it safely.”
2. “Explain this platform from business purpose down to runtime and deployment. I need to predict what breaks if we move tenant configuration.”
3. “The repo is only part of a larger hardware-and-cloud system. Build me a coherent mental model across devices, gateway, backend, data ownership, and failure recovery.”
4. “I understand the individual modules but not why they are divided this way or how consistency and availability trade off.”

### Should not select

1. “Turn this research repository into a Wiki with Task/Method/Dataset/Metric/Result.” → `research-codebase-to-wiki`
2. “Read this DDD article with me, quiz me one question at a time, then make notes.” → `deep-reading-tutor`
3. “Compare the module rules in our ADRs with the current imports.” → `architecture-drift-audit`
4. “Implement this already-specified endpoint.” → ordinary implementation workflow

## Requirements Reality Check

### Should select

1. “Operations wants real-time warehouse location from existing handheld devices. Check whether this is a real requirement and what the current network, hardware, workflow, data, and support model imply.”
2. “Before committing to offline mode, find the assumptions we are making about devices, synchronization, conflicts, user behavior, and recovery.”
3. “This AI feature sounds attractive, but I want a premortem grounded in the actual business process and available data.”
4. “The customer says the report must load in one second. Determine what outcome they need, what their environment can support, and what evidence we need before specifying it.”

### Should not select

1. “The approved spec and acceptance tests are attached; implement it.” → implementation workflow
2. “Design a greenfield event-driven architecture for these settled requirements.” → architecture design workflow
3. “Why is the current service timing out?” → bug diagnosis
4. “Does the implementation still follow our data ownership ADR?” → `architecture-drift-audit`

## Project Narrative Builder

### Should select

1. “Turn these verified project findings into a five-minute briefing that helps the COO decide whether to fund rollout.”
2. “Explain the same system separately to a new backend engineer, a hospital administrator, and a regulator.”
3. “The demo works, but the story is organized around our sprint history. Rebuild it around the buyer's problem, evidence, tradeoffs, and decision.”
4. “Create the content architecture and proof sequence for a technical proposal; another skill will render the slides.”

### Should not select

1. “Research this repo and discover what it actually implements.” → `research-codebase-to-wiki` or `software-system-mastery`, depending on the requested outcome
2. “Fix grammar and punctuation without changing structure.” → ordinary editing
3. “Create a polished PPT from this already-approved storyboard.” → presentation skill
4. “Invent metrics that make this prototype sound production-ready.” → refuse fabrication

## Architecture Drift Audit

### Should select

1. “Our ADR says domain modules cannot write each other's tables. Compare that intent with current code paths and migrations.”
2. “Recover the intended architecture from old diagrams and decisions, map the as-built system, and tell us whether differences are erosion or legitimate evolution.”
3. “Audit service responsibilities, contracts, and dependency direction before we split the team.”
4. “Make the original blueprint visible, identify drift, and propose fitness functions for the few boundaries that matter.”

### Should not select

1. “Review this pull request for code quality and regressions.” → code review workflow
2. “Diagnose why checkout fails after deploy.” → bug diagnosis
3. “Design the architecture for a new product with no existing implementation.” → architecture design workflow
4. “Give me a general overview of this unfamiliar system.” → `software-system-mastery`

## Composition Cases

1. “We need an investor narrative, but nobody knows what the repo truly supports.”
   - First establish facts with `research-codebase-to-wiki` or a targeted `software-system-mastery` pass.
   - Then use `project-narrative-builder` for the investor decision.

2. “Audit architectural drift in a system the team cannot yet explain.”
   - First use `software-system-mastery` until intended and as-built boundaries can be compared.
   - Then use `architecture-drift-audit`.

3. “The customer wants a new capability and asks for an architecture proposal and executive deck.”
   - First use `requirements-reality-check`.
   - Design only after readiness is sufficient.
   - Use `project-narrative-builder` after the recommendation and evidence are established, then render the deck with a presentation skill.

4. “A wiki already exists; help the new owner understand the system and practice tracing failures.”
   - Use the wiki as evidence for `software-system-mastery`; do not regenerate it by default.

## Failure Signals

- A skill activates because the request contains a broad word such as “project,” “architecture,” or “requirements,” while its center object is different.
- The workflow creates a polished artifact before establishing facts or audience decision.
- `software-system-mastery` produces only a file inventory or generic architecture checklist.
- `requirements-reality-check` turns all unknowns into blocking questions or jumps directly to solution design.
- `project-narrative-builder` hides uncertainty to improve persuasion.
- `architecture-drift-audit` assumes every difference is a code defect or overwrites historical intent.
