# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 139: Subpolynomial query complexity for log-concave sampling*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/139.md) (lean/docs/139.md, 2026-10-06). The release's scope note states that the formalization covers the upper bound $C_\varepsilon d^\varepsilon$, the eventual lower bound $c\log d$, and $\gamma_*=0$ for randomized adaptive measurable algorithms using exact value-and-gradient queries at total-variation error 1/10. The comparator statement is in `LogConcaveQuery.lean`. [family-level]
- [OpenAI, *OAI/Probability/LogConcave/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Probability/LogConcave/Main.lean) (openai/math repository, October 2026). This is the release's top-level Lean module for this paper. It contains `source_subpolynomial_upper`, `source_gammaStar_zero` and `exact_source_main`, the last combining the upper bound, the logarithmic lower bound and $\gamma_*=0$.
- [DakeBU, *Protocol: assimilate OpenAI Math into Samplinglib* (PR #314)](https://github.com/DakeBU/Automization-Sampling-Optimisation-Geometry-Lib/pull/314) (GitHub pull request, merged 2026-10-07). This independent Lean library pins the 2026-10-06 release snapshot and treats `OAI/Probability/LogConcave` as a full proof graph, separating reusable leaves from the "source-specific subpolynomial query-complexity route". No theorem has been ported yet.

## Related prior literature mentioned by others
- [Sinho Chewi, *Log-Concave Sampling* (book draft)](https://chewisinho.github.io/main.pdf) (version of 2026-08-20). VibeMathed cites this book as the source of the question the paper answers. In Section 9.4 the book notes that Gaussian lower bounds are only logarithmic in $d$, "whereas all of the upper bounds for general log-concave sampling thus far incur polynomial dimension dependence".

## Possibly relevant literature (found by the agent, not checked)
- [Chewi, Gerber, Lu, Le Gouic, Rigollet, *The query complexity of sampling from strongly log-concave distributions in one dimension*](https://arxiv.org/abs/2105.14163) (arXiv:2105.14163, 2021). This earlier work in the same first-order query model determines the $d=1$ complexity as a function of the condition number. It may give context for the paper's fixed-conditioning lower bound (Theorem 1.1, lower part).
- [Altschuler, Chewi, *Faster high-accuracy log-concave sampling via algorithmic warm starts*](https://arxiv.org/abs/2302.10249) (arXiv:2302.10249, 2023). This is an earlier polynomial-in-$d$ query bound ($\widetilde O(d^{1/2})$ for high accuracy) for strongly log-concave, log-smooth targets. It is relevant to the historical comparison of dimension exponents in Section 1.2.
- [Braverman, Hazan, Simchowitz, Woodworth, *The gradient complexity of linear regression*](https://arxiv.org/abs/1911.02212) (arXiv:1911.02212, 2019). This is the source of the Wishart-conditioning technique for matrix-vector query lower bounds, which Chewi's book credits in its Gaussian sampling lower bounds. It may be relevant to the rotational-invariance and block-Krylov reduction behind the paper's $c\log d$ lower bound.

## Digests and expositions
- [Latent Seminar, *Subpolynomial queries for log-concave sampling*](https://lowrank.github.io/latent-seminar/OpenAI-Math/139-log-concave-sampling-queries) (2026-10-07). This exposition explains the oracle model, Gaussian conditioning, recursive noisy-mean implementation, noise removal, and Gaussian lower-bound strategy, and states that it has not independently verified the complete proofs. [family-level]

## News and blogs
- None found.
