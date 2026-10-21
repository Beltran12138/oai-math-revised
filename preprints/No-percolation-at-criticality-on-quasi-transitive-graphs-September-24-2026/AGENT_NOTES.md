# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Nutelligence Research, *Independent Research Inspired by OpenAI’s Critical Percolation Work*](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886) (OpenAI Developer Community, post 15, 2026-10-17). This announcement explicitly cites family 213 as inspiration for claimed site-percolation results on periodic, quasi-transitive and specialized lattice graphs, reports Lean verification, and notes an additional assumption for the quasi-transitive result and unresolved novelty assessment. [family-level]

## Expert comments and discussion
- [Olle Häggström, *What I write about the day after the most earth-shattering event in the history of mathematics*](https://haggstrom.substack.com/p/what-i-write-about-the-day-after) (Crunch Time for Humanity, 2026-10-07). Häggström links both manuscripts among percolation problems he had worked on, mentions the role of the van den Berg–Häggström–Kahn inequality, and postpones detailed assessment. [family-level]

## Formalization
- [OpenAI math release, *Critical percolation on every quasi-transitive graph* (Lean scope note lean/docs/213.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/213.md) (OpenAI math release, 2026-10-06). The release's scope note says the Lean development proves that bond percolation has no infinite cluster at $p_c$ on every infinite connected locally finite quasi-transitive graph with $p_c<1$, with bond multiplicities allowed, alongside the $\mathbb Z^3$ bond and site statements. [family-level]
- [OpenAI, *lean/OAI/Probability/CriticalPercolation/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/CriticalPercolation/Main.lean) (openai/math, commit adc7f12). This is the release's Lean main file for this paper, with the theorem `no_percolation_at_criticality` for locally finite quasi-transitive bond graphs with critical probability below 1.
- [Justin Leder (Lean code by Anthropic's Claude models), *anthropics/formal-math: percolation*](https://github.com/anthropics/formal-math/tree/795efb86f191735c5481675763537cfb4ff37e55/percolation) (GitHub, commit 795efb8, 2026). This is an independent, earlier Lean formalization of the $\mathbb Z^d$ case ($d\ge2$) of this paper's theorem, through Kozma–Nitzan's reduction; the paper cites it as Leder2026. [AI-generated per source]
- [Ahmed Bou-Rabee (Lean code by ChatGPT and Claude), *percolation-after-anthropic*](https://github.com/nitromannitol/percolation-after-anthropic) (GitHub, 2026). This is an independent, earlier Lean development that includes Kozma–Nitzan Conjectures 1–4 and 6 on finite graphs, which bear on this paper's joint gluing inequality, and covers critical site percolation on $\mathbb Z^d$ for $d\ge3$; the paper cites the related expositions. [AI-generated per source]

## Related prior literature mentioned by others
- [Gil Kalai, *Amazing: There is no Percolation at the Critical Probability in all Dimensions. (Solved by AI via a conjecture of Gady Kozma and Shahaf Nitzan.)*](https://gilkalai.wordpress.com/2026/09/03/amazing-there-is-no-percolation-at-the-critical-probability-in-all-dimensions-solved-by-ai-via-a-conjecture-of-gady-kozma-and-shahaf-nitzan/) (Combinatorics and more, 2026-09-03). Kalai's 7 October post presents this quasi-transitive result as extending the setting of this earlier post on the AI-produced $\mathbb Z^d$ bond proof. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Arthur Blanc-Renaudie, *Notes on Kozma and Nitzan's proof of θ(p_c)=0*](https://arxiv.org/abs/2610.10502) (arXiv:2610.10502, 2026-10-07). This gives a human-written proof of the Kozma–Nitzan conjectures. It is relevant to the paper's joint gluing theorem (Theorem joint-gluing), which the paper relates to Kozma–Nitzan Conjecture 1.
- [Jianping Jiang, Sike Lang, Yuxuan Sun, *A connection inequality for the random-cluster model*](https://arxiv.org/abs/2610.26419) (arXiv:2610.26419, 2026-10-19). This proves a slightly generalized Kozma–Nitzan connection inequality for the random-cluster model with $q\ge1$, which bears on the paper's joint gluing inequality for Bernoulli percolation.
- [Lucas Flammant, *A finite-graph conjecture related to θ(p_c)=0 for Bernoulli bond percolation on Z^d*](https://arxiv.org/abs/2609.03492) (arXiv:2609.03492, 2026-09-03). This proposes a finite-graph connection statement that implies $\theta(p_c)=0$ on $\mathbb Z^d$. It is related to the paper's relay-set consequence of joint gluing used in the corridor exploration.

## Digests and expositions
- None found.

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 2026-10-07). Item 20 of the post lists the release's "absence of infinite critical clusters" for bond percolation on infinite connected locally finite quasi-transitive graphs with $p_c<1$, next to the separate $p_c<p_u$ family, and relates it to the earlier AI-assisted lattice criticality result.
