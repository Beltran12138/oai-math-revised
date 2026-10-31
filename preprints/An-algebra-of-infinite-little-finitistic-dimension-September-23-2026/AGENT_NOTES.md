# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Qiyue Tang (琪越 唐), *A note of refinements to an algebra of infinite little finitistic dimension*](https://hexagonmath.org/abs/2610.00140v5) (hexagon:2610.00140v5, v1 Oct 7, 2026, v5 Oct 13, 2026). Builds on this paper and extends the construction to every field, stating stronger bounds including a split basic algebra with seventh radical power zero and pairwise Hom-orthogonal brick test modules of Loewy length three; the page labels the text as mixed human/AI-written and links a Lean formalization. [AI-generated per source]
- [Andy Jiang, *Another Counterexample to Little Finitistic Dimension Conjecture*](https://hexagonmath.org/abs/2610.00232v1) (hexagon:2610.00232v1, Oct 14, 2026). Proposes a characteristic-zero variant using homogenized enveloping algebras and the Casimir operator, adapting OpenAI's square-zero-extension step; the author states the representation-theoretic inputs have not been checked. [AI-generated per source]
- [Weiheng Xia, *Global obstruction property and its applications*](https://arxiv.org/abs/2610.12583) (arXiv:2610.12583, Oct 8, 2026). Cites this paper in its introduction as proposing an algebra of infinite little finitistic dimension and states that its own finitistic-dimension results are independent of that construction.
- [Qiyue Tang (琪越 唐), *A note on counterexamples to homological conjectures*](https://hexagonmath.org/abs/2610.00143v4) (hexagon:2610.00143v4, Oct 15, 2026). Builds on the release's Auslander–Reiten and Tachikawa papers (not on this one) and claims counterexamples to the little and big finitistic dimension conjectures over any field with an element of infinite multiplicative order; the page records "Human understanding: no parts". [family-level]
- [Kevin Coulembier and Edmund Heng, *A subcategory with remarkable homological properties via actions of tensor categories*](https://arxiv.org/abs/2610.17646) (arXiv:2610.17646, Oct 13, 2026). States the small finitistic dimension conjecture alongside its Theorem 1.5, on computing finitistic dimension by a subcategory, with a footnote that "a counterexample to this conjecture was announced by an AI company"; the footnote names neither the company nor the paper.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for result 198*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/198.md) (lean/docs/198.md, 2026-10-06). The release's own Lean formalization of Theorem 1.1 (modules with $2m-2\le\mathrm{pd}<\infty$ over a fixed complex algebra) and of the left–right asymmetry corollary, with comparator statements `LittleFinitistic.lean` and `FinitisticAsymmetry.lean`.
- [tqyqiqi1509, *Note198-formalization*](https://github.com/tqyqiqi1509/Note198-formalization) (GitHub, Lean 4.34.1, linked from hexagon:2610.00140 as added 2026-10-10). Independent Lean formalization of Tang's refinement note; its [verification report](https://github.com/tqyqiqi1509/Note198-formalization/blob/main/VERIFICATION.md) records 58 targets in 28 Comparator groups passing with only standard axioms, distinguishes this from complete human review, and says AI assistance was used.

## Related prior literature mentioned by others
- [Lieven Le Bruyn and S. P. Smith, *Homogenized sl(2)*](https://sites.math.washington.edu/~smith/Research/Homog-sl2.pdf) (Proc. Amer. Math. Soc. 118, 725–730, 1993). Cited by Jiang's follow-up as the source on homogenized enveloping algebras used in its alternative construction.

## Possibly relevant literature (found by the agent, not checked)
- [Liang Chen, *Big Finitistic Dimensions of Radical-Cube-Zero Algebras*](https://arxiv.org/abs/2610.00433) (arXiv:2610.00433, Sep 30, 2026). Claims, over any field, a ten-dimensional radical-cube-zero algebra with infinite big finitistic dimension; relevant to the paper's remark that its algebra also has infinite big finitistic dimension and to its citation of radical-cube-zero little finiteness (Green–Huisgen-Zimmermann).
- [Eric J. Hanson and Kiyoshi Igusa, *A counterexample to the $\phi$-dimension conjecture*](https://arxiv.org/abs/1911.00614) (Math. Z. 300 (2022), 807–826). Disproves finiteness of the Igusa–Todorov $\phi$-dimension, an upper bound for findim; relevant to the paper's discussion of Igusa–Todorov invariants.

## Digests and expositions
- [Open Mathematics Courses, *An algebra of infinite little finitistic dimension*](https://kokunoyumeto.github.io/open-math-courses-public/courses/infinite-little-finitistic-dimension/) (online course, undated). Eight lessons with proofs and exercises following the manuscript from selection through localization and bimodule simulation to trivial extensions; authorship is attributed to Claude Opus 5.5 and independent review is described as incomplete. [AI-generated per source]
- [AI Proved What?, *No ceiling? The little finitistic-dimension conjecture*](https://aiprovedwhat.com/episodes/198-counterexample-finitistic-dimension-finiteness/) (episode 198, October 2026). Animated explanation and written account of the fixed-algebra claim and four construction stages; its authors state they did not run the Lean checks. [AI-generated per source]

## News and blogs
- [Gradient Damage, *Finitistic Dimension Conjecture: OpenAI Claims a Counterexample*](https://gradientdamage.com/videos/finitistic-dimension-conjecture-openai-claims-a-counterexample/) (video post, 2026-10-16). Discusses this manuscript through an illustrative Nakayama-algebra animation and distinguishes its schematic depiction of unbounded projective dimensions from OpenAI's actual algebra.
