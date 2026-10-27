# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-27.

## Follow-up works
- [Faruk Temur, *The square function estimate for the cone in four dimensions*](https://arxiv.org/abs/2610.12681) (arXiv:2610.12681, 2026-10-08). Proves an $L^3$ reverse square function estimate for the light cone in four dimensions, with consequences for spheres and elliptic paraboloids in three dimensions, taking as stated external inputs this paper's Theorem 1.1, Definitions 8.1–8.2, Lemma 8.4, Theorem 9.1 (round-cone propagation) and equation (10.22); it says it "does not supply an independent proof of those statements".

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 079*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/079.md) (lean/docs/079.md). The release's scope note for both papers says the Lean development covers half-wave local smoothing for all $n\ge2$ and $2\le p<\infty$ with $\varepsilon$-loss, including the critical $L^3$ estimate in dimension three, together with strict-range Fourier-analytic and Kakeya consequences, with comparator links to `LocalSmoothing.lean`. [family-level]

## Related prior literature mentioned by others
- [Francesco Di Plinio and Ioannis Parissis, *Maximal subspace averages*](https://arxiv.org/abs/2107.02109) (Advances in Mathematics 410, 108749, 2022; arXiv:2107.02109). Temur's follow-up combines the codimension-one plate maximal estimate in Theorem C with this paper's scalar local-smoothing estimate to obtain a spacetime averaging bound used in the square-function argument.
- [Zipeng Wang, *$L^p$-boundedness of the Bochner-Riesz operator*](https://arxiv.org/abs/2501.12742) (arXiv:2501.12742, v1 2025-01-22, v6 2026-06-09). The VibeMathed entry for the companion Bochner–Riesz family (078) names this as a proposed all-dimensional proof; it bears on this paper's Bochner–Riesz Corollary (Section 10), which covers the same strict three-dimensional range.

## Possibly relevant literature (found by the agent, not checked)
- [Hong Wang and Shukun Wu, *Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities*](https://arxiv.org/abs/2411.08871) (arXiv:2411.08871, 2024). Proves restriction in $\mathbb R^3$ for $p>22/7$, the prior state of the art for the spherical extension estimate $3<r<\infty$ that Section 10.1 derives from the Bochner–Riesz corollary.
- [Xiangyu Wang, *Wave Packet Density in Local Smoothing: Refinements and Limitations*](https://arxiv.org/abs/2609.34675) (arXiv:2609.34675, v1 2026-09-28, v4 2026-10-16). Refines the Gan–He–Li–Wu broad-incidence argument, which the introduction cites as the previous best result at $p=3$, and discusses geometric limits of wave-packet density methods in the Euclidean setting.

## Digests and expositions
- [AI Proved What?, *Local smoothing in every dimension? OpenAI's wave equation claim*](https://aiprovedwhat.com/episodes/079-local-smoothing-every-dimension/) (Episode 079, 2026-10-26). Mainly about the October all-dimensional paper, but also discusses this three-dimensional preprint as its companion and notes that the newer paper does not cite it; it says no expert review has been named. The site's earlier episode on the three-dimensional paper now redirects to this page. [AI-generated per source] [family-level]
- [Closed Form, *Local smoothing for the Euclidean wave equation*](https://closedform.nishachay.tech/e/openai-math-2026-079/) (Closed Form, accessed 2026-10-27). Explains the fixed-time versus time-averaged Sobolev thresholds with numerical examples, distinguishes the September three-dimensional and October all-dimensional claims, and summarizes their consequences and listed formalization scope. [AI-generated per source] [family-level]

## News and blogs
- None found.
