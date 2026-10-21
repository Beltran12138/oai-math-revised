# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release / mathcommunity, *Lean scope notes for family 231*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/231.md) (lean/docs/231.md, 6 October 2026). The release's scope note says the formalization covers the universal root-independent FUSF factor theorem and supplements on strongly Rayleigh and determinantal laws on countable groups, with links to the comparator statements `FreeUniformSpanningForest.lean` and `StronglyRayleighDPP.lean`.
- [OpenAI, *SpanningForest/Factor.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/SpanningForest/Factor.lean) (openai/math, commit adc7f12). States `fusf_is_factor_iid` (a single Borel equivariant factor rule on every graph code) and `fusf_factor_for_every_unimodular_law`, corresponding to Theorem 1.1 and Corollary 1.2 of the paper.
- [OpenAI, *StrongRayleigh/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/StrongRayleigh/Main.lean) (openai/math, commit adc7f12). States `strongly_rayleigh_group_factor` and `invariant_positive_contraction_dpp_factor`, among other results, corresponding to the paper's strongly Rayleigh group theorem and determinantal corollary.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Lyons and Peres, *Probability on Trees and Networks*](https://rdlyons.pages.iu.edu/prbtree/) (Cambridge University Press, 2016; online corrected edition). A standard monograph on uniform spanning forests and Wilson's algorithm rooted at infinity, background for the paper's discussion of the free and wired forests; it is not in the paper's bibliography.
- [Hutchcroft and Pete, *Kazhdan groups have cost 1*](https://arxiv.org/abs/1810.11015) (arXiv:1810.11015, Invent. Math. 2020). Timár cites it right after stating that the general FUSF factor question is open, in a discussion of fixed price; it may bear on the cost motivation of Lyons's 2013 question, which the paper cites.
- [Chen and Eldan, *Localization Schemes: A Framework for Proving Mixing Bounds for Markov Chains*](https://arxiv.org/abs/2203.04163v1) (arXiv:2203.04163, 2022). A general stochastic-localization framework related to the observation and posterior-drift mechanism that the paper adapts from Eldan, El Alaoui–Montanari and Nam–Sly–Zhang.

## Digests and expositions
- [Latent Seminar, *Sampling the free uniform spanning forest from IID labels*](https://lowrank.github.io/latent-seminar/OpenAI-Math/231-spanning-forest-factors) (6 October 2026). This exposition outlines the covariance response bound, Brownian innovations, deterministic inverse and equivariant allocation of edge noise, explicitly without independently verifying the complete proof.
- [Open Mathematics Courses, *The free uniform spanning forest*](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-free-uniform-spanning-forest/) (undated). Four lessons develop weighted trees, the free limit, tilted laws and the drift equation toward the manuscript's construction, but explicitly do not yet include the factor-of-IID theorem. [AI-generated per source]

## News and blogs
- None found.
