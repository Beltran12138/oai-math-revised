# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [Terence Tao, *Erdős Problem #968 forum thread*](https://www.erdosproblems.com/forum/thread/968) (erdosproblems.com, comments of 8 and 10 Sep 2025). These comments predate the paper: they sketch a positive answer to the question in Corollary 1.2, conditional on RH and a weak pair-correlation hypothesis (via Heath-Brown), and call this "close to the limit of current technology".

## Formalization
- [OpenAI math release, *Lean scope notes for family 026*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/026.md) (lean/docs/026.md). The release's scope note describes the formalized result as the prime-ratio corollary (positive lower density of indices with $p_n/n<p_{n+1}/(n+1)$) and links the comparator statement `ComparatorChallenges/PrimeGaps.lean`.
- [OpenAI, *lean/OAI/NumberTheory/PrimeGaps/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PrimeGaps/Main.lean) (openai/math, commit adc7f12). This file states `theorem main`, a Lean version of Theorem 1.1 (for every $C>0$ there are $c>0$, $N_0$ with $c N\le$ #large-gap indices up to $N$), proved from a formalized Bombieri–Vinogradov theorem; the directory contains about 57 supporting files.
- [OpenAI, *lean/OAI/NumberTheory/PrimeGaps/RatioCorollary.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PrimeGaps/RatioCorollary.lean) (openai/math, commit adc7f12). This file proves the ratio-increase density statement (Corollary 1.2) and the conjunction `large_gaps_and_ratio_density`, using `LargePrimeGaps.main`.
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/968.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/968.lean) (formal-conjectures). This file is an independent Lean statement of Erdős Problem 968 as `0 < {n | u n < u (n+1)}.lowerDensity`; it is marked solved, with a docstring that credits the OpenAI preprint and links the OpenAI Lean proof, while the file itself keeps `sorry`.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures PR #6898, merged 11 Oct 2026). This PR changes the status of Erdős 968, among other problems, to solved on the basis of the OpenAI release; the review thread does not discuss 968.

## Related prior literature mentioned by others
- [D. R. Heath-Brown, *Gaps between primes, and the pair correlation of zeros of the zeta-function*](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/41/1/103404/gaps-between-primes-and-the-pair-correlation-of-zeros-of-the-zeta-function) (Acta Arith. 41 (1982), 85–99). Tao's 2025 erdosproblems comment uses an estimate from this paper for the conditional (RH plus pair correlation) answer to the question that Corollary 1.2 settles unconditionally; it is not in the paper's bibliography.
- [Danilo Bazzanella, Alessandro Languasco and Alessandro Zaccagnini, *Prime numbers in logarithmic intervals*](https://arxiv.org/abs/0809.2967) (arXiv:0809.2967, 2008; Transactions of the American Mathematical Society 362, 2010). The AI Proved What? exposition identifies this work, also cited in the manuscript, as the earlier unconditional positive-proportion result for thresholds below approximately 0.58 times the logarithmic gap scale.
- [mo271, *fix(ErdosProblems/968): the increasing and decreasing triple variants are true*](https://github.com/google-deepmind/formal-conjectures/pull/6752) (formal-conjectures PR #6752, 30 Sep 2026). This PR settles Erdős's follow-up questions about increasing and decreasing triples of $p_n/n$ by citing Ford–Maynard–Tao, "Chains of large gaps between primes" (arXiv:1511.04468), and Maynard (2015); the paper does not cover these variants.

## Possibly relevant literature (found by the agent, not checked)
- [D. A. Goldston, J. Pintz, C. Y. Yıldırım, *Positive Proportion of Small Gaps Between Consecutive Primes*](https://arxiv.org/abs/1103.3986) (arXiv:1103.3986, 2011). This paper proves the small-gap counterpart of Theorem 1.1: a positive proportion of consecutive gaps are below $\eta\log p_n$, counted with equal weight on prime indices. It is not in the bibliography.
- [W. D. Banks, T. Freiberg, J. Maynard, *On limit points of the sequence of normalized prime gaps*](https://arxiv.org/abs/1404.5094) (arXiv:1404.5094, Proc. LMS 2016). This paper studies the values taken by $d_n/\log p_n$ (its limit points) with Maynard-sieve methods, which bears on Theorem 1.1's count of gaps with $d_n/\log p_n>C$. It is not in the bibliography.

## Digests and expositions
- [AI Proved What?, *Long gaps, how often?*](https://aiprovedwhat.com/episodes/026-positive-lower-density-large-prime/) (Episode 026, October 2026). This video and transcript explain the claimed gap-frequency theorem, its prime-ratio consequence, and the adjacent-interval counting argument, with scripts and animations described as AI-assisted in the site's [production notes](https://aiprovedwhat.com/about/). [AI-generated per source] [family-level]

## News and blogs
- [Thomas Bloom, *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog, 8 Oct 2026). The entry on Problem 968 summarizes the claimed answer, says the argument uses Goldston–Pintz–Yıldırım and Maynard–Tao sieve tools, and states that "This proof has been formalised."
- [OfficeChai Team, *OpenAI Has Also Included Proofs For 23 Erdos Problems In Its Latest Math Proof Drop*](https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/) (OfficeChai, 9 Oct 2026). The article mentions Problem 968 only as one item, under prime gaps, in its list of Erdős problems in the release.
