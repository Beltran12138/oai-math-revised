# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Buhai, Cohen-Addad, Fleischmann, Gupta, Jubés Monforte, Pittu, Stouras, Svensson, Vogl, *A Better-than-2 Approximation for k-Median Part I: The Power of General Bids*](https://arxiv.org/abs/2610.18144) (arXiv:2610.18144, 13 October 2026). An independent randomized polynomial-time 1.95-approximation for k-median; its "AI Acknowledgment and Concurrent Work" paragraph describes the OpenAI result that extends iterative rounding to a $(1+2/e+\varepsilon)$-approximation as concurrent work announced on 6 October 2026. [family-level]
- [Buhai, Cohen-Addad, Fleischmann, Gupta, Jubés Monforte, Pittu, Stouras, Svensson, Vogl, *A Better-than-2 Approximation for k-Median Part II: Stable Instances*](https://arxiv.org/abs/2610.17172) (arXiv:2610.17172, 12 October 2026). The companion paper (a $(1.89+\varepsilon)$-approximation for β-stable instances) calls the iterative-rounding OpenAI paper "an optimal" $(1+2/e+\varepsilon)$-approximation in its concurrent-work discussion. [family-level]

## Comments and discussion
- [Ola Svensson, quoted by Digg, *OpenAI is said to have solved a problem students worked on for over a year*](https://digg.com/ai/5agbrefi) (X post quoted by Digg, 2026-10-07). The quoted post describes OpenAI's k-median result as solving a problem the poster's students had pursued and announces the group's different algorithmic approach. [family-level]
- [Ola Svensson (@AlgoSvensson), post on X](https://x.com/AlgoSvensson/status/2107736070192287922) (2026-10-07). The original post says OpenAI "completely solved a problem on which my students have worked hard for 1+ years" and that the group will upload a different algorithmic approach. [family-level]
- [Ola Svensson (@AlgoSvensson), post on X](https://x.com/AlgoSvensson/status/2107739490349420894) (2026-10-07). The post says the tight k-median approximation implies a tight result for facility location, an optimal opening-cost versus connection-cost tradeoff, a "pretty well-known connection but not stated in the OpenAI paper".

## Formalization
- [OpenAI math release, *Lean scope notes for family 125*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/125.md) (lean/docs/125.md, 2026). The release's Lean scope note covers the deterministic polynomial-time $1+2/e+\varepsilon$ approximation on finite rational metrics with specified candidate facilities and, assuming $P\ne NP$, the exact infimum threshold $1+2/e$; comparator files are MetricKMedian.lean and KMedianThreshold.lean. [family-level]

## Related prior literature mentioned by others
- [Jarosław Byrka, Yuhao Guo, Yang Hu, Shi Li, Chengzhang Wan and Zaixuan Wang, *k-Clustering via Iterative Randomized Rounding*](https://arxiv.org/abs/2604.06046) (arXiv:2604.06046, 2026-04-07). Both Buhai et al. papers describe the threshold paper as extending this iterative-rounding $2+\varepsilon$ approach; the paper itself cites it as the framework it builds on.

## Possibly relevant literature (found by the agent, not checked)
- [Cohen-Addad, Gupta, Kumar, Lee, Li, *Tight FPT Approximations for k-Median and k-Means*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.42) (ICALP 2019, LIPIcs 132, 42:1–42:14). Gives a $(1+2/e+\varepsilon)$ factor for k-median in FPT time, the same factor that Theorem 1.1 claims in polynomial time; the paper's bibliography does not cite it, although the companion paper does.

## Digests and expositions
- None found.

## News and blogs
- [Post-Cutoff, *OpenAI model claims tight 1 + 2/e approximation for k-median*](https://postcutoff.com/e/2026-10-06-openai-k-median-optimal-approximation-1-plus-2-over-e/) (2026-10-15). This article summarizes both manuscripts, the release's Lean comparator statements, and the concurrent work of Buhai et al. [AI-generated per source] [family-level]
