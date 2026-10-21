# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [琪越 唐 (Hexagon contributor), *A note on counterexamples to homological conjectures*](https://hexagonmath.org/abs/2610.00143v4) (hexagon:2610.00143, v1 2026-10-07, v4 2026-10-15). Extends the constructions of both family papers to any base field containing an element of infinite multiplicative order, and lists counterexamples to the Auslander–Reiten, Gorenstein-projective, Tachikawa, Nakayama-type, finitistic-dimension and Wakamatsu tilting conjectures; the page marks the authorship as mixed human/AI and says "Human understanding: no parts". [AI-generated per source] [family-level]
- [Weiheng Xia, *Global obstruction property and its applications*](https://arxiv.org/abs/2610.12583) (arXiv:2610.12583, 2026-10-08). Proves positive Auslander–Reiten results via a "global obstruction property"; its introduction cites this paper as "a recent preprint by OpenAI [that] proposes a counterexample to ARC" and states that its results do not depend on that counterexample being valid.

## Expert comments and discussion
- [René Marczinzik, *Homological conjectures and problems*](https://sites.google.com/view/rene-marczinzik/homological-conjectures-and-problems) (personal research page, updated 16 October 2026). Discussing the claimed Tachikawa counterexample and its homological consequences, Marczinzik calls for careful checking and proposes a weakly Gorenstein conjecture over fields whose nonzero elements all have finite multiplicative order, outside the fields used by these constructions. [family-level]

## Formalization
- [OpenAI math release, *Counterexamples to Auslander–Reiten, Tachikawa and related homological conjectures: Lean scope* (mirrored on mathcommunity/oai-math-revised)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/199.md) (lean/docs/199.md, 2026). Describes the release's Lean formalization of the eight-simple nonprojective Gorenstein-projective counterexample over F_2(q,H_1,H_2), including A/rad A ≅ k^8, (rad A)^4 ≠ 0 and persistence under every field extension, with the comparator statement `AuslanderReiten.lean`. [family-level]
- [Formal Conjectures (Google DeepMind), *FormalConjectures/Paper/AuslanderReiten.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Paper/AuslanderReiten.lean#L64) (formal-conjectures, statement added in PR #5440, merged 2026-09-22). States the negation of the Artin-algebra Auslander–Reiten conjecture, marked `research solved`, with the statement left as `sorry` and a docstring linking to this paper and to the release's formal proof; the commutative variants remain marked open.

## Related prior literature mentioned by others
- [René Marczinzik, *Gendo-symmetric algebras, dominant dimensions and Gorenstein homological algebra*](https://arxiv.org/abs/1608.04212) (arXiv:1608.04212, 2016; revised 2 September 2021). Marczinzik cites this work on weakly Gorenstein and gendo-symmetric algebras in their response to the OpenAI counterexamples as background for the proposed restriction to fields with torsion multiplicative group. [family-level]
- [Kaito Kimura, *Auslander–Reiten conjecture for normal rings*](https://arxiv.org/abs/2304.03956) (arXiv:2304.03956, 8 April 2023). The formal-conjectures discussion cites this positive result for commutative Noetherian normal rings when distinguishing the still-open general commutative conjecture from OpenAI's noncommutative counterexample.

## Possibly relevant literature (found by the agent, not checked)
- [Justin Lyle, *On the totally acyclic condition and the Auslander-Reiten Conjecture*](https://arxiv.org/abs/2610.00022) (arXiv:2610.00022, 2026-09-01). Proves new cases of the commutative (graded, Gorenstein reduced) Auslander–Reiten conjecture; relevant to the paper's remark that the commutative restriction is not resolved by either construction.

## Digests and expositions
- [AI Proved What?, *No gluing, not projective? Auslander–Reiten and Tachikawa*](https://aiprovedwhat.com/episodes/199-counterexamples-auslander-reiten-tachikawa-related/) (episode 199, October 2026). This AI-assisted video and transcript outline the seed algebra, cone and twist constructions, symmetric transfer and homological consequences, while distinguishing the stated Lean scope from the later consequences. [AI-generated per source] [family-level]

## News and blogs
- None found.
