# OODA Loop

**Category:** Decision making
**Also known as:** Observe-Orient-Decide-Act loop

## Purpose

Make timely decisions in changing, incomplete-information environments by
cycling through observation, orientation, decision, action, and feedback.

## Use When

- Conditions change faster than a static plan can remain accurate.
- Action can generate valuable feedback.
- Decisions are at least partly reversible or can be bounded.
- Competitive tempo, incident response, or experimentation matters.

## Avoid When

- Action could create irreversible catastrophic harm without prior assurance.
- The environment is stable and a standard procedure already works.
- The real bottleneck is authority, resources, or ethics rather than feedback.
- Speed is being used to excuse poor observation or careless action.

## Inputs

- A current objective, boundary, and timebox.
- Live observations, prior-loop feedback, and signal-quality judgments.
- Relevant constraints, mental models, experience, and stakeholder perspectives.
- Candidate actions, predicted outcomes, and safety limits.

## Procedure

1. **Observe:** gather current signals, changes, anomalies, and feedback. Separate
   observations from interpretations and note data freshness.
2. **Orient:** interpret observations using context, capabilities, prior
   experience, cultural assumptions, and competing hypotheses. Orientation is
   the pivotal step; update the frame rather than merely adding data.
3. **Decide:** select a course of action as a testable hypothesis. Define the
   expected signal, timebox, and boundary.
4. **Act:** execute promptly within the boundary and preserve observability.
5. Feed results immediately into the next Observe phase.
6. Adjust loop speed to risk and information decay. Seek better cycles, not
   motion for its own sake.

## Guiding Questions

- What changed since the last cycle?
- Which signals are current, reliable, and decision-relevant?
- What assumption or mental model shapes our interpretation?
- What competing explanation fits the observations?
- What action would produce useful feedback at acceptable risk?
- What result do we predict, and by when?
- What would trigger continuation, adaptation, escalation, or stop?

## Output Format

| Phase | Content |
|---|---|
| Observe | Signals, freshness, anomalies, prior feedback |
| Orient | Context, hypotheses, assumptions, constraints |
| Decide | Chosen hypothesis, expected result, boundary, timebox |
| Act | Owner, action, instrumentation |
| Next loop | Review time and adapt, continue, stop, or escalate criteria |

## Worked Example

After a software release, error rates rise for one customer segment. The team
observes logs and recent configuration changes, then orients around two plausible
hypotheses rather than assuming a universal defect. It decides to route a small
percentage of affected traffic to the prior configuration, predicts a specific
error reduction, and acts with rollback limits. The next observation confirms
one hypothesis, so the team expands the rollback and begins a new loop focused
on the triggering configuration.

## Common Pitfalls

- Reducing the loop to a linear checklist instead of continuous feedback.
- Skipping orientation and reacting directly to noisy observations.
- Choosing an action without a predicted signal or review time.
- Equating faster cycles with reckless or larger actions.
- Gathering so much data that it becomes stale before use.
- Failing to update identity, assumptions, or strategy when evidence changes.

## Useful Combinations

- **Cynefin Framework** — determine whether experimentation or standard practice
  fits the situation.
- **Ladder of Inference** — improve orientation by checking assumptions.
- **Inversion** — define safety boundaries and stop conditions.
- **Impact-Effort Matrix** — select a small, high-learning action.
