# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Buhai, Cohen-Addad, Fleischmann, Gupta, Jubés Monforte, Pittu, Stouras, Svensson, Vogl, *A Better-than-2 Approximation for k-Median Part II: Stable Instances*](https://arxiv.org/abs/2610.17172) (arXiv:2610.17172, 12 October 2026). An independent $(1.89+\varepsilon)$-approximation for β-stable instances; its concurrent-work discussion says the OpenAI stable-instance paper shares "many similarities" with it and achieves $(1+2/e+\varepsilon)$ on stable instances but only $(2-\sigma)$ in general. [family-level]
- [Buhai, Cohen-Addad, Fleischmann, Gupta, Jubés Monforte, Pittu, Stouras, Svensson, Vogl, *A Better-than-2 Approximation for k-Median Part I: The Power of General Bids*](https://arxiv.org/abs/2610.18144) (arXiv:2610.18144, 13 October 2026). An independent randomized polynomial-time 1.95-approximation for k-median; it describes the OpenAI $(2-\sigma)$ result as building on the stable-instance and pseudo-approximation framework, much like its own approach. [family-level]

## Expert comments and discussion
- [Ola Svensson, quoted by Digg, *OpenAI is said to have solved a problem students worked on for over a year*](https://digg.com/ai/5agbrefi) (X post quoted by Digg, 2026-10-07). The quoted post describes OpenAI's k-median result as solving a problem the poster's students had pursued and announces the group's different algorithmic approach. [family-level]

## Formalization
- [OpenAI math release, *Lean scope notes for family 125*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/125.md) (lean/docs/125.md, 2026). The release's Lean scope note covers the exact-budget refined recovery theorem (under the bounded-integral-metric and accurate-proxy hypotheses) and the randomized $(2-\sigma)$ approximation on finite rational metrics; comparator files are KMedianRefinedRecovery.lean and KMedianRecovery.lean. [family-level]

## Related prior literature mentioned by others
- [Vincent Cohen-Addad, Fabrizio Grandoni, Euiwoong Lee, Chris Schwiegelshohn and Ola Svensson, *A $(2+\varepsilon)$-Approximation Algorithm for Metric k-Median*](https://arxiv.org/abs/2503.10972v2) (arXiv:2503.10972v2, 2026-05-19). Buhai et al.'s concurrent-work discussion identifies this paper's stable-instance/pseudo-approximation framework as the shared basis of the OpenAI recovery paper and their own approach.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- None found.

## News and blogs
- [Post-Cutoff, *OpenAI model claims tight 1 + 2/e approximation for k-median*](https://postcutoff.com/e/2026-10-06-openai-k-median-optimal-approximation-1-plus-2-over-e/) (2026-10-15). This article summarizes both manuscripts, the release's Lean comparator statements, and the concurrent work of Buhai et al. [AI-generated per source] [family-level]
