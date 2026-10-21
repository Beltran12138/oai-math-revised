# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [rob-p (GitHub), *practical-scs-2opt*](https://github.com/rob-p/practical-scs-2opt) (GitHub repository with Typst note, Python reference and Rust implementation). Says the base graph needs only the at most 2L prefixes and suffixes rather than all O(L²) substrings, and benchmarks the algorithm against greedy and the lower bound W on repeat-rich and real data.
- [Krushna Dere and Svyatoblood (nurric-ai), *lazy-scs: Scalable factor-2 shortest common superstring*](https://github.com/nurric-ai/lazy-scs) (GitHub repository with Rust/Python implementation and Lean 4 file, October 2026). Implements the algorithm with periodic rules applied lazily, reports runs on a 4.64 Mb E. coli genome, and formalizes the lower-bound argument in Lean, taking the paper's count facts as hypotheses; the README says some construction branches "never fired in any test". [AI-generated per source]
- [bkarak (GitHub), *shortest-superstring-js*](https://github.com/bkarak/shortest-superstring-js) (GitHub repository, JavaScript). Implements the paper's algorithm as `twoApprox` next to Greedy, MGREEDY, TGREEDY and an exact solver, and reports benchmarks including the family {c(ab)^k, (ba)^k, (ab)^k c}, where it reports greedy outputs of 4k+2 against the algorithm's 2k+6.
- [rongou (GitHub), *superstring-rs*](https://github.com/rongou/superstring-rs) (GitHub repository, Rust). Provides preprocessing, an exact solver, a greedy baseline and the occurrence-count lower bound W as groundwork for the paper's algorithm; the README states the approximation algorithm itself is not implemented yet.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *A factor-two approximation for shortest common superstring — Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/128.md) (OpenAI Math Release, lean/docs/128.md, 2026-10-06). The release's scope note describes a Lean formalization of a deterministic polynomial-time factor-two algorithm for every finite list of explicitly encoded strings, with time measured in input bits and approximation in symbol length, and links the comparator statement `ComparatorChallenges/Superstring.lean`.
- [buberlo (GitHub), *VeriSCS*](https://github.com/buberlo/veriscs) (GitHub repository, example run dated 2026-10-07). Packages the release's Lean function `OAI.Superstring.answer` (openai/math commit adc7f12) as an executable, reports axiom checks and running times, and leaves a human review of `IsCommonSuperstring` and `opt` against classical SCS as an open item ([issue list](https://github.com/buberlo/veriscs/issues)).

## Related prior literature mentioned by others
- [Hiroki Shibata, *Disproving the Greedy Superstring Conjecture*](https://arxiv.org/abs/2609.01365) (arXiv:2609.01365, 1 September 2026). Cited by the VeriSCS and lazy-scs repositories next to this paper as the claimed counterexample to the Tarhio–Ukkonen greedy conjecture (ratio at least 9/4); also in the paper's bibliography.
- [Nikolai Chukhin, Alexander S. Kulikov, Ivan Mihajlin, Alexander Smal, *A Tight Cycle-Cover Inequality for Shortest Common Superstring*](https://arxiv.org/abs/2609.27921) (arXiv:2609.27921, v1 21 August 2026, v2 24 September 2026). Cited in the VeriSCS README as the 7/3-approximation preceding this paper; the paper cites the ECCC version TR26-157, and the arXiv v2 comment reads "updated the proof's exposition".

## Possibly relevant literature (found by the agent, not checked)
- [Alexander Golovnev, Alexander S. Kulikov, Ivan Mihajlin, *Approximating Shortest Superstring Problem Using de Bruijn Graphs*](https://golovnev.org/papers/scs_apx.pdf) (CPM 2013). An earlier approximation algorithm by the same group, based on rural postman paths in de Bruijn graphs, which may be relevant to the paper's graph and Euler-tour representation of superstrings (Section 1, "Proof overview").
- [Nikolai Chukhin, Alexander S. Kulikov, Ivan Mihajlin, Alexander Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*](https://arxiv.org/abs/2608.20018) (arXiv:2608.20018, August 2026). Lower bounds for the greedy algorithm on fixed-length strings, relevant to the paper's remark that its factor-2 guarantee does not apply to the Greedy procedure.
- [Maksim Nikolaev, *Greedy Conjecture for the Shortest Common Superstring Problem and its Strengthenings*](https://arxiv.org/abs/2407.20422) (arXiv:2407.20422, July 2024). Studies strengthenings of the Greedy conjecture and a locally greedy uniform 4-approximation, relevant to the paper's discussion of conjectures about specific procedures.

## Digests and expositions
- [梁植华, *最短公共超串的多项式时间 2-近似算法*](https://eksmu.com/en/w/6d5e4fa2-4ed3-41e1-a44f-a709b65ae427) (Eksmu, 2026-10-11). This Chinese-language guide outlines the manuscript's occurrence-count lower bound, balanced hierarchical graph, periodic layers and connection budgets, and distinguishes its algorithm from maximum-overlap Greedy.
- [Claude Opus 5.5 (Anthropic), *Shortest common superstrings*](https://kokunoyumeto.github.io/open-math-courses-public/courses/shortest-common-superstrings/) (Open Mathematics Courses, October 2026). Four lessons develop the manuscript's hierarchical graph, forced occurrence counts, periodic layers and connection argument with examples and exercises; the course identifies its checking as AI self-checking and says independent review is incomplete. [AI-generated per source]

## News and blogs
- None found.
