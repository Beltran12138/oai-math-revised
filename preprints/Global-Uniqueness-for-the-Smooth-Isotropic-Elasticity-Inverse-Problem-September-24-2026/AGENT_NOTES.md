# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Huaian Diao, Umidjon Durdiev, *Unique Determination of the Lamé Parameters in Three Dimensions*](https://arxiv.org/abs/2610.14741) (arXiv:2610.14741, 10 Oct 2026). Claims the same full-data global uniqueness theorem (smooth λ, μ, μ > 0 and 3λ+2μ > 0, bounded smooth domain in ℝ³) by a four-component Laplace-type reduction, CGO solutions and Cauchy–Plemelj factorization; its Section 1.2 says the authors later became aware of "the related OpenAI preprint" and describe their work as independent.
- [Huaian Diao, Umidjon Durdiev, *Logarithmic Stability for the Inverse Boundary Problem in Three-Dimensional Isotropic Elasticity*](https://arxiv.org/abs/2610.24053) (arXiv:2610.24053, 16 Oct 2026). Proves logarithmic interior stability and boundary derivative estimates for both Lamé parameters, and states global uniqueness for C^22 parameters, which it says "relaxes the C∞ regularity assumptions in the independent uniqueness results" including the OpenAI preprint.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 372: Global uniqueness in smooth isotropic elasticity*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/372.md) (lean/docs/372.md, 2026-10-06). The release's own Lean scope note: the formalization covers the uniqueness statement (Theorem 1.1) for both smooth real Lamé moduli under the paper's positivity and full displacement-to-traction data assumptions, via the comparator challenge `ElasticityUniqueness.lean`; reconstruction is outside its scope. [family-level]

## Related prior literature mentioned by others
- [Lu Chen, Yan Jiang, Hongyu Liu, Longyue Tao, *On an inverse boundary problem in elastodynamics*](https://arxiv.org/abs/2609.20134) (arXiv:2609.20134v1, 17 Sep 2026). Proves uniqueness for smooth coefficients when μ is axisymmetric, separable on a product domain, or quasianalytic in one direction; both the paper and the Diao–Durdiev follow-ups cite it as the most recent structured-case result before the general theorem.

## Possibly relevant literature (found by the agent, not checked)
- [Oleg Imanuvilov, Gunther Uhlmann, Masahiro Yamamoto, *On reconstruction of Lamé coefficients from partial Cauchy data in three dimensions*](https://arxiv.org/abs/1205.4436) (arXiv:1205.4436, 2012; related DOI 10.1088/0266-5611/28/12/125002). Recovers both Lamé coefficients in dimension ≥ 3 from partial Cauchy data when μ is close to a constant; relevant to the paper's history paragraph on near-constant three-dimensional results, and not in its bibliography.
- [Elena Beretta, Elisa Francini, Sergio Vessella, *Uniqueness and Lipschitz stability for the identification of Lamé parameters from boundary measurements*](https://arxiv.org/abs/1303.2443) (arXiv:1303.2443, 2013). Uniqueness and Lipschitz stability for piecewise constant Lamé parameters in 3D from the Dirichlet-to-Neumann map; a non-smooth special class relevant to the paper's claim of treating "the full smooth class", and not in its bibliography.
- [Elena Beretta, Elisa Francini, Antonino Morassi, Edi Rosset and Sergio Vessella, *Lipschitz continuous dependence of piecewise constant Lamé coefficients from boundary data: the case of non flat interfaces*](https://arxiv.org/abs/1406.1899) (arXiv:1406.1899, 2014-06-07). Establishes Lipschitz stability for piecewise constant Lamé coefficients on a known finite partition with C¹,α interfaces, a comparison point for the paper's recovery of both moduli in the general smooth class.

## Digests and expositions
- None found.

## News and blogs
- [Latent Space AINews, *Quasi-Riemann-Hypothesis: OpenAI publishes 722 math papers …*](https://www.latent.space/p/ainews-quasi-riemann-hypothesis-openai) (newsletter, 7 Oct 2026). Its Twitter recap mentions this paper in one sentence, as "a uniqueness result for the elastic inverse problem, which the paper says had been open in 3D since 1994."
