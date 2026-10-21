# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Homogeneous depth-five lower bounds for iterated matrix multiplication: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/135.md) (OpenAI math release, lean/docs/135.md, 2026-10-06). The scope note says the formalization covers the $n^{\sqrt n/400}$ lower bound over every characteristic-zero field (field-independent threshold, unrestricted bottom support and sharing) and the $n^{\sqrt n+4}$ upper bound over every field, and it points to the comparator statement `lean/ComparatorChallenges/DepthFive.lean`.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Neeraj Kayal and Chandan Saha, *Lower Bounds for Depth Three Arithmetic Circuits with Small Bottom Fanin*](https://eccc.weizmann.ac.il/report/2014/089/) (ECCC TR14-089, 2014; [CCC 2015, pp. 158–182](https://d-nb.info/1365607895/34)). Theorem 1.2 gives characteristic-zero homogeneous depth-five lower bounds of $N^{\Omega(\sqrt d)}$ for Nisan–Wigderson design polynomials with bottom fan-in restricted to $O(N^\mu)$ for fixed $\mu<1$, a restricted-bottom-fan-in precursor to this paper's claim of removing bottom-support restrictions for balanced IMM.
- [S. Chillara, N. Limaye and S. Srinivasan, *Small-depth Multilinear Formula Lower Bounds for Iterated Matrix Multiplication, with Applications*](https://arxiv.org/abs/1710.05481) (arXiv:1710.05481, 2017). It gives depth-dependent lower bounds for IMM in small-depth multilinear formulas, complementing the paper's survey of restricted-model IMM lower bounds (Fournier–Limaye–Malod–Srinivasan, Kayal–Saha–Tavenas), which does not list it.

## Digests and expositions
- [Latent Seminar, *Homogeneous depth-five matrix products*](https://lowrank.github.io/latent-seminar/OpenAI-Math/135-homogeneous-depth-five-matrix-products) (2026-10-07). This exposition explains the differentiation–multiplication rank measure, circuit-side dimension estimates, path moments, field transfer, and block upper bound, and states that it does not independently verify the complete proof.
- [Open Mathematics Courses, *Results on homogeneous depth-five circuits, a rank measure from derivatives and multiplications, and iterated matrix multiplication*](https://kokunoyumeto.github.io/open-math-courses-public/courses/depth-five-circuits-for-iterated-matrix-multiplication/providers.html) (undated). This guide links five lessons developing the paper's upper and lower bounds and identifies them as written and self-checked by Claude Opus 5.5, with independent mathematical review incomplete. [AI-generated per source]

## News and blogs
- None found.
