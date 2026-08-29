# Reality Check Lenses

Use the lenses that can change the decision. The purpose is to expose consequential mismatch between the request and its operating environment, not to complete a universal questionnaire.

## Reality Stack

| Layer | Questions |
| --- | --- |
| Outcome | What observable condition should improve? Who values it, and how much? |
| People and incentives | Who performs, approves, avoids, bypasses, supports, or is harmed by the workflow? |
| Business process | What happens today, including handoffs, queues, exceptions, reconciliation, and workarounds? |
| Physical environment | Which devices, sensors, locations, connectivity, power, ergonomics, or safety limits matter? |
| Software estate | Which systems, versions, interfaces, identity providers, licenses, and deployment models already exist? |
| Data reality | Who creates and owns the data? Is it timely, complete, lawful, interoperable, and recoverable? |
| Operations | Who deploys, monitors, supports, restores, audits, and pays for the capability? |
| Change capacity | Which behavior, training, procurement, migration, policy, or organizational change is required? |

## Scenario Matrix

For each important scenario, record the trigger, environment, expected outcome, constraints, failure response, and owner.

| Scenario | Questions |
| --- | --- |
| Normal | Does the end-to-end workflow work under ordinary conditions? |
| Peak | What changes at maximum realistic load, concurrency, volume, or urgency? |
| Degraded | What happens when a dependency, device, network, data source, or person is unavailable? |
| Recovery | Can work resume without duplication, corruption, silent loss, or unsafe state? |
| Maintenance/change | How are upgrades, schema changes, model changes, device replacement, and rollback handled? |

For safety-critical, physically constrained, or abuse-prone systems, also test accident, misuse, and environmental-boundary scenarios.

## Risk Causal Chain

Write risks as causal claims:

```text
Existing condition or assumption
  -> triggering event
  -> system or workflow response
  -> user/business consequence
  -> evidence or uncertainty
```

Avoid labels such as `integration risk` without explaining the chain.

## Evidence-Buying Experiments

Prefer the smallest experiment that can change the decision:

- observe the real workflow rather than relying on an idealized process map;
- sample actual data and quantify missingness, latency, and mismatch;
- test a dependency contract or device under representative conditions;
- run a thin end-to-end spike through the riskiest boundary;
- rehearse a degraded or recovery scenario;
- ask the accountable operator to validate support and ownership assumptions.

An experiment is useful only if its possible outcomes lead to different decisions.

## Traceability and V&V

For each architecturally or operationally significant requirement, preserve this chain:

```text
business or mission reason
  -> affected stakeholder and real use
  -> requirement
  -> dependency and owner
  -> verification method
  -> validation context
  -> lifecycle monitoring or support consequence
```

- Verification asks whether the delivered solution satisfies the stated requirement.
- Validation asks whether that requirement and solution satisfy the intended use in the real environment.

A requirement can be verifiable yet invalid because it solves the wrong problem. It can also express a valid need while remaining too vague to verify.

## Requirement Reframe

Use this shape when it improves clarity:

```text
For [actor] in [real operating context],
enable [outcome],
under [material constraints and scenarios],
as demonstrated by [observable acceptance evidence].

Assumptions still requiring evidence:
- ...
```
