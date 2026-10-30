# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- None found.

## Comments and discussion
- [Tasmin Chu, reaction in *100+ reactions to 100+ solutions*, Proofs and Prompts](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (blog post of 2026-10-08, reactions updated to 2026-10-19). Recalls the 1996 Benjamini–Schramm conjecture and remarks: "Unsurprisingly the OpenAI preprint builds on work of my advisor Tom Hutchcroft", also describing the preprint's impact on Chu's own research plans.
- [Inhyeok Choi, reaction in *100+ reactions to 100+ solutions*, Proofs and Prompts](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (2026-10-08). Choi, co-author of the cited Choi–Seo paper on acylindrically hyperbolic groups, says they had thought about the $p_c<p_u$ question and asks "whether there is a more natural proof for groups with free subgroups."

## Formalization
- [OpenAI math release, *The Benjamini–Schramm nonuniqueness conjecture: Lean scope note* (lean/docs/214.md), mirrored on github.com/mathcommunity/oai-math-revised](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/214.md) (release of 2026-10-06). Describes the release's own Lean formalization of $p_c<p_{2\to2}\le p_u$, the coupled nonuniqueness interval, the arbitrary-generating-set Cayley-graph corollary and selected critical and exponential-connectivity estimates, with comparator files `BenjaminiSchramm.lean` and `CayleyPercolation.lean`. [family-level]
- [MathVet, *Formalization fidelity assessment for family 214*](https://raw.githubusercontent.com/mathvet/mathvet/main/reviews/openai-math/fidelity-table.csv) (assessment of release commit fd4aeeb2, accessed 2026-10-30). Records a sandboxed Comparator pass and a preliminary model-assisted assessment that the Lean statements cover the operator gap, coupled nonuniqueness interval, critical laws and arbitrary-generating-set Cayley case, explicitly examining the custom isoperimetric and Følner definitions; the project's assessments await named human refereeing. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [Tom Hutchcroft, *The $L^2$ boundedness condition in nonamenable percolation*](https://arxiv.org/abs/1904.05804) (arXiv:1904.05804, 2019; revised 2020-09-23). Linked by the BinaryVerse AI article to explain how the operator condition yields more than nonuniqueness, including exponential connectivity and critical-radius estimates; also in the paper's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [Russell Lyons, *Fixed price of groups and percolation*](https://arxiv.org/abs/1109.5418) (arXiv:1109.5418; Ergodic Theory Dynam. Systems 33 (2013) 183–185). Shows that a finitely generated group either has fixed price or every one of its Cayley graphs has a Bernoulli percolation phase with infinitely many infinite clusters, an earlier all-generating-sets result relevant to Corollary 1.2 (arbitrary Cayley graphs).
- [Zhongyang Li, *Tree embeddings and nonuniqueness in site percolation*](https://arxiv.org/abs/2304.00923) (arXiv:2304.00923, v7 2026-07-05). Proves nonuniqueness for Bernoulli site percolation on properly embedded planar graphs of minimum degree at least 7; relevant since Benjamini–Schramm's standing model is site percolation, while Theorem 1.1 concerns bond percolation.
- [Tom Hutchcroft and Minghao Pan, *Percolation at the uniqueness threshold via subgroup relativization*](https://arxiv.org/abs/2409.12283) (arXiv:2409.12283, 2024-09-18). Its nonuniqueness results at $p_u$ for specific nonamenable groups give endpoint context for Theorem 1.1's strict gap $p_c<p_u$, which does not itself determine the cluster count at $p_u$.
- [Yucheng Liu, Leonardo T. Rolla and Yuliang Shi, *Percolation on Bidirected Graphs*](https://arxiv.org/abs/2610.28762) (arXiv:2610.28762, 2026-10-20). Its Theorem 1.12 gives $p_c<p_{\mathrm{sc}}$ on transitive graphs when $p_c<p_\triangle$ and $\triangle_{p_c}<1$, and it describes the stronger inequality $p_c<p_{2\to2}$ as conjectural, which is the operator-threshold statement of Theorem 1.1 here; it does not cite this manuscript.

## Digests and expositions
- [Latent Seminar, *Nonamenable percolation and the two-point operator*](https://lowrank.github.io/latent-seminar/OpenAI-Math/214-nonamenable-percolation) (2026-10-06). Exposition of the connection operator, corridor deformation, spectral contradiction and simultaneous coupling argument; it states that it does not independently verify the complete proofs or audit the Lean development. [family-level]

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 2026-10-07). Item 20 ("Percolation: criticality and nonuniqueness") lists the release's claim of $p_c<p_u$ for nonamenable quasi-transitive graphs and links Kalai's 2009 discussion of the Benjamini–Schramm conjecture.
- [Azmat, *Benjamini–Schramm Nonuniqueness Conjecture: OpenAI Proof Cracks the 30-Year Mystery of Infinite Clusters*](https://binaryverseai.com/benjamini-schramm-nonuniqueness-conjecture/) (BinaryVerse AI, 2026-10-14). Describes the paper's graph hypotheses, operator gap, proof strategy and critical-law consequences, distinguishing the asserted interval from behavior exactly at $p_u$.
