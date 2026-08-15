# Fallacy Taxonomy

Named reasoning errors, organized by *what* they corrupt: the thesis, the
premises, the inference, or the language. Each entry gives the English and Latin
name, the mechanism, and a modern example. Cite both names in a verdict so the
error is unambiguous.

A fallacy label is a diagnosis, not a rebuttal. Naming "ad hominem" does not make
the underlying claim true; it says *this particular support fails*. Match the
strongest reading of the argument before assigning a label.

## Errors against the thesis

The argument proves something other than what was claimed, or nothing at all.

- **Missing the point — *ignoratio elenchi***. The conclusion reached is not the
  one in dispute, though it resembles it. *Example:* asked whether an app leaks
  user data, the maker answers "ten million people downloaded it" — popularity,
  not safety.
- **Straw man**. Refuting a weakened or distorted version of the opponent's
  claim. *Example:* "You want a code review step? So you think we should never
  ship anything without a committee."
- **Proving too much — *qui nimium probat, nihil probat***. The premises, taken
  seriously, also entail an absurd conclusion, so they establish neither.
  *Example:* "You can't trust Wikipedia, anyone can edit it" — the same argument
  discredits every open-source project the internet runs on.

## Errors against the premises

The premises are unproven, assume the conclusion, or are irrelevant.

- **Begging the question — *petitio principii***. A premise presupposes the truth
  of the thesis. *Example:* "This channel is reliable because it only posts
  verified facts" — "verified" is exactly what's in question.
- **Circular reasoning — *circulus in demonstrando***. Thesis A is supported by B,
  and B is in turn supported by A. *Example:* "The author is trustworthy — how do
  we know? — because his trustworthy books say so."
- **Same by the same — *idem per idem***. A claim restated as its own ground.
  *Example:* "We see through glass because glass is transparent" — transparent
  *means* you can see through it.
- **Appeal to the person — *argumentum ad hominem***. Attacking the arguer instead
  of the argument. *Example:* "What does that blogger know about economics — look
  at the car he drives."
- **Appeal to authority — *argumentum ad verecundiam***. Citing an authority
  outside its competence, or with no authority named at all. *Example:* "Experts
  agree" with no expert, field, or study identified.
- **Appeal to the crowd — *argumentum ad populum***. Wide belief offered as proof.
  *Example:* "Millions use this diet, so it works."
- **Appeal to fear or force — *ad baculum* / *ad misericordiam***. Substituting a
  threat or a plea for pity in place of a reason. *Example:* "Approve the budget
  or the team gets blamed for the miss."

## Errors against the inference

The form does not transmit truth from premises to conclusion.

- **Affirming the consequent**. From "if P then Q" and "Q", concluding "P".
  *Example:* "If the server is down the page fails; the page failed, so the server
  is down" — a bad deploy could also fail the page. See
  [formal validity](formal-validity.md).
- **Denying the antecedent**. From "if P then Q" and "not P", concluding "not Q".
  *Example:* "If it's premium it's fast; this isn't premium, so it's slow."
- **Undistributed middle**. A syllogism whose middle term is never distributed, so
  it links nothing. *Example:* "Managers use spreadsheets; she uses spreadsheets;
  so she's a manager." See [formal validity](formal-validity.md).
- **False cause — *post hoc ergo propter hoc***. Treating sequence as causation.
  *Example:* "We shipped the redesign and signups rose, so the redesign caused
  it" — ignoring a marketing campaign that launched the same week.
- **Hasty generalization**. A sweeping claim from too few or unrepresentative
  cases. *Example:* "Two users complained about the new flow, so users hate it."
- **False dilemma**. Presenting two options as exhaustive when others exist.
  *Example:* "Either we rewrite the service or we live with the bug forever."
- **Slippery slope**. Asserting an unsupported chain from a small step to an
  extreme outcome. *Example:* "If we allow one exception, all standards collapse."
- **Sweeping vs. hasty accident — *a dicto simpliciter***. Applying a general rule
  to an exception, or generalizing an exceptional case into a rule. *Example:*
  "Exercise is healthy, so this patient with an acute injury should run."

## Errors of language

The words, not the reasoning, carry the mistake.

- **Equivocation — *homonymia***. A key term shifts meaning between premises.
  *Example:* a debate about "free speech" where one side means a legal right and
  the other means freedom from any consequence — one word, two concepts. This
  breaks the [law of identity](overview.md).
- **Amphiboly**. Ambiguous grammar, not an ambiguous word, carries a false
  inference. *Example:* "The policy covers employees working from home in
  California" — which clause does "in California" bind?
- **False precision**. Dressing a guess as a measurement. *Example:* "This change
  improves retention by 23.4%" from an uninstrumented hunch.

## Second-order tells (imitated rigor)

Modern text sometimes performs the *look* of good reasoning without the substance.
Flag by content, not by style: a device is a fallacy only when it is empty.

- **False balance**. Presenting two positions as equally supported when the
  evidence is lopsided.
- **Rhetorical question as premise**. A question posed as though it settles a
  point it never argues. *Example:* "Do we really want to be the team that ships
  bugs?" standing in for a case.
- **Cited-authority theater**. "Studies show", "data suggests", "research
  confirms" with nothing citable behind it — a dressed-up
  [appeal to authority](#errors-against-the-premises).

## Useful combinations

- **[Ladder of Inference](../references/ladder-of-inference.md)** — trace an
  unsupported-leap fallacy rung by rung to find where evidence ran out.
- **[Inversion](../references/inversion.md)** — surface the failure the false
  dilemma or slippery slope is hiding.
- **[First Principles](../references/first-principles.md)** — dismantle a
  question-begging premise instead of accepting it.
