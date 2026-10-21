# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 220*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/220.md) (lean/docs/220.md, 2026). Describes the release's Lean formalization of Theorem 1.1 (iid uniformly elliptic ballisticity from almost-sure directional transience, d ≥ 2) and of the positive-probability and velocity-hemisphere conclusions in d ≥ 3 (Corollary 1.2), with the comparator statements `DirectionalBallisticity.lean` and `VelocityHemisphere.lean`. [family-level]
- [OpenAI math release, *Lean proof module `OAI/Probability/Ballisticity/Main.lean`*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/Ballisticity/Main.lean) (openai/math, commit adc7f12, 2026). Contains the theorem `OAI.DirectionalTransience.directional_transience_implies_ballisticity`, the Lean counterpart of Theorem 1.1; it reduces the statement to an imported unit-vector lemma.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Élodie Bouchet, *Sub-ballistic random walk in Dirichlet environment*](https://arxiv.org/abs/1205.5709) (arXiv:1205.5709, 2012). Studies directionally transient but sub-ballistic walks in (non-uniformly elliptic) Dirichlet environments in d ≥ 3, which bears on the uniform-ellipticity hypothesis of Theorem 1.1; it is cited in the companion zero–one paper but not here.
- [Alexander Drewitz and Alejandro F. Ramírez, *Ballisticity conditions for random walk in random environment*](https://arxiv.org/abs/0903.4465) (arXiv:0903.4465, 2009). Proves that (T)_γ is equivalent to (T') for γ above a dimension-dependent threshold, part of the quantitative-ballisticity literature reviewed in Section 1.2.
- [David Campos and Alejandro F. Ramírez, *Ellipticity criteria for ballistic behavior of random walks in random environment*](https://arxiv.org/abs/1212.4020) (arXiv:1212.4020; to appear in PTRF per arXiv). Extends Sznitman-type and polynomial ballisticity criteria beyond uniform ellipticity, which bears on whether the paper's uniform-ellipticity assumption could be relaxed.
- [Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walk in Random Environment*](https://arxiv.org/abs/1309.2589) (arXiv:1309.2589, 10 September 2013). The survey states the conjectured implication from directional transience to ballisticity for iid uniformly elliptic environments in d ≥ 2 and reviews renewal times and quantitative ballisticity conditions. [family-level]

## Digests and expositions
- [Gradient Damage, *Every OpenAI Math Result, Part 2 of 4*](https://gradientdamage.com/videos/every-openai-math-result-part-2-of-4-pcp-for-ppad-birkhoff-conjecture/) (video compilation, 2026-10-14). Chapter 51 ("Random Walk in Random Environment", at 17:20) summarizes result family 220, including the claimed resolution of the ballisticity conjecture. [family-level]

## News and blogs
- None found.
