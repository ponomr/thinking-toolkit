# Inversion

**Category:** Problem solving
**Also known as:** Reverse thinking, premortem reasoning

## Purpose

Approach a goal from the opposite direction: identify how failure would occur,
what the worst decision would look like, or what conditions guarantee the
undesired outcome, then design to prevent or reverse those conditions.

## Use When

- Optimistic planning is hiding failure modes.
- A team needs a premortem before a project or decision.
- Direct solution generation is stuck in familiar patterns.
- Prevention is more reliable than maximizing upside.

## Avoid When

- The group is already immobilized by fear or excessive risk aversion.
- Immediate positive generation is needed before critique.
- The task depends mainly on discovering a causal mechanism from evidence.
- Imagined failure could be mistaken for a forecast rather than a hypothesis.

## Inputs

- A desired outcome, proposed decision, or project plan.
- Relevant constraints, stakeholders, and time horizon.
- Known vulnerabilities, dependencies, and prior failures.
- A threshold for unacceptable outcomes.

## Procedure

1. State the desired outcome and the decision or plan being tested.
2. Choose an inversion prompt:
   - What would guarantee failure?
   - What is the worst plausible decision?
   - Imagine the project failed; what caused it?
   - What would the opposite of success look like?
3. Generate failure conditions without immediately debating probability.
4. Explain the mechanism that makes each condition harmful.
5. Separate preventable risks, detectable risks, transferable risks, and risks
   that must be accepted.
6. Reverse the most material conditions into safeguards, design requirements,
   monitoring signals, or stop rules.
7. Assign an owner and timing to each selected safeguard.
8. Check that risk controls do not destroy the intended value or make action
   impossible.

## Guiding Questions

- If this failed badly, what would probably have happened?
- Which assumption would have been false?
- What behavior or incentive could undermine the plan?
- What warning sign would appear early?
- Which failure is severe, plausible, and preventable?
- What is the opposite condition, and how can we create it?
- What risk remains after safeguards?

## Output Format

| Failure condition | Mechanism | Severity | Plausibility | Early signal | Prevention or response | Owner |
|---|---|---:|---:|---|---|---|
|  |  |  |  |  |  |  |

Conclude with top safeguards, residual risk, stop conditions, and review date.

## Worked Example

Before migrating a customer database, a team imagines the migration has failed.
Causes include incomplete backups, unnoticed schema mismatch, unavailable domain
experts, and a rollback that was documented but never tested. The team converts
these into restore verification, sample migrations, expert on-call coverage, and
a timed rollback rehearsal. The premortem changes the plan without claiming the
failure scenarios are predictions.

## Common Pitfalls

- Generating dramatic scenarios without causal mechanisms.
- Treating possibility as probability.
- Creating controls for every risk regardless of materiality.
- Using inversion to reject all action.
- Naming safeguards without owners, signals, or tests.
- Ignoring new costs and failure modes introduced by the controls.

## Useful Combinations

- **Second-Order Thinking** — trace how a failure condition develops over time.
- **Six Thinking Hats** — use inversion as a disciplined Black Hat phase.
- **Decision Matrix** — add verified risks without double-counting them.
- **OODA Loop** — monitor warning signals and adapt safeguards.
- **`/logic` analysis** — turn a suspected weakness into a named formal or
  informal fallacy.
