# Red Teaming

**Category:** Problem solving
**Also known as:** Adversarial review, devil's advocacy, challenge session

## Contents

- [Purpose](#purpose)
- [Use When](#use-when)
- [Avoid When](#avoid-when)
- [Inputs](#inputs)
- [Procedure](#procedure)
- [Guiding Questions](#guiding-questions)
- [Output Format](#output-format)
- [Worked Example](#worked-example)
- [Common Pitfalls](#common-pitfalls)
- [Useful Combinations](#useful-combinations)

## Purpose

Stress-test a plan, argument, design, or belief by having someone argue the
strongest case against it from an adversary's or skeptic's perspective, so
weaknesses surface before reality finds them.

## Use When

- A high-stakes plan has consensus and no one is incentivized to attack it.
- An intelligent counterparty — competitor, attacker, negotiator, regulator,
  or market — will actively respond to the plan.
- Group confidence has grown faster than the evidence behind it.
- A decision document, forecast, or architecture needs challenge before
  commitment.

## Avoid When

- The team already distrusts the plan; more attack adds heat, not signal.
- No one can play the adversary with genuine independence from the plan's
  authors.
- The challenge would target people or systems without authorization or
  outside agreed boundaries.
- The plan is still a rough draft; premature attack kills exploration.

## Inputs

- The artifact under test: plan, argument, design, or estimate, in reviewable
  form.
- A defined adversary or skeptic perspective with goals and capabilities.
- Explicit scope and rules: what may be attacked, what is out of bounds.
- A red team with independence from the artifact's authors, or at minimum a
  deliberately assigned challenger role.

## Procedure

1. Fix the artifact under test and state what "the plan succeeds" means, so
   attacks target the real success condition.
2. Define the adversary honestly: their goals, capabilities, information, and
   constraints. Avoid assuming they share the defender's values or logic.
3. Set scope, rules of engagement, and a timebox before the attack begins.
4. Attack along independent lines: assumptions that could be false, resources
   that could fail, incentives that could turn, moves the adversary makes in
   response, and the strongest honest argument that the plan is simply wrong.
5. Record each finding with its mechanism: how exactly the weakness leads to
   failure, and what evidence supports its plausibility.
6. Rank findings by severity and plausibility rather than rhetorical force.
7. Hand findings back to the plan's owners for explicit disposition: fix,
   monitor, accept with rationale, or investigate further.
8. Verify that material fixes were made, and schedule re-testing when the
   plan or the adversary's capabilities change.

## Guiding Questions

- What does the adversary want, know, and control?
- What is the strongest honest case that this plan fails or this belief is
  wrong?
- Which single assumption, if false, unravels the most?
- How does the adversary adapt after seeing our first move?
- Which finding is severe and plausible rather than merely clever?
- Who decides what happens with each finding, and by when?
- What changed since the last challenge that invalidates its conclusions?

## Output Format

| Finding | Attack line | Mechanism | Severity | Plausibility | Disposition | Owner |
|---|---|---|---:|---:|---|---|
|  |  |  |  |  |  |  |

Conclude with the top findings, accepted risks with rationale, fixes with
owners, and the trigger for the next challenge.

## Worked Example

A company prepares a price increase, and the plan assumes competitors will
follow within a quarter. A designated red team plays the strongest competitor
and finds a better move: hold prices, run comparison campaigns targeting the
company's largest accounts, and absorb short-term margin loss to capture
share. The red team also attacks an internal assumption that enterprise
customers renew regardless of a 15 percent increase, showing two accounts
where procurement rules force a re-tender above 10 percent. The plan's owners
add a key-account exception below the re-tender threshold and prepare a
response campaign, accepting the remaining risk explicitly.

## Common Pitfalls

- Running a token challenge whose real purpose is to bless the plan.
- Staffing the red team with the plan's authors or their reports, so the
  attack pulls punches.
- Modeling the adversary as a mirror of the defender's own logic and values.
- Rewarding clever-sounding findings over severe and plausible ones.
- Producing findings that no one is obligated to disposition, so nothing
  changes.
- Attacking the presenters instead of the plan, poisoning future candor.

## Useful Combinations

- **Inversion** — generate failure conditions first, then let the red team
  weaponize the material ones.
- **Ladder of Inference** — attack the inferential steps behind a contested
  conclusion.
- **Six Thinking Hats** — contain the challenge inside a Black Hat phase when
  a full red team is too heavy.
- **Decision Matrix** — re-score options after findings change the risk
  picture.
- **`/logic` analysis** — attack an argument's validity with a named fallacy,
  not just a stronger counter-move.
