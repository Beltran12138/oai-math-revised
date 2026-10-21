# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Shisheng Li, Zhong Zhuang, *Coprime pairs with equal sum of divisors, assuming smooth shifted primes*](https://arxiv.org/abs/2610.15674) (arXiv:2610.15674, 2026-10-11). Uses a Pollack–Pomerance argument to reduce Erdős Problem #824 to a smooth-$p+1$ hypothesis, and argues that this paper's method for $p-1$ carries over to $p+1$ after sign changes in two sections; the authors state they have not independently verified the paper's main new estimates.
- [Plasma AI, *The normal order of the number of iterations of Euler’s function*](https://github.com/plasma-ai/erdos-408/blob/main/paper/totient_iterates.pdf) (preprint, Palomar PALOMAR-2026-10-19-000009, 2026-10-19). Derives a normal order for iterated-totient heights (Erdős #408); its graph-transference step reuses this paper's Lemma 3.4, Theorem 3.5, Corollary 3.11, Theorem 4.1 and Lemma 4.3, together with OpenAI's Dirichlet zero-free half-plane. [family-level]
- [Jizhou Guo, *Shifted primes with a prescribed parity of the number of prime factors*](https://github.com/aster2024/openai-math-followups/blob/main/shifted-prime-parity/README.md) (preprint, 2026-10-09). Uses the parity paper’s prime-slot correlations and this paper's sieve estimates to claim a lower bound of $cX/(\log X)^{300}$ for squarefree $p+h$ with either Möbius sign, uniformly for $0<|h|\le(\log X)^5$. [AI-generated per source] [family-level]
- [Jizhou Guo, *Sums of two rough numbers with prescribed Liouville signs*](https://github.com/aster2024/openai-math-followups/blob/main/rough-goldbach-parity/README.md) (preprint, 2026-10-09). Combines adaptations of this paper’s graph estimates with OpenAI’s Dirichlet zero-free half-plane to claim many representations of large even integers as sums of squarefree rough numbers with prescribed Liouville signs. [AI-generated per source]

## Comments and discussion
- [Thomas Bloom, *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog, 2026-10-08). The erdosproblems.com maintainer lists this paper's claim as a resolution of Problem #821, notes the previous best exponent was $0.715\ldots$, and says the proof goes through results on the prime factors of $p-1$.

## Formalization
- [OpenAI, *lean/OAI/NumberTheory/TotientFibers/FiniteFiber.lean*](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/TotientFibers/FiniteFiber.lean) (openai/math, 2026-10-06). The release's own Lean file, proving finiteness of totient fibers and a pigeonhole transfer that assumes a large set of primes with $t$-smooth predecessors; it does not prove the smooth-shifted-prime count (Theorem 1.2).
- [Yao Xu (@cadamcat), *totient-fibers-lean4*](https://github.com/cadamcat/totient-fibers-lean4) (GitHub, v1.0.0, verification recorded 2026-10-14). An independent Lean 4 formalization of Theorems 1.1 (Erdős #821) and 1.2 following the paper's structure, with a statement comparison against Formal Conjectures; per its [verification record](https://github.com/cadamcat/totient-fibers-lean4/blob/main/docs/verification.md), `Erdos821.erdos_821` depends only on `propext`, `Classical.choice` and `Quot.sound`. [AI-generated per source]
- [Yao Xu (@cadamcat), *equal-divisor-sums-lean4*](https://github.com/cadamcat/equal-divisor-sums-lean4) (GitHub, accessed 2026-10-21). A Lean 4 proof of Erdős #824 that combines Li–Zhuang's conditional reduction with a proved supply of smooth shifted primes $p+1$, reusing the sign-free parts of totient-fibers-lean4. [AI-generated per source]
- [Shisheng Li and Zhong Zhuang, *Erdős Problem 824: coprime pairs with equal sum of divisors*](https://github.com/daizisheng/erdos-824) (Lean 4 development, 2026). Formalizes the implication from an explicit smooth-successor hypothesis to the pair-count lower bound, excluding the weighted-dilation argument and the squarefree addendum. [AI-generated per source]
- [google-deepmind/formal-conjectures, *ErdosProblems/824.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/824.lean) (formal-conjectures). The formal statement of Erdős #824, marked solved; it cites this paper and Li–Zhuang and links equal-divisor-sums-lean4 as a formal proof.
- [Plasma AI, *erdos-408* (Lean 4)](https://github.com/plasma-ai/erdos-408) (GitHub, 2026-10-19). Lean development for Erdős #408 whose graph inputs come from a vendored copy of totient-fibers-lean4, i.e. formalized versions of this paper's results. [family-level]

## Related prior literature mentioned by others
- [Kevin Ford, *The distribution of totients*](https://arxiv.org/abs/1104.3264) (arXiv:1104.3264, revised version of Ramanujan J. 2 (1998)). Boris Alexeev cited this paper on the [Erdős #821 forum](https://www.erdosproblems.com/forum/discuss/821) (2025-09-30) for the earlier multiplicity-exponent record $0.7039$, which Thomas Bloom noted Lichtman had since improved.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- None found.

## News and blogs
- [Patrick White with Claude, *Erdős #821: OpenAI totient fibers, refereed*](https://erdosproblemaday.com/day/821-openai-totient-fibers-refereed) (Erdős Problem a Day, 2026-10-11). A machine review by ten AI "seats" that reports no mathematical gap but lists drafting issues (a sketched bijection in Lemma 3.7, an unwritten inequality in §5, a $4\delta<\varepsilon$ versus $3\delta<\varepsilon$ mismatch in §8), and states that no human has verified the paper. [AI-generated per source]
