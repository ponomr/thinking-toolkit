# Confidence Determines Speed vs. Quality

**Category:** Decision making
**Also known as:** Problem-solution confidence model, speed-quality confidence matrix

## Purpose

Choose an appropriate product-development trade-off between speed and quality
using confidence in the problem's importance and confidence in the proposed
solution's correctness.

## Use When

- A product team must decide between rapid learning and deeper polish.
- The problem may be unimportant, poorly evidenced, or already validated.
- The solution may be speculative, partially tested, or well understood.
- Work can be staged with explicit quality floors and learning goals.

## Avoid When

- Safety, security, legal, accessibility, or ethical requirements impose a
  non-negotiable quality floor.
- "Quality" and "speed" have not been defined for the context.
- The choice is not about building or delivering a solution.
- Confidence is being used as a substitute for evidence.

## Inputs

- Evidence that the problem is important: frequency, severity, reach, strategic
  fit, and user behavior.
- Evidence that the solution addresses the problem: tests, prototypes, prior
  analogues, and mechanism clarity.
- Quality floors, cost of defects, reversibility, and learning objectives.
- A shared scale for low, medium, and high confidence.

## Procedure

1. Define speed as time to a decision-relevant learning or outcome, not haste.
2. Define quality dimensions and non-negotiable floors.
3. Rate confidence in problem importance using explicit evidence.
4. Rate confidence in solution correctness separately.
5. Choose the posture:
   - low problem confidence: favor a fast, low-cost test before polishing;
   - high problem and low solution confidence: balance speed with enough quality
     to make the test valid and safe;
   - high problem and high solution confidence: invest in durable quality and
     scale readiness;
   - low problem and high solution confidence: challenge the apparent mismatch;
     validate demand before building a polished answer to a weak problem.
6. Define the smallest artifact that can resolve the dominant uncertainty.
7. Set evidence, quality, and stop thresholds before execution.
8. Update both confidence ratings after the result.

## Guiding Questions

- What proves the problem is frequent, severe, or strategically important?
- What proves this solution changes the target outcome?
- Which quality dimensions are mandatory regardless of confidence?
- Would lower quality invalidate the learning?
- What is the smallest safe test that could change our confidence?
- What defects become expensive or irreversible after launch?
- What result justifies more quality investment?

## Output Format

- **Problem confidence:** rating, evidence, and weakest assumption.
- **Solution confidence:** rating, evidence, and weakest assumption.
- **Quality floor:** mandatory dimensions.
- **Chosen posture:** speed, balanced learning, or durable quality.
- **Next artifact:** prototype, experiment, limited release, or production build.
- **Success, stop, and escalation thresholds:** explicit.

## Worked Example

A team proposes an automated weekly report. Interviews suggest reporting is
painful, so confidence in the problem is high. No one has tested whether the
proposed summary is trusted, so solution confidence is low. The team chooses a
balanced posture: a manually generated pilot that preserves data accuracy and
privacy but omits scalable automation. Usage and correction rates determine
whether to invest in production quality.

## Common Pitfalls

- Treating stakeholder conviction as calibrated confidence.
- Equating speed with avoidable defects or quality with perfection.
- Polishing a solution before validating the problem.
- Running a test too poor to produce valid learning.
- Ignoring mandatory quality floors.
- Failing to update confidence after evidence arrives.

## Useful Combinations

- **Impact-Effort Matrix** — prioritize candidate learning activities.
- **OODA Loop** — execute repeated evidence-driven cycles.
- **Inversion** — define unacceptable failure and quality floors.
- **Decision Matrix** — compare solution candidates after confidence improves.
