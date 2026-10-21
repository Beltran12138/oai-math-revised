# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Thomas Bloom (erdosproblems.com forum), *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (blog post, 8 October 2026). The post lists Problem 172 as a claimed proof of Hindman's conjecture, notes Alweiss's earlier proof over the rationals, and describes the 70-page PDF as one that "has not been formalised".

## Formalization
- [Yao Xu (cadamcat), *hindman-sums-products-lean4*](https://github.com/cadamcat/hindman-sums-products-lean4) (GitHub, v1.0.0, 2026). An AI-assisted Lean 4/Mathlib formalization of the finite sums-and-products statement of this paper, building on OpenAI's `openai/math` library and omitting the separation clause of Theorem 1.1 and Corollary 1.2; its [verification notes](https://raw.githubusercontent.com/cadamcat/hindman-sums-products-lean4/main/docs/verification.md) report kernel, Comparator and nanoda checks with only the standard axioms `propext`, `Classical.choice` and `Quot.sound`.
- [google-deepmind/formal-conjectures, *FormalConjectures/ErdosProblems/172.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/172.lean) (Formal Conjectures). This file contains the formal statement of Erdős Problem 172, now marked `research solved` with a reference to this preprint and a `formal_proof` link to the repository above.
- [cadamcat, *feat(ErdosProblems/172): mark solved and link the formal proof*](https://github.com/google-deepmind/formal-conjectures/pull/7127) (formal-conjectures PR #7127, merged 11 October 2026). This pull request changed `erdos_172` from open to solved with answer `True`, linking the external Lean proof of this paper's main theorem and adding this preprint to the references.

## Related prior literature mentioned by others
- [erdosproblems.com, *Problem #172*](https://www.erdosproblems.com/172) (page last edited 16 October 2026). The page records the question under Erdős and Erdős–Graham references (Er77c, ErGr79, ErGr80) not in the paper's bibliography, links the two-colour infinite variant as Problem 1198, and says a positive answer "is claimed" via this preprint.
- [Noah Kravitz, Borys Kuca and James Leng, *Quantitative concatenation for polynomial box norms*](https://arxiv.org/abs/2407.08636) (arXiv:2407.08636, 2024; revised 2026-01-21). Xu's mathematical guide identifies §6 as the source of the subgroup box-norm concatenation theorem used in the formalization in place of the manuscript's Tao–Ziegler concatenation input.

## Possibly relevant literature (found by the agent, not checked)
- [Conner Griffin, *Infinite Sum-Product Configurations in Parallel*](https://arxiv.org/abs/2605.24751) (arXiv:2605.24751, 2026-05-23; revised 2026-09-19). Related to the introduction's distinction between finite and infinite configurations, this paper obtains an infinite sequence with monochromatic finite sums and infinitely many monochromatic products of fixed length, possibly in a different colour.
- [F. K. Richter and K. Tsinas, *Density regularity of {x, x+y, xy} in the integers*](https://arxiv.org/abs/2609.30410) (arXiv:2609.30410, v1 24 September 2026). This paper proves a density strengthening of Moreira's {x, x+y, xy} result, which the paper cites in Section 1.1.
- [W. Huang, S. Shao, T. Tao, R. Xiao and N. Yang, *Monochromatic Sums and Products with Additive or Multiplicative Shifts in Natural Numbers*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i3p44) (Electron. J. Combin. 33(3), P3.44, 28 August 2026). This paper gives further partial results on monochromatic mixed sum/product configurations in N, alongside those of Moreira, Alweiss and Bowen surveyed in Section 1.1.
- [S. Chakraborty, S. Goswami and S. K. Patra, *Random Finite Sumsets and Product Sets in Subsets of the Natural Numbers*](https://arxiv.org/abs/2510.01301) (arXiv:2510.01301, October 2025). This paper studies finite-sum and finite-product sets in Bernoulli random subsets of N, a probabilistic counterpart to the FS(A)/FP(A) sets in Theorem 1.1.

## Digests and expositions
- [Yao Xu, *The statement and proof*](https://raw.githubusercontent.com/cadamcat/hindman-sums-products-lean4/main/docs/mathematics.md) (project documentation, accessed 2026-10-21). This guide maps the Lean development to the manuscript's sections and explains its replacement concatenation theorem and its bridge from OpenAI's cyclic inverse theorem to the nilsequence models used in §5.

## News and blogs
- [OfficeChai Team, *OpenAI Has Also Included Proofs For 23 Erdos Problems In Its Latest Math Proof Drop*](https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/) (OfficeChai, 9 October 2026). The article lists Problem 172 (this paper's result) among the claimed Erdős-problem results, noting it was one of four without a Lean formalization at the time of writing.
