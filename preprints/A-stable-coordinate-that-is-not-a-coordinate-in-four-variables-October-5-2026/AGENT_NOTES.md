# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 049: A stable-coordinate counterexample in four variables*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/049.md) (release Lean docs, October 2026). Describes the formalized scope: a degree-five one-stable noncoordinate in four variables whose fibres are all affine three-space and nonrectifiable, the Abhyankar–Sathaye statement for every n ≥ 4, and a related commuting-derivations statement, with links to the three Comparator challenges. [family-level]
- [OpenAI math release, *StableCoordinateFour.lean* (comparator statement)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/StableCoordinateFour.lean) (openai/math, added in the 7 October 2026 update). Lean statement `OAI.StableCoordinate.principal_package` encoding Theorem 1.1 (degree five, one-stable coordinate, not a coordinate) and Corollary 1.2 (every fibre ≅ A³, not rectifiable); the proof field in this statement file is `sorry`. Comparator challenge files leave the proof as `sorry` by design; `StableCoordinateFour.json` names the module `OAI.AlgebraicGeometry.StableCoordinate.Principal` as the release's proof of this statement.
- [OpenAI math release, *AbhyankarSathaye.lean* (comparator statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/AbhyankarSathaye.lean) (openai/math, October 2026). Lean statement `OAI.AbhyankarSathaye.exists_noncoordinate_polynomial` (for every n ≥ 4 a noncoordinate F with quotient ≅ ℂ^[n-1]), the Abhyankar–Sathaye consequence shared by both papers; the proof field in this statement file is `sorry`. Comparator challenge files leave the proof as `sorry` by design; `AbhyankarSathaye.json` names the module `OAI.AlgebraicGeometry.AbhyankarSathaye.Counterexample` as the release's proof of this statement. [family-level]

## Related prior literature mentioned by others
- [Vladimir Shpilrain and Jie-Tai Yu, *Affine varieties with equivalent cylinders*](https://arxiv.org/abs/math/0110324) (arXiv:math/0110324, 2001). The AI Proved What? episode links this paper for the stable coordinate conjecture and its low-dimensional background; it is also in the October manuscript's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [Vladimir L. Popov, *Around the Abhyankar–Sathaye conjecture*](https://arxiv.org/abs/1409.6330) (arXiv:1409.6330, 2014). Survey-type paper on the conjecture and on commuting locally nilpotent derivations, relevant to the paper's claim that Corollary 1.2 disproves the Abhyankar–Sathaye conjecture in ambient dimension four.
- [Shulim Kaliman and Mikhail Zaidenberg, *Venereau polynomials and related fiber bundles*](https://arxiv.org/abs/math/0308191) (arXiv:math/0308191, 2003). Studies Vénéreau polynomials on A⁴ with all fibres ≅ A³ via fibre bundles, the testing ground the introduction discusses alongside Lewis and Blanc–Poloni.
- [Parnashree Ghosh and Neena Gupta, *On the triviality of a family of linear hyperplanes*](https://arxiv.org/abs/2206.15210) (arXiv:2206.15210, 2022/2023). Gives higher-dimensional families of linear hyperplanes for which the Abhyankar–Sathaye conjecture holds, a point of comparison for the paper's four-dimensional counterexample.

## Digests and expositions
- [AI Proved What?, *One variable too few? A stable coordinate that is not a coordinate*](https://aiprovedwhat.com/episodes/049-stable-coordinate-counterexample-four-variables/) (episode 049, October 2026). This AI-assisted video and transcript explain both constructions, outline the October paper's filtration and derivation obstruction, and distinguish it from the September paper's critical-point argument. [AI-generated per source] [family-level]

## News and blogs
- None found.
