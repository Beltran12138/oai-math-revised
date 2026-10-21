# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 348: Nonnegative-curvature Einstein classification and an L² topological gap*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/348.md) (lean/docs/348.md, 2026). The scope note names this manuscript and says the Lean development covers its classification theorem (round S⁴, Fubini–Study CP², round RP⁴, no orientability assumption), linking to a comparator statement.
- [OpenAI math release, *EinsteinFour.lean* (comparator challenge statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/EinsteinFour.lean) (github.com/openai/math, commit adc7f12, 2026). Target statements `orientedClassification`, `classificationOn` and `classification` for this paper's main theorem, stated there with `sorry` as the challenge to be matched.
- [OpenAI math release, *OAI/Geometry/EinsteinFour/Classification.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/EinsteinFour/Classification.lean) (github.com/openai/math, commit adc7f12, 2026). Solution module stating `classification` for this paper's Theorem 1.1; its proof calls `classificationOn` from imported modules, which the agent did not inspect.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Z. Zhang, *Four-dimensional Einstein manifolds with sectional curvature bounded from above*](https://arxiv.org/abs/1606.01157) (arXiv:1606.01157, 2016). Proves that a nonnegatively curved Einstein four-manifold satisfying a pinching condition is S⁴, RP⁴ or CP²; this is another quantitative upper-bound result in the line (Yang, Costa, Cao–Tran) surveyed in the introduction, and it is not cited.
- [T. Liu, *Toric Einstein 4-manifolds with nonnegative sectional curvature*](https://arxiv.org/abs/2311.04840) (arXiv:2311.04840; Ann. Global Anal. Geom. 67 (2025), 14). Shows that T²-invariant Einstein metrics with nonnegative sectional curvature are locally symmetric; this symmetry-based partial result is cited in the companion papers but not here, next to the Killing-field corollary of Cheng.

## Digests and expositions
- [Latent Seminar, *Einstein four-manifolds: curvature rigidity and an L² topological gap*](https://lowrank.github.io/latent-seminar/OpenAI-Math/348-einstein-four-manifold-rigidity) (7 October 2026). Explains the three manuscripts’ dependencies, coupled Weyl estimates and Ricci-flow gap argument, and distinguishes its reported arithmetic checks from verification of the complete proofs. [family-level]
- [Gradient Damage, *Calabi Flow, Affine Bernstein Problem and 7 More in Differential Geometry*](https://gradientdamage.com/videos/calabi-flow-affine-bernstein-problem-and-7-more-in-differential/) (15 October 2026). The opening chapter presents the family’s nonnegative-curvature classification and topological-gap claims as an illustrative animation. [family-level]

## News and blogs
- None found.
