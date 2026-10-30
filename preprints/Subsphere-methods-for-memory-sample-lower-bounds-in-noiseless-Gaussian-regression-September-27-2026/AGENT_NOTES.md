# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [GitHub user acprk (author name not given), *The leading constant of the memory–sample tradeoff for noiseless Gaussian regression*](https://github.com/acprk/memory-sample-leading-constant) (GitHub note, v0.1.0, 2026-10-10). Claims the constant $2^{-16}$ of this paper can be replaced by any $c < 2\ln 2$ for $o(d^2)$ memory, matched by finite-bit randomized Kaczmarz, conditional on the upstream proof; it takes its architecture and unchanged lemmas from this paper. [AI-generated per source]
- [Zeyu Wu, Zihao Wang, Minghua Deng, *The Cost of Working Memory in Streaming Mean Estimation*](https://arxiv.org/abs/2610.39540) (arXiv:2610.39540, stat.ML, 2026-10-29). Mentions this paper in its related work (Section 1.1) as a finite-memory sample lower bound for exact linear equations, contrasted with its own noisy Gaussian location model, and uses no result from it.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Memory–sample lower bounds for noiseless Gaussian regression: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/140.md) (oai-math-revised mirror of openai/math, 2026-10). Describes the Lean formalization across the six papers, with eight comparator files (e.g. NoiselessRegression.lean, SubsphereCurrent.lean); for this paper it reports the explicit $2^{-16} d \log_2(1/\epsilon)$ bound at success 2/3 and a same-order bound at success 1/2. [family-level]
- [MathVet, *Family 140 statement-fidelity audit*](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv) (GitHub audit, accessed 2026-10-30). Classifies the family’s formal statements as covering its headline and identifies custom learner and measurability definitions for scrutiny. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [V. Sharan, A. Sidford and G. Valiant, *Memory-Sample Tradeoffs for Linear Regression with Small Error*](https://arxiv.org/abs/1904.08544) (arXiv:1904.08544, STOC 2019). Identified by VibeMathed as the noisy-regression precursor to the family's precision question. [family-level]
- [Marsden, Sharan, Sidford, Valiant, *Efficient Convex Optimization Requires Superlinear Memory*](https://arxiv.org/abs/2203.15260) (arXiv:2203.15260, 2022; COLT 2022). Cited by the acprk leading-constant note as related memory lower-bound work for first-order convex optimization.
- [Blanchard, Zhang, Jaillet, *Quadratic Memory is Necessary for Optimal Query Complexity in Convex Optimization: Center-of-Mass is Pareto-Optimal*](https://arxiv.org/abs/2302.04963) (arXiv:2302.04963, 2023; COLT 2023). Cited by the acprk leading-constant note as related work on quadratic-memory thresholds.

## Possibly relevant literature (found by the agent, not checked)
- [Brown, Bun, Smith, *Strong Memory Lower Bounds for Learning Natural Models*](https://arxiv.org/abs/2206.04743) (arXiv:2206.04743, COLT 2022). One-pass memory lower bounds for natural learning problems, whose abstract notes earlier linear-regression bounds covered only narrow sample-size ranges; relevant to the claim that the bound holds uniformly in accuracy.

## Digests and expositions
- [Latent Seminar, *Memory and samples in noiseless Gaussian regression*](https://lowrank.github.io/latent-seminar/OpenAI-Math/140-noiseless-regression-memory) (Latent Seminar, 2026-10-07). Explains residual subspheres and the two-dimension cost per block, without claiming independent verification of the complete proofs. [family-level]

## News and blogs
- [ミトKeY(MeatKey), *OpenAIの"openai/math"の広い意味での研究へのインパクトについての「ある実験」*](https://note.com/mi6242/n/n7753aa269c7e) (note.com, 2026-10-12). Presents an AI-generated application experiment using family 140 for sensor calibration and discusses proposed finite-bit Kaczmarz and manufacturing-transfer extensions. [AI-generated per source] [family-level]
