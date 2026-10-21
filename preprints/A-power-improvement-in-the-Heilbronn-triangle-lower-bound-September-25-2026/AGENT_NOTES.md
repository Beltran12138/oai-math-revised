# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Ivan Blinov (@littleBro), *heilbronn-triangle-bounds*](https://github.com/littleBro/heilbronn-triangle-bounds) (GitHub repository, conditional research draft). Calls itself a conditional extension of this manuscript (pinned at commit fd4aeeb), using extension degree d = 5 and a shifted sphere packing to state a conditional exponent η = 1/145,278,430, with selected parts formalized in Lean 4 (not the full Heilbronn theorem); it says it was made with "substantial OpenAI Codex assistance" and has no peer review. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [mathcommunity/oai-math-revised, *lean/docs/191.md*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/191.md) (OpenAI Math Release Lean scope note, 2026-10-06). Describes a formalized power lower bound for an unbounded sequence of sizes $n$, sufficient to refute the almost $n^{-2}$ upper bound, and explicitly distinguishes this from the manuscript's assertion for every sufficiently large $n$. [family-level]
- [OpenAI, *lean/ComparatorChallenges/HeilbronnTriangle.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HeilbronnTriangle.lean) (openai/math, commit adc7f12). Comparator statements `heilbronn_power_lower_bound` and `almost_n_minus_two_refuted`, with the explicit exponent 1/(100000·K), where K is built from binomial coefficients.
- [OpenAI, *lean/OAI/Geometry/HeilbronnTriangle/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/HeilbronnTriangle/Main.lean) (openai/math, commit adc7f12). The Lean proofs of the two comparator theorems; they rely on imported modules (`Definitions`, `Refutation`, `ActualWeightedFiberCount`).

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [C. Bertram-Kretzberg, T. Hofmeister, H. Lefmann, *An Algorithm for Heilbronn's Problem*](https://api.crossref.org/works/10.1137/S0097539798348870) (SIAM J. Comput. 30(2), 383–390, 2000). A deterministic polynomial-time version of the Komlós–Pintz–Szemerédi (log n)/n² lower bound, which is the bound the paper's Theorem 1.1 improves by a power.
- [Tao Jiang, Ming Li and Paul Vitányi, *The Average-Case Area of Heilbronn-Type Triangles*](https://arxiv.org/abs/math/9902043) (Random Structures & Algorithms 20(2), 2002; arXiv:math/9902043). Its order-$n^{-3}$ expected minimum triangle area for independent uniform points gives a probabilistic comparison point for the manuscript's arithmetic sampling and deletion construction behind the $n^{-2+\eta}$ lower bound.

## Digests and expositions
- None found.

## News and blogs
- None found.
