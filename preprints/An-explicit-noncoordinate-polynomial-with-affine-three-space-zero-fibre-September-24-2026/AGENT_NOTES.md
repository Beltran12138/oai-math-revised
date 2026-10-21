# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 049: A stable-coordinate counterexample in four variables*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/049.md) (release Lean docs, October 2026). Describes the formalized scope, including a noncoordinate F in ℂ[x_1,…,x_n] with quotient ≅ ℂ^[n-1] for every n ≥ 4, a companion statement on n−1 commuting locally nilpotent derivations, and the degree-five stable noncoordinate, with links to the three Comparator challenges; the three-variable case is not covered. [family-level]
- [OpenAI math release, *AbhyankarSathaye.lean* (comparator statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/AbhyankarSathaye.lean) (openai/math, October 2026). Lean statement `OAI.AbhyankarSathaye.exists_noncoordinate_polynomial` matching Corollary 1.2 (every n ≥ 4); the proof field in this statement file is `sorry`.
- [OpenAI math release, *StableCoordinateFour.lean* (comparator statement)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/StableCoordinateFour.lean) (openai/math, added in the 7 October 2026 update). Lean statement for the degree-five example of the 5 October companion paper, which strengthens this paper's zero-fibre result to all fibres; the proof field in this statement file is `sorry`. [family-level]

## Related prior literature mentioned by others
- [Shulim Kaliman, Stéphane Vénéreau and Mikhail Zaidenberg, *Simple birational extensions of the polynomial ring C^[3]*](https://arxiv.org/html/math/0104204v2) (arXiv:math/0104204v2, 2001). Math Referee's source assessment discusses Theorem 4.2(a) as background for the manuscript's restricted affirmative embedding results and separates that context from the internal construction; this work is already in the manuscript's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [Drew Lewis, *Venereau-type polynomials as potential counterexamples*](https://arxiv.org/abs/1007.2230) (arXiv:1007.2230; J. Pure Appl. Algebra 217 (2013)). Discusses Vénéreau-type polynomials as candidate counterexamples to the Abhyankar–Sathaye embedding conjecture, the conjecture this paper's Theorem 1.1 addresses in four variables.
- [Shulim Kaliman and Mikhail Zaidenberg, *Venereau polynomials and related fiber bundles*](https://arxiv.org/abs/math/0308191) (arXiv:math/0308191, 2003). Earlier four-variable candidates with affine three-space fibres, connected in its abstract to the Abhyankar–Sathaye embedding problem.
- [Vladimir L. Popov, *Around the Abhyankar–Sathaye conjecture*](https://arxiv.org/abs/1409.6330) (arXiv:1409.6330, 2014). Paper on the conjecture and on commuting locally nilpotent derivations, relevant both to Theorem 1.1 and to the derivation-theoretic interpretation via D = h∂_u − 3u²∂_v + 2u∂_w.
- [Parnashree Ghosh and Neena Gupta, *On the triviality of a family of linear hyperplanes*](https://arxiv.org/abs/2206.15210) (arXiv:2206.15210, 2022/2023). Affirmative Abhyankar–Sathaye results for linear hyperplanes x_1^{r_1}⋯x_m^{r_m}y = F, complementing the affirmative results by Ghosh–Gupta–Pal and Ghosh cited in the introduction.

## Digests and expositions
- [AI Proved What?, *One variable too few? A stable coordinate that is not a coordinate*](https://aiprovedwhat.com/episodes/049-stable-coordinate-counterexample-four-variables/) (episode 049, October 2026). This AI-assisted video and transcript explain both constructions, outline the October paper's filtration and derivation obstruction, and distinguish it from the September paper's critical-point argument. [AI-generated per source] [family-level]
- [Math Referee, *An explicit noncoordinate polynomial with affine three-space zero fibre — panel review*](https://mathreferee.dimensionreducers.ai/papers/noncoordinate-polynomial/panel/) (review, 2026-10-13). This AI-generated review reports no demonstrated error in four completed model assessments of the manuscript, records coverage qualifications and source checks, and states that human assessment remains pending. [AI-generated per source]
- [Math Referee, *Optional AI source assessment — noncoordinate polynomial*](https://mathreferee.dimensionreducers.ai/papers/noncoordinate-polynomial/source-audit/) (source assessment, 2026-10-13). This separate AI assessment details checks of the lifting lemma, quotient presentation, critical point and inverse maps, with reproducible symbolic calculations and explicit limits on its bibliography and formalization coverage. [AI-generated per source]

## News and blogs
- [Curtis Pyke, *One OpenAI Math Proof Target Passed Twice. Two Hit Our Memory Cap.*](https://kingy.ai/blog/openai-math-proof-test-local-memory-limit/) (Kingy AI, 2026-10-06). The post reports two successful local Comparator checks of `OAI.AbhyankarSathaye.exists_noncoordinate_polynomial`, provides public logs, and states that Codex operated the checks without human mathematical review of correspondence between the formal statement and manuscript.
