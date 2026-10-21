# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Samuel Kittle, Constantin Kogler, *The Exact Overlaps Conjecture for Self-Similar Measures on the Real Line*](https://arxiv.org/abs/2610.10511) (arXiv:2610.10511, 7 Oct 2026). An independent preprint whose Theorem 1.1 is the same formula, dim ν = min{1, h_μ/|χ_μ|}, noting that "A proof of Theorem 1.1 was independently announced in [20] as paper number 148"; it says its entropy inequality strengthens Lemma 3.2 of paper 148 and contrasts its variance-summation argument with paper 148's entropy-growth arguments. Per its machine contribution statement, GPT-6 Astra found the first proof presented to the authors on 27 September 2026. [AI-generated per source]
- [Samuel Kittle, Constantin Kogler, *Supplementary material for the exact overlaps conjecture for self-similar measures on the real line*](https://github.com/ckkogler/kk26-supplementary-material) (GitHub, 2026). Model-written manuscripts and a conversation transcript (27 Sep–5 Oct 2026) behind the Kittle–Kogler proof, including explorations of a sharper entropy-loss bound and higher-dimensional extensions, which the repository distinguishes from the established results of the main paper. [AI-generated per source]

## Expert comments and discussion
- [Jörg Neunhäuserer, comment on *AHM Statement on OpenAI's October 6 Release of Mathematical Documents* (Terence Tao's blog)](https://terrytao.wordpress.com/2026/10/07/ahm-statement-on-openais-october-6-release-of-mathematical-documents/#comment-697228) (8 Oct 2026). The commenter writes "I worked on three of the problems that have now been solved by ChatGPT (153, 148, and 146)" and reflects on how mathematicians might respond; an anonymous reply notes that the solutions have not yet been independently peer-reviewed.
- [Zhou Feng, contribution to *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/comment-page-1/) (Proofs and Prompts, Oct 2026). Feng discusses item 148, observes that its proof appears to work within the framework developed by earlier mathematicians, and says he intends to study it further.

## Formalization
- [OpenAI math release, *Lean scope notes for result 148* (lean/docs/148.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/148.md) (OpenAI math release, Oct 2026). Describes the release's Lean formalization of dim_H μ = min{1, h_RW/χ}, with signed and unequal ratios and exact overlaps allowed, and of the two no-exact-overlap corollaries (homogeneous measures; attractor formula dim_H K = min{1, s}), linking comparator statements `SelfSimilar.lean` and `SelfSimilarCorollaries.lean`.
- [OpenAI math release, *SelfSimilar.lean* comparator statement](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/SelfSimilar.lean) (OpenAI math release, Oct 2026). Lean statement `OAI.EntropyRateDimension.entropy_rate_dimension`: the lower Hausdorff dimension of the self-similar measure equals `min 1 (entropyRate / lyapunov)`; as a challenge statement, its proof body is `sorry`.
- [Constantin Kogler, Samuel Kittle, *A Lean formalization of the exact overlaps conjecture in dimension one*](https://github.com/ckkogler/exact-overlaps-one-dim-lean) (GitHub, 2026). An independent Lean formalization of the seventeen numbered results and Definition 3.5 of arXiv:2610.10511, including the same dimension formula min 1 (h/|χ|) and Hochman's Theorem 1.4; the README says OpenAI Codex assisted with the Lean implementation and automated checking. [AI-generated per source]

## Related prior literature mentioned by others
- [Samuel Kittle, Constantin Kogler, *Dimension of contracting on average self-similar measures*](https://arxiv.org/abs/2501.17795v1) (arXiv:2501.17795v1, 29 Jan 2025). Kittle–Kogler's October 2026 paper identifies this work's variance summation method as an ingredient in its alternative deduction of the dimension formula also asserted by paper 148.

## Possibly relevant literature (found by the agent, not checked)
- [Péter P. Varjú, *Self-similar sets and measures on the line*](https://arxiv.org/abs/2109.10629) (arXiv:2109.10629, Sep 2021). An earlier survey of the dimension theory of self-similar sets and measures on the line, background for the exact-overlaps history the paper recounts; the paper cites only Varjú's 2026 entropy-rate survey.
- [Michael Hochman, *On self-similar sets with overlaps and inverse theorems for entropy in ℝ^d*](https://arxiv.org/abs/1503.09043) (arXiv:1503.09043, 2015/2017). The higher-dimensional version of the Hochman 2014 dichotomy used as background in the paper, relevant to whether its line-only theorem extends beyond ℝ.
- [Meng Wu, *Projection theorems with countably many exceptions and applications to the exact overlaps conjecture*](https://arxiv.org/abs/2503.21923) (arXiv:2503.21923, 2025). Recent work on parameter families of self-similar measures, with stated applications to the exact overlaps conjecture that Theorem 1.1 is said to resolve on the line.

## Digests and expositions
- [Latent Seminar, *Self-similar dimension from affine-map entropy*](https://lowrank.github.io/latent-seminar/OpenAI-Math/148-self-similar-dimension) (6 Oct 2026). Explains paper 148's map entropy, repeated-map examples, finite-law fair-pair estimate and disjoint-window argument, stating that it does not independently verify the complete proof.

## News and blogs
- [MINT Lab, *Yesterday in AI · 6 October 2026*](https://mintresearch.org/newsletters/yinai/2026-10-06/) (newsletter, Oct 2026). Covers the Kittle–Kogler preprint as "a concrete case of parallel discovery", citing OpenAI's proof claimed on 24 September and public on 6 October, and Kittle–Kogler's found on 27 September and posted on 7 October. [AI-generated per source]
