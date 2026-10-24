# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [erdosproblems.com forum (T. Bloom, M. Firsching and others), *Erdős Problem #978 discussion thread*](https://www.erdosproblems.com/forum/thread/978) (forum, Sep 2025 – Mar 2026). This thread predates the paper and does not comment on it, but discusses the hypotheses of the question that Theorem 1.1 addresses: Firsching reports a degree-6 counterexample with fixed divisor $2^4$, and the problem statement was then amended to exclude fixed prime-power divisors.

## Formalization
- [OpenAI / mathcommunity, *Lean scope notes for family 020: Squarefree quartics and power-free polynomial values*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/020.md) (lean/docs/020.md). The release's scope note: the $(d-2)$-free Euler-product density for every irreducible $f\in\mathbb Z[x]$ of degree $d\ge4$ with no fixed prime $(d-2)$th-power divisor, with no monicity, primitivity or height restriction. [family-level]
- [OpenAI, *lean/OAI/NumberTheory/PowerFree/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PowerFree/Main.lean) (openai/math, commit adc7f12). Contains the theorems `density` ($4\le d\le8$), `allDegrees` ($d\ge4$) and the quartic dyadic tail bound `quartic_dyadic_tail` (saving $N^{-3/1000}$). [family-level]
- [OpenAI, *lean/ComparatorChallenges/PowerFreeValues.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PowerFreeValues.lean) (openai/math, commit adc7f12). The comparator statement of `allDegrees`, defining `PowerFree`, `rho`, `LocallyAdmissible`, `densityConstant` and `DensityStatement`. [family-level]
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/978.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/978.lean#L30) (formal-conjectures). Formalizes the statement of Erdős Problem #978, whose parts (ii) and (iii) cite this paper as [OAI26a] and link the openai/math Lean proof; the file itself contains only `sorry` placeholders. [family-level]

## Related prior literature mentioned by others
- [S. R. Zapata Ceballos, F. Jalalvand, *On the Squarefree Values of Degree-2q Polynomials*](https://arxiv.org/abs/2608.10335) (arXiv:2608.10335, v1 11 Aug 2026; v2 15 Oct 2026). The paper's introduction cites v1 as a claim that includes $n^4+1$; the authors withdrew it in v2 with the comment "The proof of Proposition 2.3 is incomplete". [cites earlier version]
- [Theodor Estermann, *Einige Sätze über quadratfreie Zahlen* (reference in Bogdan Grechuk's exposition)](https://functor.network/user/3333/entry/2011) (Mathematische Annalen 105, 653–662, 1931). Grechuk cites this work on the quadratic case as historical context for the paper's quartic squarefree-value theorem.

## Possibly relevant literature (found by the agent, not checked)
- [B. Poonen, *Squarefree values of multivariable polynomials*](https://arxiv.org/abs/math/0203292) (Duke Math. J. 118 (2003), 353–373). Extends the $abc$-conditional squarefree density, which the introduction attributes to Granville for univariate polynomials, to multivariable polynomials.
- [T. D. Browning, A. Gorodnik, *Power-free values of polynomials on symmetric varieties*](https://arxiv.org/abs/1606.06342) (arXiv:1606.06342, 2016/2017). An asymptotic count of $r$-free polynomial values at integral points of symmetric varieties, a broader setting for the paper's power-free density problem.

## Digests and expositions
- [Bogdan Grechuk, *Square-free values of quartic polynomials*](https://functor.network/user/3333/entry/2011) (Functor Network, 2026-10-14). Explains the local density factors, the quartic examples, the large-prime obstacle and determinant-method strategy, and the higher-degree consequence via Browning's theorem.

## News and blogs
- None found.
