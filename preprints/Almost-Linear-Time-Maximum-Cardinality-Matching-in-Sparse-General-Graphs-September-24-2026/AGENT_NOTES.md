# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [spele1100 (GitHub), *reverse-matching: Reference implementation of 'Almost-Linear-Time Maximum-Cardinality Matching in General Graphs'*](https://github.com/spele1100/reverse-matching) (GitHub repository, 2026). A pure-Python reimplementation of the paper's reductions, phase machine, ledgers and assembly, tested against NetworkX blossom matching, with the pricing machinery of Sections 5–8 replaced by exact substitutes. The README states "Running time is not reproduced" and lists six deviations from the text. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- None found.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Varsha Dani, Thomas P. Hayes, Seth Pettie, *Maximum Matching on Regular Nonbipartite Graphs*](https://arxiv.org/abs/2609.14126) (arXiv:2609.14126, September 2026). Shows that blocking-flow algorithms run in deterministic $O(n^2)$ time on $d$-regular nonbipartite graphs. Relevant to the paper's comparison with Micali–Vazirani in the dense regime ($n^{2+o(1)}$ at $m=\Theta(n^2)$).
- [Dawei Huang, Seth Pettie, *Approximate Generalized Matching: f-Factors and f-Edge Covers*](https://arxiv.org/abs/1706.05761) (arXiv:1706.05761, 2017, rev. 2020). Gives linear-time approximation schemes for weighted $f$-factors and exact cardinality versions in $O(m\sqrt{f(V)})$ time. These are prior bounds to compare with the paper's $f$-factor corollary, which the introduction compares only with Gabow's $O(n^{2/3}m)$.
- [Taisuke Izumi, Naoki Kitamura, Yutaro Yamaguchi, *Forgetting Alternation and Blossoms: A New Framework for Fast Matching Augmentation and Its Applications to Sequential/Distributed/Streaming Computation*](https://arxiv.org/abs/2511.08210) (arXiv:2511.08210, November 2025). A recent augmentation framework for general-graph maximum matching, positioned relative to Micali–Vazirani, in the combinatorial line that the paper's context section surveys.

## Digests and expositions
- [Readable Intelligence, *Almost-Linear-Time Maximum-Cardinality Matching in General Graphs (readable version)*](https://readable-intelligence.com/paper/669239fdc7f9?view=readable) (readable-intelligence.com, undated). A rewritten readable version of the full paper; the page states that its proofs have not been independently checked. [AI-generated per source]
- [Gradient Damage, *Unique Games Conjecture, Bin Packing and 8 More in Theoretical Computer Science*](https://gradientdamage.com/videos/unique-games-conjecture-bin-packing-and-8-more-in-theoretical/) (video compilation, 2026-10-15). Chapter 9, beginning at 2:49, illustrates the claimed almost-linear-time maximum-matching result, and the accompanying page reproduces the matching and prescribed-degree-factor guarantees. [family-level]

## News and blogs
- [Scott Aaronson, *The Mathocalypse*](https://scottaaronson.blog/?p=10169) (Shtetl-Optimized, 2026-10-07). This post on the release lists the paper's result, "a randomized nearly linear-time algorithm" for finding a maximum matching, among the theoretical-computer-science results it highlights. [family-level]
