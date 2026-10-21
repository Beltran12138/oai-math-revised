# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [Ben Green, contribution to *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/comment-page-1/) (Proofs and Prompts, posted 8 October 2026, updated 19 October 2026). Green singles out result 182's square-difference power saving as the result he intends to study first, while emphasizing the work needed to understand the manuscripts.
- [Steve Fan and Andrew Lott, *The optimal van der Corput property for squares*](https://arxiv.org/html/2610.07765v2) (arXiv:2610.07765v2, 12 October 2026). An introductory remark says "A prominent AI company has circulated a draft claiming the power-saving bound", calls it "largely unreadable", notes its claimed Lean certificate, and records that their first submission preceded the release's initial repository commit; the paper itself proves an $N\exp(-c\sqrt{\log N\log\log N})$ bound and shows the van der Corput property cannot give a power saving.
- [Telegram channel @MathfromKrach, post on the OpenAI release](https://t.me/s/MathfromKrach/215) (Telegram, October 2026). The post lists the claimed $N^{1-c}$ bound for square-difference-free sets among the highlighted results and cautions that papers without Lean certificates may contain mistakes. [family-level]

## Formalization
- [OpenAI, *Power savings for intersective polynomial differences and prime arguments: Lean scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/182.md) (OpenAI Math Release, lean/docs/182.md, 6 October 2026). The family scope note states that the formalization proves Theorem 1.1 of this paper, $|A|\le CN^{1-c}$ for square-difference-free $A\subseteq[N]$ with absolute constants, uniformly for all $N\ge1$. [family-level]
- [OpenAI math release, *SquareDifference.lean*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/SquareDifference.lean) (lean/ComparatorChallenges). The comparator statement `OAI.SquareDifference.power_saving` that the scope note links for this theorem.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Eric Naslund (contributor), *Square-difference-free sets of exponent 0.7580758*](https://hexagonmath.org/2610.00151v1) (Hexagon 2610.00151v1, Oct 2026). Gives a computer-assisted lower-bound construction with exponent $0.7580758\ldots$, above the Krachun exponent the paper cites as the lower end of the remaining gap; the page says the Lean formalization is registered as PALOMAR-2026-09-19-000006. [AI-generated per source]
- [Khalid Younis, *Sets whose differences avoid a bracket quadratic*](https://arxiv.org/abs/2608.30078) (arXiv:2608.30078, 30 Aug 2026). Proves a fixed power saving $N^{1-c}$ in a Furstenberg–Sárközy-type problem with a bracket-quadratic difference set, obtained via the van der Corput property.
- [Alexandros Kalogirou, Andrew Lott, Ákos Magyar, Akash Singha Roy, *The Furstenberg–Sárközy theorem for sums of an even number of odd powers*](https://arxiv.org/abs/2609.16595) (arXiv:2609.16595, 15 Sep 2026). Proves power-saving bounds for sets whose differences avoid sums of an even number of odd $k$-th powers, a multi-variable relative of the single-square problem treated here.

## Digests and expositions
- [Gradient Damage, *Circulant Hadamard Conjecture, Cycle–Clique Ramsey Numbers and 7 More in Combinatorics*](https://gradientdamage.com/videos/circulant-hadamard-conjecture-cycle-clique-ramsey-numbers-and-7-more/) (video compilation, 15 October 2026). The chapter beginning at 2:26 illustrates square-difference avoidance, while its accompanying text summarizes the family's intersective-polynomial and prime-argument claims. [family-level]

## News and blogs
- None found.
