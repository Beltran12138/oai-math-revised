# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [queelius, *openai-math-counterexamples*](https://github.com/queelius/openai-math-counterexamples) (GitHub repository, accessed 2026-10-21). This project, which recomputes explicit counterexamples from the release, classifies family 162 as "not-explicit": it notes that $q_0$ is not given and the hypergraph comes from a random procedure, and it lists the smallest case $q=5$ as not attempted. [AI-generated per source]

## Formalization
- [OpenAI math release, *Counterexamples to Ryser's covering conjecture: Lean formalization scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/162.md) (lean/docs/162.md, 6 October 2026). The release's scope note states that the formalization proves this paper's balanced theorem: for every sufficiently large prime $q$, there is an intersecting $(q+1)$-partite hypergraph with $\tau=q+1$ and exactly $q+1$ nonisolated vertices per part, with an existential threshold (comparator `BalancedRyser.lean`). [family-level]
- [Kenta Kitamura (KitaKen1), *Formalize Ryser's conjecture and mark r = 4, ν ≤ 3 as solved*](https://github.com/google-deepmind/formal-conjectures/pull/6812) (google-deepmind/formal-conjectures PR #6812, opened 2026-10-03). This open PR states Ryser's conjecture in Lean and marks the general statement as `research open`; it predates the release and does not refer to these counterexamples. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Alexey Pokrovskiy, *Bounded diameter monochromatic component covers*](https://arxiv.org/abs/2507.05842) (arXiv:2507.05842, v2 2026-01-06). The abstract says that Gyárfás's tree-cover conjecture is equivalent to Milićević's bounded-diameter strengthening, which connects to the paper's Corollary 1.2 on monochromatic tree covers at ranks $q+1$.
- [Matija Bucić, Dániel Korándi, Benny Sudakov, *Covering graphs by monochromatic trees and Helly-type results for hypergraphs*](https://arxiv.org/abs/1902.05055) (arXiv:1902.05055, 2019). This paper studies monochromatic tree covers of $r$-edge-coloured graphs through hypergraph covering questions, the same correspondence that the paper's tree-cover corollary uses.

## Digests and expositions
- [Latent Seminar, *Intersecting hypergraphs and Ryser covering counterexamples*](https://lowrank.github.io/latent-seminar/OpenAI-Math/162-ryser-covering) (7 October 2026). Explains both affine-plane constructions, the obstruction to small covers and the monochromatic-tree consequence; the page states that it reviews statements and selected proof mechanisms rather than complete proofs. [family-level]
- [AI Proved What?, *Ryser disproved? Counterexamples to Ryser’s covering conjecture and Gyárfás’s tree-cover conjecture*](https://aiprovedwhat.com/episodes/162-counterexamples-rysers-covering-conjecture/) (episode 162, October 2026). An animated exposition with transcript distinguishing the two constructions, their asymptotic existence claims and tree-cover consequences, and describing the formalization scope without rebuilding the Lean development. [AI-generated per source] [family-level]

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 2026-10-07). Item 11 of the post describes the new counterexamples as intersecting $r$-partite $r$-uniform hypergraphs "requiring r vertices to meet every edge" and refers to Kalai's earlier post on Aharoni's tripartite proof. [family-level]
