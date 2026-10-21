# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Rapid mixing of graph switches for every degree sequence: Lean formalization scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/131.md) (lean/docs/131.md, result family 131, 2026). The release's scope note reports formal proofs of switch connectivity, the exponential total-variation estimate, the mixing-time bound $2n^8$, and the spectral-gap bound $1/(24n^2\binom n4)$, while excluding the exactly uniform sampling algorithm of Corollary 1.2. [family-level]
- [OpenAI math release, *SwitchChain.lean* (Comparator challenge)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/SwitchChain.lean) (lean/ComparatorChallenges, 2026). Comparator statement file containing `switch_chain_main`, `switch_chain_tv_bound` and `switch_connectivity`, with proofs left as `sorry` and supplied by the separate development.
- [OpenAI math release, *lean/OAI/Probability/SwitchChain*](https://github.com/mathcommunity/oai-math-revised/tree/main/lean/OAI/Probability/SwitchChain) (Lean source directory, 2026). The proof development behind the comparator statements, with modules for the three-row variance step, disjoint-pair estimates, Havel-based connectivity and the mixing-time arithmetic (`Main.lean`).

## Related prior literature mentioned by others
- [Weibo Fu, Qian Qin and Guanyang Wang, *Spectral Gap for the Binary Fixed-Margin Swap Chain*](https://arxiv.org/abs/2606.22636v2) (arXiv:2606.22636v2, 2026-07-13). The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/131-switch-chain-mixing/) identifies this bipartite predecessor and its three-row variance inequality as background to the manuscript's undirected argument; it is also cited in the manuscript's bibliography. [AI-generated per source]

## Possibly relevant literature (found by the agent, not checked)
- [S. J. Robertson, *Mixing Times of Switch Chains via High-Dimensional Expansion*](https://arxiv.org/abs/2610.09506) (arXiv:2610.09506, 7 Oct 2026). Proves $O(\Delta^2 m\log m)$ mixing for the switch chain when $m\ge C\Delta^8$, which can be compared with the paper's uniform bound $t_{\mathrm{mix}}(d)\le 2n^8$ (Theorem 1.1); it does not cite the release.
- [K. Tikhomirov and P. Youssef, *Sharp Poincaré and log-Sobolev inequalities for the switch chain on regular bipartite graphs*](https://arxiv.org/abs/2007.02729) (arXiv:2007.02729, 2020). Gives optimal Poincaré constants for the switch chain in a regular bipartite regime, relevant when comparing the spectral-gap lower bound $[24n^2\binom n4]^{-1}$ in Theorem 1.1 with known sharp gaps.
- [P. Gao and C. Greenhill, *Mixing time of the switch Markov chain and stable degree sequences*](https://arxiv.org/abs/2003.08497) (arXiv:2003.08497, 2020). Stability-based rapid-mixing results, including heavy-tailed/power-law sequences, belonging to the line of partial results that the introduction's history paragraph surveys.
- [P. L. Erdős, E. Győri, T. R. Mezei, I. Miklós and D. Soltész, *Half-graphs, other non-stable degree sequences, and the switch Markov chain*](https://arxiv.org/abs/1909.02308) (Electron. J. Combin. 28(3) (2021) P3.7). Exhibits non-P-stable families where the switch chain still mixes rapidly, relevant to the paper's point that Theorem 1.1 goes beyond P-stable families.

## Digests and expositions
- [AI Proved What?, *Switch chain mixes fast?*](https://aiprovedwhat.com/episodes/131-switch-chain-mixing/) (episode 131, October 2026). This video and transcript explain the claimed bounds through Curveball trades, overlapping and disjoint pair estimates, and comparison with individual switches, and report small-instance numerical checks while stating that the authors have not run the Lean check. [AI-generated per source] [family-level]

## News and blogs
- [Joe Halliwell, *Does any of the OpenAI maths have real-world consequences?*](https://joehalliwell.com/posts/openai-maths.html) (blog, 2026-10-08). The section on random networks discusses this paper's relevance to degree-preserving network null models and the gap between its $2n^8$ guarantee and practical simulation budgets; the post credits Claude Opus 5.5 as co-author. [AI-generated per source]
