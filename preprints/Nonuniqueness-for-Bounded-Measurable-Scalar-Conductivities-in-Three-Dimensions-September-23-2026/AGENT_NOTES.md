# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 365*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/365.md) (lean/docs/365.md, Oct 2026). The scope document covers only this paper's Theorem 1.1 on the ball B(0,3) ⊂ ℝ³, describing formalized scalar nonuniqueness with uniform positivity, agreement with one near the boundary, distinctness on a set of positive volume, identical full weak Dirichlet-to-Neumann operators, and unique weak solvability for every boundary trace.
- [OpenAI math release, *Conductivity.lean* (comparator challenge statement)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/Conductivity.lean) (lean/ComparatorChallenges, Oct 2026). The Lean statement of the nonuniqueness theorem used as the comparator target; its body here is `sorry` by design. `Conductivity.json` names the module `OAI.Analysis.Conductivity.Main` as the release's proof of this statement.
- [OpenAI math release, *OAI/Analysis/Conductivity/Main.lean*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/OAI/Analysis/Conductivity/Main.lean) (Lean solution module, Oct 2026). This module contains the proof of `main_nonuniqueness` and has no `sorry` in the file itself; it imports roughly 15 further modules.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Santacesaria, *Note on Calderón's inverse problem for measurable conductivities*](https://arxiv.org/abs/1803.06931) (Inverse Problems & Imaging 13 (2019) 149–157). It proposes a Clifford-algebra approach as a possible first step toward $L^\infty$ uniqueness in dimension ≥ 3, the question that Theorem 1.1 answers negatively.
- [Greenleaf, Lassas, Uhlmann, *On nonuniqueness for Calderón's inverse problem*](https://arxiv.org/abs/math/0302258) (arXiv:math/0302258, 2003; Math. Res. Letters). It constructs anisotropic conductivities, singular near an interior surface, with the same DN map as a homogeneous one, an earlier nonuniqueness mechanism distinct from the paper's bounded, uniformly positive scalar setting.
- [Boaz Haberman and Daniel Tataru, *Uniqueness in Calderon's problem with Lipschitz conductivities*](https://arxiv.org/abs/1108.6068) (arXiv:1108.6068; Duke Mathematical Journal 162, 2013). Its uniqueness results for arbitrary continuously differentiable conductivities and Lipschitz conductivities sufficiently close to the identity provide a regularity comparison for this paper’s claimed nonuniqueness with only bounded measurability.

## Digests and expositions
- None found.

## News and blogs
- None found.
