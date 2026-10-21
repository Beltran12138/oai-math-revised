# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [F.-U. Caja-Lopez, M. G. Delgadino, J. Kitagawa, *Stability of optimal transport maps and second variation of the 2-Monge–Kantorovich distance*](https://arxiv.org/abs/2605.24232) (arXiv:2605.24232v2, revised 19 Oct 2026). This paper is in the manuscript's bibliography as v1; v2 adds a citation of "the manuscript released by OpenAI" as showing that their bound (1.3) holds with sharp exponent α=1/3 for a uniform source on a convex body.
- [Songbo Wang, Xiaozhen Wang, *Quantitative stability of optimal transport via regularization*](https://arxiv.org/abs/2610.09640) (arXiv:2610.09640, 7 Oct 2026). Proves W₂-Hölder map stability for L^p source densities via regularized Brenier potentials and cites "the OpenAI preprint" for the sharp W₂^{1/3} estimate for uniform sources on convex bodies; the authors also disclose a dialogue with OpenAI Codex in an AI-use section.
- [Bang-Xian Han, Zhuo-Nan Zhu, *Stability of optimal transport on sub-Riemannian manifolds*](https://arxiv.org/abs/2610.09688) (arXiv:2610.09688, 7 Oct 2026). Proves a W₁^{1/4} map estimate on Riemannian and fat sub-Riemannian manifolds, describes the OpenAI preprint as a concurrent work whose example "disproves the square-root conjecture", and notes that its own W₁ estimate does not give a W₂^{1/3} bound in its settings.
- [Anonymous, *Exact sensitivity certificates for planar transport maps: coefficient uncertainty, a convergent box refinement and a sharp three-atom calibration*](https://evidencepress.org/releases/planar-transport-map-sensitivity-certificates/) (Evidence Press, version 0.2.0-candidate, 2026-10-07; DOI 10.5281/zenodo.23205731). This unrefereed work extends OpenAI's three-atom construction with exact planar sensitivity formulas and coefficient-box certificates, explicitly stating that it neither uses nor validates the general one-third theorem. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Sharp one-third stability of Brenier maps — Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/374.md) (lean/docs/374.md, OpenAI math release, 2026-10-06). States that the Lean development covers both the uniform W₂^{1/3} bound for targets in a fixed compact set and the three-atom sharpness on a cube, with comparator statement `lean/ComparatorChallenges/Brenier.lean`. [AI-generated per source]
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit at commit fd4aeeb2, 2026-10-10). The audit reports that the Brenier challenge passed Lean and nanoda checking, that all twelve displayed definition bodies matched, and that its transfer check to the displayed statement passed.

## Related prior literature mentioned by others
- [Cyril Letrouit, *Unstable optimal transport maps*](https://arxiv.org/abs/2510.13265) (arXiv:2510.13265, 15 Oct 2025; published in C. R. Math. 364 (2026)). Han–Zhu (arXiv:2610.09688) identify Conjecture 3 of this note as the square-root conjecture the manuscript disproves; the manuscript cites the Comptes Rendus version.
- [Mohit Bansil and Jun Kitagawa, *Quantitative stability in the geometry of semi-discrete optimal transport*](https://arxiv.org/abs/2002.02022) (arXiv:2002.02022, 2020-02-05; revised 2021-02-10). The Evidence Press follow-up identifies this work on Laguerre-cell stability under changing masses at fixed sites as related background for its extension of the paper's three-atom construction.

## Possibly relevant literature (found by the agent, not checked)
- [Jun Kitagawa, Cyril Letrouit, Quentin Mérigot, *Stability of optimal transport maps on Riemannian manifolds*](https://arxiv.org/abs/2504.05412) (arXiv:2504.05412, 2025). Proves target-uniform quantitative stability for maps and Kantorovich potentials on Riemannian manifolds, with a sharpness-of-exponent example in v2; a comparison point for the manuscript's potential-then-gradient route to the 1/3 exponent and its sharpness claim.
- [Yuanlong Ruan, *Sharp conditioning and quantitative stability of optimal transport*](https://arxiv.org/abs/2610.07577) (arXiv:2610.07577, 2026-10-06). Section 12 derives common-source Brenier-map stability from transport-cost error bounds, including a compact-support W₁ quarter-power estimate for bounded source densities, for comparison with the manuscript's W₂ one-third estimate.

## Digests and expositions
- None found.

## News and blogs
- [ミトKeY (MeatKey), *An "Experiment" on the Impact of OpenAI's "openai/math" on Broad-Sense Research*](https://note.com/mi6242/n/n7753aa269c7e?hl=en) (note.com, 2026-10-12). The post reproduces AI-generated discussion and a draft application combining family 374's transport stability bound with family 140's regression bounds for manufacturing domain adaptation, with experiments described as synthetic. [AI-generated per source] [family-level]
