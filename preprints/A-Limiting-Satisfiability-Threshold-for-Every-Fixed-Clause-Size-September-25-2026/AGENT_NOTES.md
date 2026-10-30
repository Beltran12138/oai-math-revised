# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [P. M. Aronow and Patrick Lopatto, *Existence of the $q$-Colorability Threshold for Sparse Random Graphs*](https://hexagonmath.org/abs/2610.00608v1) (Hexagon 2610.00608v1, 28 October 2026). Adapts this paper's capped hitting-time variance bound (Lemmas 3.1–3.2), product inequality and balanced-tree convergence (Lemmas 5.2 and 5.4) to prove a limiting $q$-colorability threshold for every fixed $q\ge3$ with a window of order $n(\log n)^{-3/2}$ edges, replacing the variable-deletion step (Proposition 2.2), which it says does not carry over to colorings, by frozen-pair estimates. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Limiting random SAT thresholds, sharp variance and computability — Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/235.md) (lean/docs/235.md, October 2026). Describes a Lean statement of the existence of a finite positive limiting threshold $\alpha_k$ for every fixed $k\ge3$, for independent proper uniformly signed clauses sampled with replacement (comparator `FixedClauseThreshold.lean`), with no assertion at $c=\alpha_k$. [family-level]

## Related prior literature mentioned by others
- [Gaia Carenini, *A polynomial scaling window for random k-SAT and a proof of the satisfiability conjecture*](https://eccc.weizmann.ac.il/report/2026/229/) (ECCC TR26-229, 5 October 2026). This concurrent work establishes limiting thresholds for every fixed $k\ge3$ through a polynomial window bound and the Abbe–Montanari criterion; the release and OfficeChai credit it with priority. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [W. Perkins, *Searching for (sharp) thresholds in random structures: where are we now?*](https://arxiv.org/abs/2401.01800) (arXiv:2401.01800, 2024). A survey of thresholds and sharp thresholds in random structures, motivated in part by the Ding–Sly–Sun large-$k$ result; it gives background on the satisfiability conjecture that Theorem 1.1 addresses for every fixed $k\ge3$.

## Digests and expositions
- None found.

## News and blogs
- [OfficeChai Team, *OpenAI Releases Over 300 Mathematical Results Produced By An Internal Model*](https://officechai.com/ai/openai-releases-over-300-mathematical-results-produced-by-an-internal-model/) (OfficeChai, 7 October 2026). Discusses the random SAT family specifically through its credit to Carenini for priority on threshold existence. [family-level]
