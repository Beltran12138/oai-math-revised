# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [GitHub user acprk (author name not given), *The leading constant of the memory–sample tradeoff for noiseless Gaussian regression*](https://github.com/acprk/memory-sample-leading-constant) (GitHub note, v0.1.0, 2026-10-10). Claims the constant $2^{-16}$ of the subsphere paper can be replaced by any $c < 2\ln 2$ for $o(d^2)$ memory, matched by finite-bit randomized Kaczmarz, conditional on the upstream proof; it cites this paper for the order of the sample complexity. [AI-generated per source]
- [Draft posted by ミトKeY(MeatKey), *Edge Transfer of Fault-Diagnosis Models Based on the Stability of Optimal Transport Maps*](https://note.com/api/v2/attachments/download/1111109722a2884f64386fff14228b16) (public revised draft with placeholder author names, posted 2026-10-12). Section 3.2 cites this paper and proposes a quantized Kaczmarz calibration bound within a synthetic fault-diagnosis transfer experiment. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Memory–sample lower bounds for noiseless Gaussian regression: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/140.md) (oai-math-revised mirror of openai/math, 2026-10). Describes the Lean formalization across the six papers, with eight comparator files (e.g. NoiselessRegression.lean, SubsphereCurrent.lean); for this paper it reports fixed-quadratic-memory and subquadratic-memory precision bounds, with inverse-Gram and exact-projection supporting estimates. [family-level]

## Related prior literature mentioned by others
- [V. Sharan, A. Sidford and G. Valiant, *Memory-Sample Tradeoffs for Linear Regression with Small Error*](https://arxiv.org/abs/1904.08544) (arXiv:1904.08544, STOC 2019). Identified by VibeMathed as the noisy-regression precursor to the family's precision question. [family-level]
- [Marsden, Sharan, Sidford, Valiant, *Efficient Convex Optimization Requires Superlinear Memory*](https://arxiv.org/abs/2203.15260) (arXiv:2203.15260, 2022; COLT 2022). Cited by the acprk leading-constant note as related memory lower-bound work for first-order convex optimization.
- [Blanchard, Zhang, Jaillet, *Quadratic Memory is Necessary for Optimal Query Complexity in Convex Optimization: Center-of-Mass is Pareto-Optimal*](https://arxiv.org/abs/2302.04963) (arXiv:2302.04963, 2023; COLT 2023). Cited by the acprk leading-constant note as related work on quadratic-memory thresholds.

## Possibly relevant literature (found by the agent, not checked)
- [Brown, Bun, Smith, *Strong Memory Lower Bounds for Learning Natural Models*](https://arxiv.org/abs/2206.04743) (arXiv:2206.04743, COLT 2022). One-pass memory lower bounds for natural learning problems, whose abstract notes earlier linear-regression bounds covered only narrow sample-size ranges; relevant to the claim that the bound holds uniformly in accuracy.
- [Menart, Nikolov, Shamir, *Stronger Memory-Query Tradeoffs for Convex Optimization: The Limitations of Subquadratic Memory*](https://arxiv.org/abs/2607.24827) (arXiv:2607.24827, 2026-07-21). Reports a sharp change in query complexity near memory $m \approx d^2$ for convex optimization, a related phenomenon to the $Ad^2$ memory threshold in the main theorem.
- [Berg, Ordentlich, Shayevitz, *Statistical Inference with Limited Memory: A Survey*](https://arxiv.org/abs/2312.15225) (arXiv:2312.15225, 2023, rev. 2024; JSAIT). Survey of memory-constrained estimation and lower-bound techniques, background for the finite-state learner model used here.

## Digests and expositions
- [Latent Seminar, *Memory and samples in noiseless Gaussian regression*](https://lowrank.github.io/latent-seminar/OpenAI-Math/140-noiseless-regression-memory) (Latent Seminar, 2026-10-07). Explains the backward successful-mass invariant and block selection cost, and states that the complete proofs were not independently verified. [family-level]
- [Perplexity / Orply, *Bounded Memory Forces Logarithmically More Samples for Precise Gaussian Regression*](https://orply.com/articles/perplexity/140-1-memory-and-precision-in-noiseless-gaussian-regression-11957e33) (Orply, 2026-10-11). An AI-assisted exposition of this paper's finite-state model, backward mass invariant, projection argument, and reflection endpoint. [AI-generated per source]

## News and blogs
- [ミトKeY(MeatKey), *OpenAIの"openai/math"の広い意味での研究へのインパクトについての「ある実験」*](https://note.com/mi6242/n/n7753aa269c7e) (note.com, 2026-10-12). Presents an AI-generated application experiment using family 140 for sensor calibration and discusses proposed finite-bit Kaczmarz and manufacturing-transfer extensions. [AI-generated per source] [family-level]
