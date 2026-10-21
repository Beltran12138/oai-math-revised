# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [琪越 唐 (Hexagon contributor), *A note on counterexamples to homological conjectures*](https://hexagonmath.org/abs/2610.00143v4) (hexagon:2610.00143, v1 2026-10-07, v4 2026-10-15). Extends the constructions of both family papers to any base field containing an element of infinite multiplicative order, and lists counterexamples to both Tachikawa conjectures, the Auslander–Reiten, Nakayama-type, Auslander–Gorenstein, finitistic-dimension and Wakamatsu tilting conjectures; the page marks the authorship as mixed human/AI and says "Human understanding: no parts". [AI-generated per source] [family-level]
- [Kenta Kitamura, *tachikawa-characteristic-zero* (repository with the manuscript "A characteristic-zero Tachikawa counterexample")](https://github.com/KitaKen1/tachikawa-characteristic-zero) (GitHub, October 2026). Its README says it adapts this paper's characteristic-two example to a finite-dimensional symmetric Q-algebra with a nonprojective self-orthogonal module, with a Lean 4 proof; the README discloses ChatGPT/Codex assistance and lists independent review as outstanding. [AI-generated per source]

## Comments and discussion
- [René Marczinzik, *Homological conjectures and problems*](https://sites.google.com/view/rene-marczinzik/homological-conjectures-and-problems) (personal research page, updated 16 October 2026). Discussing the claimed Tachikawa counterexample and its homological consequences, Marczinzik calls for careful checking and proposes a weakly Gorenstein conjecture over fields whose nonzero elements all have finite multiplicative order, outside the fields used by these constructions. [family-level]

## Formalization
- [OpenAI math release, *Counterexamples to Auslander–Reiten, Tachikawa and related homological conjectures: Lean scope* (mirrored on mathcommunity/oai-math-revised)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/199.md) (lean/docs/199.md, 2026). Describes the release's Lean formalization of Theorem 1.1 (a symmetric algebra over F_2(q,H_1,H_2) and a nonprojective module M with Ext^i(M,M)=0 for i>0), with comparator statement `Tachikawa.lean`; the field-extension, endomorphism-algebra and other homological corollaries are listed as not formalized. [family-level]
- [KitaKen1 (Kenta Kitamura), *Formalize Tachikawa's second conjecture over ℚ and record an external Lean counterexample*](https://github.com/google-deepmind/formal-conjectures/pull/7067) (formal-conjectures PR #7067, opened 2026-10-10, open). Proposes a Formal Conjectures statement of the rational symmetric case marked `answer(False)`, with the proof in the external repository above; a reviewer accepted the statement's fidelity but asked for independent verification of the linked proof before approval.

## Related prior literature mentioned by others
- [René Marczinzik, *Gendo-symmetric algebras, dominant dimensions and Gorenstein homological algebra*](https://arxiv.org/abs/1608.04212) (arXiv:1608.04212, 2016; revised 2 September 2021). Marczinzik cites this work on weakly Gorenstein and gendo-symmetric algebras in their response to the OpenAI counterexamples as background for the proposed restriction to fields with torsion multiplicative group. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Liang Chen, *Big Finitistic Dimensions of Radical-Cube-Zero Algebras*](https://arxiv.org/abs/2610.00433) (arXiv:2610.00433, 2026-09-30). Constructs a ten-dimensional radical-cube-zero algebra over any field with infinite big finitistic dimension; relevant to Corollary 1.3 (infinite little and big finitistic dimension of Γ_K).

## Digests and expositions
- [AI Proved What?, *No gluing, not projective? Auslander–Reiten and Tachikawa*](https://aiprovedwhat.com/episodes/199-counterexamples-auslander-reiten-tachikawa-related/) (episode 199, October 2026). This AI-assisted video and transcript outline the seed algebra, cone and twist constructions, symmetric transfer and homological consequences, while distinguishing the stated Lean scope from the later consequences. [AI-generated per source] [family-level]

## News and blogs
- None found.
