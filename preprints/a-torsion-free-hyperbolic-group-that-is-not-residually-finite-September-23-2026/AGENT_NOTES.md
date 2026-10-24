# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Seth Douglas and Nidhal Mghirbi, *Non-soficity of OpenAI's torsion-free hyperbolic group*](https://github.com/Apsiape/hyperbolic-group-not-sofic) (GitHub repository with note and Lean code, v1.1.0, Zenodo DOI 10.5281/zenodo.23374284, 2026). Adapts this paper's rank argument against finite quotients to approximate permutation models and claims that the same group is not sofic. The main Lean theorem, `Approx252.exists_torsionFree_wordHyperbolic_not_sofic`, imports the release's development, and the README says the sharper constants and the v1.1.0 additions are proved only on paper.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 252*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/252.md) (lean/docs/252.md). The Lean statement covers the existence of a torsion-free word-hyperbolic group that is not residually finite; nonlinearity over every field is not a separate conclusion of the linked comparator statement. [family-level]
- [OpenAI, *Main.lean (theorem `OAI.Release075.main`)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/Hyperbolic/Main.lean) (openai/math, commit adc7f12). The release's Lean theorem asserts `∃ G, TorsionFree G ∧ WordHyperbolic G ∧ ¬ Group.ResiduallyFinite G`, with hyperbolicity defined by uniformly thin geodesic triangles in a Cayley graph.
- [OpenAI, *TorsionFreeHyperbolic.lean (comparator statement)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/TorsionFreeHyperbolic.lean) (openai/math, commit adc7f12). The comparator challenge statement that the scope note links for the main theorem.
- [Formal Conjectures, *HyperbolicGroupsResiduallyFinite.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Other/HyperbolicGroupsResiduallyFinite.lean) (google-deepmind/formal-conjectures). Independent formal statements of (H1)(a), (H1)(b) and the Kapovich–Wise equivalence, all marked `research solved` with reference to this paper and linking its Lean proof. The proofs are `sorry`, and the docstring says the match between the release's thin-triangle definition and `Group.IsHyperbolic` is not formalized.
- [homeowmorphism, *feat(Other): residual finiteness questions for hyperbolic groups*](https://github.com/google-deepmind/formal-conjectures/pull/6791) (formal-conjectures PR #6791, merged 2026-10-07). Added the formal statements together with word-metric, Gromov-product and hyperbolic-group definitions. The PR says the statements were autoformalized with Claude Opus 5.5 and checked manually. [AI-generated per source]
- [homeowmorphism, *feat(Other): mark residual finiteness of hyperbolic groups as solved*](https://github.com/google-deepmind/formal-conjectures/pull/6921) (formal-conjectures PR #6921, merged 2026-10-08). Marks both questions solved on the basis of this paper. It reports that the release's proof contains no `sorry`/`axiom`/`native_decide` but was not compiled locally, and that the four-point and thin-triangle definitions of hyperbolicity have not been bridged formally.

## Related prior literature mentioned by others
- [G. Baumslag, A. G. Myasnikov, V. Shpilrain, *Open problems in combinatorial group theory: hyperbolic and automatic groups*](https://shpilrain.ccny.cuny.edu/gworld/problems/probhyp.html) (online problem list, Problem (H1)). Formal-conjectures cites this list as the source of questions (H1)(a) "Are hyperbolic groups residually finite?" and (H1)(b), and marks both as answered by this paper; the list is not in the paper's bibliography.
- [M. Bestvina, *Questions in geometric group theory*](https://www.math.utah.edu/~bestvina/eprints/questions-updated.pdf) (problem list, updated July 2004, Q 1.15). Formal-conjectures cites Question 1.15 as an earlier formulation of the residual-finiteness question, with notes distinguishing nonlinearity from failure of residual finiteness; it is not in the paper's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [Rémi Coulon and Denis Osin, *A non-residually finite group acting uniformly properly on a hyperbolic space*](https://arxiv.org/abs/1804.09432) (arXiv:1804.09432, 2018). Constructs a non-residually finite group with a uniformly proper action on a Gromov hyperbolic space, a related setting for the failure of residual finiteness in Theorem 1.1; the paper does not cite it.
- [Xuzhi Tang, *If there is a non-residually finite hyperbolic group, then there is a non-residually finite rigid hyperbolic group*](https://arxiv.org/abs/2305.15650) (arXiv:2305.15650, 2023). A conditional result whose hypothesis is the conclusion of Theorem 1.1, of the same kind as the class-level consequences the paper draws from Kapovich–Wise.
- [Jan Kim and Donghi Lee, *Non-residually finite groups hyperbolic relative to residually finite subgroups*](https://arxiv.org/abs/1903.00838) (arXiv:1903.00838, 2019, withdrawn). An earlier claimed negative answer to the same question, via Baumslag–Solitar groups and a theorem of Osin. The authors withdrew it, citing "an important error in Section 4".

## Digests and expositions
- [Open Mathematics Courses, *A hyperbolic group that is not residually finite*](https://kokunoyumeto.github.io/open-math-courses-public/courses/a-hyperbolic-group-that-is-not-residually-finite/) (online course, accessed 2026-10-21). Seven lessons explain the paper's triangle-complex geometry, punctured-line construction and rank obstruction; the source identifies Claude Opus 5.5 as writer and self-checker and states that independent review is incomplete. [AI-generated per source]

## News and blogs
- None found.
