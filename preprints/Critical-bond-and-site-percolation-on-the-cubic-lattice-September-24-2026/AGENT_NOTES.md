# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Nutelligence Research, *Independent Research Inspired by OpenAI’s Critical Percolation Work*](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886) (OpenAI Developer Community, post 15, 2026-10-17). This announcement explicitly cites family 213 as inspiration for claimed site-percolation results on periodic, quasi-transitive and specialized lattice graphs, reports Lean verification, and notes an additional assumption for the quasi-transitive result and unresolved novelty assessment. [family-level]

## Comments and discussion
- [Olle Häggström, *What I write about the day after the most earth-shattering event in the history of mathematics*](https://haggstrom.substack.com/p/what-i-write-about-the-day-after) (Crunch Time for Humanity, 2026-10-07). Häggström links both manuscripts among percolation problems he had worked on, mentions the role of the van den Berg–Häggström–Kahn inequality, and postpones detailed assessment. [family-level]

## Formalization
- [OpenAI math release, *Critical percolation on every quasi-transitive graph* (Lean scope note lean/docs/213.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/213.md) (OpenAI math release, 2026-10-06). The release's scope note says the Lean development proves that nearest-neighbour bond and site percolation on $\mathbb Z^3$ have no infinite cluster at their critical parameters, and it states the quasi-transitive bond theorem, linking the two comparator statements. [family-level]
- [OpenAI, *lean/OAI/Probability/CriticalZ3/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/CriticalZ3/Main.lean) (openai/math, commit adc7f12). This is the release's Lean main file for this paper; its theorem `critical_no_infinite` combines `bond_critical_no_infinite` and `site_critical_no_infinite` on $\mathbb Z^3$.
- [Justin Leder (Lean code by Anthropic's Claude models), *anthropics/formal-math: percolation*](https://github.com/anthropics/formal-math/tree/795efb86f191735c5481675763537cfb4ff37e55/percolation) (GitHub, commit 795efb8, 2026). This is an independent, earlier Lean formalization of $\theta(p_c)=0$ for nearest-neighbour bond percolation on $\mathbb Z^d$ for all $d\ge2$, which covers the bond half of this paper; the paper cites it as Leder2026. [AI-generated per source]
- [Ahmed Bou-Rabee (Lean code by ChatGPT and Claude), *percolation-after-anthropic*](https://github.com/nitromannitol/percolation-after-anthropic) (GitHub, 2026). This is an independent, earlier Lean development of critical site nonpercolation on $\mathbb Z^d$ for $d\ge3$ and of finite bond and hyperedge gluing inequalities, building on Anthropic’s bond-percolation library, which covers the site half of this paper; the paper cites the related exposition as SitePublic2026. [AI-generated per source]

## Related prior literature mentioned by others
- [Gil Kalai, *Amazing: There is no Percolation at the Critical Probability in all Dimensions. (Solved by AI via a conjecture of Gady Kozma and Shahaf Nitzan.)*](https://gilkalai.wordpress.com/2026/09/03/amazing-there-is-no-percolation-at-the-critical-probability-in-all-dimensions-solved-by-ai-via-a-conjecture-of-gady-kozma-and-shahaf-nitzan/) (Combinatorics and more, 2026-09-03). Kalai's 7 October post presents the OpenAI criticality result as extending the setting of this earlier post on the AI-produced $\mathbb Z^d$ bond proof; its comment thread discusses whether the formalization has been verified. [family-level]
- [Nikita Gladkov and Aleksandr Zimin, *Bond percolation does not simulate site percolation*](https://arxiv.org/abs/2404.08873) (arXiv:2404.08873, 2024-04-13; revised 2026-02-03). Cited in the earlier [site-percolation exposition](https://nitromannitol.github.io/site-percolation-7d3f2/), its obstruction to approximating site connectivity by independent-bond gadgets provides context for the cubic manuscript’s separate hyperedge treatment of sites.

## Possibly relevant literature (found by the agent, not checked)
- [Arthur Blanc-Renaudie, *Notes on Kozma and Nitzan's proof of θ(p_c)=0*](https://arxiv.org/abs/2610.10502) (arXiv:2610.10502, 2026-10-07). This gives a human-written proof of the Kozma–Nitzan conjectures. It is relevant to the paper's finite connection inequality (intro, eq. (1)), which the paper says implies Kozma–Nitzan Conjecture 1.
- [Jianping Jiang, Sike Lang, Yuxuan Sun, *A connection inequality for the random-cluster model*](https://arxiv.org/abs/2610.26419) (arXiv:2610.26419, 2026-10-19). This proves a slightly generalized Kozma–Nitzan connection inequality for the random-cluster model with $q\ge1$. It relates to the paper's finite hyperedge comparison, which is stated for independent bits only.
- [Lucas Flammant, *A finite-graph conjecture related to θ(p_c)=0 for Bernoulli bond percolation on Z^d*](https://arxiv.org/abs/2609.03492) (arXiv:2609.03492, 2026-09-03). This proposes a finite-graph statement about reaching boundary vertices whose increasing events occur, which implies $\theta(p_c)=0$ on $\mathbb Z^d$. It is close in form to the paper's relay failure bound derived from the comparison inequality.

## Digests and expositions
- [Perplexity / Orply, *Critical Percolation on the Cubic Lattice Has No Infinite Cluster*](https://orply.com/articles/perplexity/213-1-critical-bond-and-site-percolation-on-the-cubic-lattice-0afddf10) (Orply, 2026-10-11). This AI-assisted exposition summarizes the manuscript’s finite hyperedge comparison, site endpoint convention, and adaptive exploration with conditional failure bounds. [AI-generated per source]

## News and blogs
- None found.
