# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 110: Optimal-order randomized k-server on arbitrary metrics*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/110.md) (lean/docs/110.md, October 2026). The release's own scope description: it says the formalization proves the $O((\log(k+1))^2)$ bound for all $k\ge2$ and all metric spaces with at least $k+1$ points, with an additive constant that is zero for distinct starts, and it links the comparator statements for this and the companion uniform-computation result. [family-level]
- [OpenAI, *KServer/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/KServer/Main.lean) (openai/math, commit adc7f12). Lean file containing `main_theorem : MainStatement`, the formal counterpart of Theorem 1.1. The file shows no `sorry`, but it imports further modules that were not inspected here.
- [OpenAI, *ComparatorChallenges/KServer.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KServer.lean) (openai/math, commit adc7f12). Standalone comparator statement of the main theorem (proof left as `sorry` by design), for checking that the formal statement matches Theorem 1.1.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Indyk, Magen, Sidiropoulos, Zouzias, *Online Embeddings*](https://dspace.mit.edu/handle/1721.1/72043) (APPROX-RANDOM 2010, LNCS 6302, 246–259). Studies metric embeddings, including into distributions over ultrametrics, built as points arrive; possibly relevant to the paper's request-driven changing partitions (Sections 7–8) and its discussion of dynamic embeddings.
- [Bubeck, Cohen, Lee, Lee, *Metrical task systems on trees via mirror descent and unfair gluing*](https://arxiv.org/abs/1807.04404) (arXiv:1807.04404, 2018). Companion to the cited BCLLM18 mirror-descent framework, applied to HSTs; possibly relevant to the tree allocation theorem (Sections 3–5) and its treatment of per-level losses.
- [Wenbin Chen, *An O(log k log^2 n)-competitive Randomized Algorithm for the k-Sever Problem*](https://arxiv.org/abs/1510.07773) (arXiv:1510.07773, 2015). Claims a finite-metric bound with $n$-dependence that the introduction's survey of prior bounds (BBMN15, BCLLM18) does not mention; the arXiv page carries an admin note about text overlap with arXiv:1410.4955.

## Digests and expositions
- [Latent Seminar, *Randomized k-server: competitive ratios and uniform computation*](https://lowrank.github.io/latent-seminar/OpenAI-Math/110-randomized-k-server) (blog exposition, 2026-10-07). Exposition of both manuscripts' proof mechanisms, including partition and allocation costs, the bounded request filter, and delayed activation; it states that it did not independently verify the complete proofs. [family-level]
- [Gradient Damage, *Unique Games Conjecture, Bin Packing and 8 More in Theoretical Computer Science*](https://gradientdamage.com/videos/unique-games-conjecture-bin-packing-and-8-more-in-theoretical/) (video compilation, 2026-10-15). The chapter beginning at 1:25 introduces randomized k-server through a taxi analogy, and its accompanying text attributes the arbitrary-metric bound and finite-rational-metric implementation claims to OpenAI. [family-level]

## News and blogs
- [JinV+, *OpenAI Just Solved Hundreds of Math Problems. The Fight Over How It Did That Is Just Beginning.*](https://vocal.media/01/openai-just-solved-hundreds-of-math-problems-the-fight-over-how-it-did-that-is-just-beginning) (vocal.media, October 2026). Article about the release with a short section titled "k-server Closes", mentioning the randomized problem and the Bubeck–Coester–Rabani lower bound next to the Coester–Koutsoupias–Zbysiński deterministic result, without naming these manuscripts. [family-level]
