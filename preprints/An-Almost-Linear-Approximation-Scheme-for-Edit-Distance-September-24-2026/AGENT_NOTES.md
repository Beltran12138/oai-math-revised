# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Bingbing Hu, Tomasz Kociumaka, Jakob Nogler, Barna Saha, *Tree Edit Distance: Near-Linear-Time Approximate, Sublinear, and Dynamic*](https://arxiv.org/abs/2610.22250) (arXiv:2610.22250, 15 October 2026; SODA 2027). A footnote cites this paper as having "claimed a randomized (1+ε)-approximation for ED in expected n^{1+o(1)} time for fixed ε>0"; the paper itself is about tree edit distance.
- [Jihan-Wang (GitHub), *An Almost-Linear Approximation Scheme for Metric-Weighted Edit Distance*](https://github.com/Jihan-Wang/metric-weighted-edit-distance) (GitHub repository, commits 8–9 October 2026). Manuscript that adapts this paper's refinement framework to edit costs from an arbitrary metric and claims expected time N^{1+O(log log log N / log log N)}. It also contains independent reading notes on this paper and states that it has no implementation and no formal proof.

## Comments and discussion
- [sebzim4500, *Comment on “Sharing AI progress in mathematics”*](https://news.ycombinator.com/item?id=49993877) (Hacker News, October 2026). This brief reader comment discusses the manuscript’s readability and questions the completeness of its linked Lean challenge, without providing a mathematical review.

## Formalization
- [OpenAI, *Almost-linear approximation of edit distance: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/121.md) (OpenAI math release, 6 October 2026). Describes the scope of the release's own Lean formalization: the fixed-rational-accuracy $(1+\varepsilon)$ guarantee with probability at least 2/3, deterministic zero on equal strings, expected work $(N+2)^{1+\eta}$ for every fixed $\eta>0$ and sufficiently large $N$, and polynomial space.
- [OpenAI, *EditApproximation.lean* comparator challenge](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/EditApproximation.lean) (openai/math, commit adc7f12). The comparator statement file for this result, about 19,000 lines long, which the scope note links to.

## Related prior literature mentioned by others
- [Xiao Mao and Aviad Rubinstein, *Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time*](https://arxiv.org/abs/2603.29702) (arXiv:2603.29702, 31 March 2026). The AI Proved What? exposition identifies this fixed-accuracy randomized approximation scheme with running time $n^2/2^{\log^{\Omega(1)}n}$ as a predecessor to the manuscript’s claimed almost-linear bound.

## Possibly relevant literature (found by the agent, not checked)
- [Egor Gorbachev, *Factor Three Approximation for Edit Distance*](https://arxiv.org/abs/2610.01311) (arXiv:2610.01311, 1 October 2026). Gives a randomized factor-3 approximation for unweighted edit distance in $\widetilde{O}(N^{11/6})$ time, a point of comparison for the manuscript’s claimed fixed-$(1+\varepsilon)$ almost-linear scheme.
- [Debarati Das, Jacob Gilbert, MohammadTaghi Hajiaghayi, Tomasz Kociumaka, Barna Saha, *Weighted Edit Distance Computation: Strings, Trees and Dyck*](https://arxiv.org/abs/2302.04229) (arXiv:2302.04229, February 2023; STOC 2023). Exact weighted edit distance in O(n+poly(k)) time; relevant to the paper's comparison of its unit-cost model with weighted edit-cost models.
- [Sudatta Bhattacharya, Sanjana Dey, Elazar Goldenberg, Michal Koucký, *Many Flavors of Edit Distance*](https://arxiv.org/abs/2410.09877) (arXiv:2410.09877, October 2024). Reductions from arbitrary to binary alphabets and between indel and edit distance; relevant to the paper's choice of polynomially bounded integer alphabets with no fixed alphabet bound.

## Digests and expositions
- [Latent Seminar, *An almost-linear approximation scheme for edit distance*](https://lowrank.github.io/latent-seminar/OpenAI-Math/121-edit-distance-approximation) (7 October 2026). This exposition explains the fixed-accuracy runtime contract, adaptive seed estimates, alignment bands and recursive work accounting, while explicitly disclaiming independent verification of the complete proofs.
- [AI Proved What?, *Almost-linear edit distance? A claimed approximation scheme for edit distance*](https://aiprovedwhat.com/episodes/121-edit-distance-approximation-scheme/) (episode 121, October 2026). This video and transcript explain the claim and refinement strategy with illustrative computations and discuss the very large asymptotic thresholds; the project discloses AI-assisted scripts and animations and AI-generated narration. [AI-generated per source]

## News and blogs
- None found.
