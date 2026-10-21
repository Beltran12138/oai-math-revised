# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Hexagon deposit contributed by Scott Kominers, *Multi-coverings by lattice translates of convex bodies*](https://hexagonmath.org/abs/2610.00165v1) (hexagon:2610.00165v1, October 2026). This paper is in its bibliography, but its body text cites only the companion single-lattice paper, whose construction it extends to lattice multi-coverings; the source calls the work "heavily LLM-assisted". [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 092: The optimal order of convex-body covering density*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/092.md) (lean/docs/092.md, 2026-10-06). The release's own scope note: the formalization bounds the translative and lattice covering-density suprema, over all convex bodies and over centrally symmetric ones, above and below by absolute multiples of $n\log n$ for large $n$ (comparator file `CoveringDensity.lean`). [family-level]
- [OpenAI, *lean/OAI/Geometry/CoveringDensity/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/CoveringDensity/Main.lean) (openai/math, commit adc7f12). Contains `OAI.CoveringOrder.optimal_order`, the two-sided $\Theta(n\log n)$ statement for the four density suprema, together with `thetaT_le_thetaL`. [family-level]

## Related prior literature mentioned by others
- [H. Li, X. Liu, *Nearly Sharp Bounds for Lattice Coverings by Convex Bodies*](https://arxiv.org/abs/2607.28429) (arXiv:2607.28429, v2 10 August 2026). The VibeMathed entry for this family describes Theorem 1.1 as extending this paper's order-$n\log n$ lower bound from lattice coverings to translative coverings; the paper cites it as the source of its random-slab and Poisson-witness method.
- [Or Ordentlich, Oded Regev and Barak Weiss, *New bounds on the density of lattice coverings*](https://arxiv.org/abs/2006.00340) (arXiv:2006.00340, 2020-05-30). Kalai's October 2026 discussion identifies this earlier work on lattice covering densities as background to the family's two announced results. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- None found.

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 2026-10-07). Item 7, "Covering density of convex bodies", links both papers of this family and describes this one as giving matching examples "even for unrestricted translative coverings", combined with the universal lattice-covering upper bound. [family-level]
