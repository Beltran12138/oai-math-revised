# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [bramble_trace, *Structured cubic and sextic means for angular Gauss coefficients*](https://rstation.ai/problems/riemann_hypothesis/papers/5) (rStation, v3, 17 October 2026). This work on coefficient-specific angular mean-square estimates cites the manuscript as reference [5] and explicitly distinguishes its prime first moment and angular cancellation scale from the estimates developed there. [AI-generated per source]
- [bramble_trace, *Natural cubic Möbius–Gauss means above the square-root range*](https://rstation.ai/problems/riemann_hypothesis/papers/70) (rStation, v1, 28 October 2026). Posted on the same site, this work lists the manuscript's Lemmas 2.2–2.3 and Section 5 among its references, and its reviewer report says the manuscript does not already give the work's arbitrary-vector reconstruction and inverse-product conclusion.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Patterson's first moment for cubic Gauss sums* (Lean scope note 023)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/023.md) (lean/docs/023.md, release of 2026-10-06). The release's own scope note says the Lean development proves the sharp-cutoff asymptotic with main term $\frac65c_*X^{5/6}/\log X$, the angular comparison for every integer mode, and $o(X^{5/6}/\log X)$ cancellation for each fixed nonzero mode; the comparator statement is `PattersonFirstMoment.lean`. [family-level]

## Related prior literature mentioned by others
- [Alexander Dunn and Maksym Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*](https://arxiv.org/abs/2109.07463) (Annals of Mathematics 200, 2024; arXiv:2109.07463v3, 14 May 2024). The AI Proved What? exposition and Evidence Press commentary identify this GRH-conditional predecessor, whose level-aspect Voronoi formula and corrected dispersion provide context for the manuscript's claimed unconditional result.

## Possibly relevant literature (found by the agent, not checked)
- [A. Dunn, *Metaplectic cusp forms and the large sieve*](https://arxiv.org/abs/2403.13151) (arXiv:2403.13151; Algebra & Number Theory 19 (2025)). Proves Type I/II estimates over primes for Fourier coefficients of a cubic metaplectic cusp form via Voronoi summation and Heath-Brown's cubic large sieve, bearing on the paper's prime-sum Type I/bilinear strategy and its remark that it does not improve the cubic large sieve.
- [Alexandre de Faveri, *Optimal large sieve for fixed order characters*](https://arxiv.org/abs/2610.04045) (arXiv:2610.04045, 2 October 2026). Its improved large-sieve inequalities for fixed-order Hecke characters may be relevant to the manuscript's use of cubic large-sieve bounds in its structured moment and dispersion estimates.
- [Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein, *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*](https://arxiv.org/abs/2607.07911) (arXiv:2607.07911v2, 13 July 2026). Its unconditional non-orthogonality results arising from Gauss-sum bias provide a comparison for the manuscript's distinction between cancellation for structured prime coefficients and bounds for arbitrary coefficients.
- [C. David, A. Dunn, A. Hamieh and H. Lin, *Quartic Gauss sums over primes and metaplectic theta functions*](https://arxiv.org/abs/2306.11875) (arXiv:2306.11875, v5 2026-01-30). Gives the quartic analogue (Type I and Type II estimates over $\mathbb{Q}(i)$, conjectured moment asymptotics); relevant for whether the paper's unconditional cubic argument has a quartic counterpart.
- [Z. Y. Ma, *Optimal homological vanishing: cancellation of character sums and Patterson's conjecture over $\mathbb{F}_q[t]$*](https://arxiv.org/abs/2606.26440) (arXiv:2606.26440, 2026-06-24). Bounds the bias of higher-order Gauss sums over function fields, a function-field analogue of the Patterson conjecture that the paper proves over $\mathbb{Q}(\omega)$.

## Digests and expositions
- [Latent Seminar, *The first moment of cubic Gauss sums*](https://lowrank.github.io/latent-seminar/OpenAI-Math/023-cubic-gauss-first-moment) (6 October 2026). This exposition explains the factor of two between primary-prime and rational-prime normalizations, corrected dispersion, the stopping-bin decomposition, and the fixed-mode scope, while explicitly disclaiming independent verification of the complete proof. [family-level]
- [AI Proved What?, *Still biased? Patterson's first moment for cubic Gauss sums*](https://aiprovedwhat.com/episodes/023-pattersons-first-moment-cubic-gauss/) (episode 023, October 2026; status checked 19 October 2026). This AI-assisted video and accompanying explanation illustrate the bias numerically, describe the normalization and fixed-power limitations, and distinguish OpenAI's reported Lean coverage from checks performed by the site. [AI-generated per source] [family-level]
- [Gradient Damage, *Patterson's Conjecture on Cubic Gauss Sums: OpenAI Claims a Proof*](https://gradientdamage.com/videos/pattersons-conjecture-on-cubic-gauss-sums-openai-claims-a-proof/) (16 October 2026). This short animation illustrates the manuscript's claimed first-moment bias with finite Gauss-sum computations and explicitly presents the animation as illustration rather than proof. [family-level]
- [Bogdan Grechuk, *Kummer’s Bias in Cubic Gauss Sums*](https://functor.network/user/3333/entry/2021) (Functor Network, 20 October 2026). Explains how the manuscript’s claimed positive first moment coexists with equidistribution, distinguishes average bias from an excess of positive terms, and contrasts the claim with Dunn–Radziwiłł’s GRH-conditional smoothed asymptotic while noting that independent verification is pending.

## News and blogs
- [Evidence Press, *How did a language model prove a quasi-Riemann hypothesis?*](https://evidencepress.org/articles/how-a-language-model-proved-quasi-riemann/) (10 October 2026). The article discusses the cubic first-moment manuscript as a possible precursor to OpenAI's quasi-Riemann work, explicitly identifying this discovery-path connection as an inference and noting that the later theorem does not use the first-moment result.
