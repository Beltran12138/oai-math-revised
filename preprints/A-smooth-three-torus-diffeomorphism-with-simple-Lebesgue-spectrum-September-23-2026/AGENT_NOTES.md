# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Banach’s simple Lebesgue-spectrum problem: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/144.md) (lean/docs/144.md, OpenAI Math Release, 6 October 2026). The release's scope note says the Lean development constructs the smooth volume-preserving three-torus diffeomorphism, gives a real cyclic vector whose iterates form an orthonormal basis of the mean-zero space, provides the unitary model as multiplication by the coordinate on the circle, and proves ergodicity. [AI-generated per source]
- [OpenAI math release, *ThreeTorus.lean* (comparator challenge statement)](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ThreeTorus.lean) (lean/ComparatorChallenges, 2026). This is the comparator statement `ThreeTorus.simple_lebesgue_spectrum`, left as `sorry` in this file by design: smooth `T` with smooth inverse, Haar measure preservation, ergodicity, a real mean-zero `f` with orthonormal iterates spanning a dense subspace of `H₀`, and a unitary model in which the Koopman operator becomes multiplication by the first character.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [el Houcein el Abdalaoui, *$L^1$-flat polynomials and simple Lebesgue spectrum for conservative maps exist: A simple proof*](https://arxiv.org/abs/2210.15480) (arXiv:2210.15480, Oct 2022, rev. Jun 2023). This gives a conservative ergodic map and flow with simple Lebesgue spectrum, a companion to the infinite-measure result the paper cites from arXiv:1508.06439v8 (Theorem 2.2), which the paper says does not imply the probability-space conclusion.
- [Valery V. Ryzhikov, *Spectral properties of dynamical tensor powers, and tensor factorizations of simple Lebesgue spectrum*](https://arxiv.org/abs/2406.08409) (arXiv:2406.08409, Jun 2024). Its text calls the question "is there an automorphism with simple Lebesgue spectrum?" Banach's problem and treats the probability-space case separately, the formulation Theorem 1.1 addresses.
- [Valery V. Ryzhikov, *Unsolved problems on joinings, multiple mixing, spectrum, and rank*](https://arxiv.org/abs/2405.03641) (arXiv:2405.03641, May 2024). This survey links a hypothetical simple Lebesgue-spectrum automorphism to "the problems of Banach, Rokhlin and del Junco-Rudolph", which is relevant to the mixing consequences derived in Section 6.
- [A. A. Prikhod'ko, *On group actions with simple Lebesgue spectrum*](https://arxiv.org/abs/1111.0230) (arXiv:1111.0230, Nov 2011). This constructs measure-preserving $\mathbb R^d$-actions with simple Lebesgue spectrum, which relates to the introduction's comparison with continuous-time results (it cites Prikhod'ko's 2020 flow paper but not this one).
- [Bassam Fayad, Anatole Katok, *Constructions in elliptic dynamics*](https://arxiv.org/abs/math/0501362) (arXiv:math/0501362, Jan 2005; Ergodic Theory Dynam. Systems 24 (2004)). This is a survey of the Anosov–Katok approximation-by-conjugation method, which the introduction names as background for its successive smooth coordinate changes.

## Digests and expositions
- [AI Proved What?, *One signal, every pattern? A smooth three-torus map with simple Lebesgue spectrum*](https://aiprovedwhat.com/episodes/144-simple-lebesgue-spectrum/) (episode 144, October 2026). This illustrated exposition and transcript explain the claimed spectral model and the twist, passage, density-bias, whitening, and diagonal-limit construction, with numerical illustrations and a statement that its authors have not run the Lean check. [AI-generated per source]
- [Gradient Damage, *Birkhoff Conjecture, Zero Entropy and 7 More in Dynamical Systems and Ergodic Theory*](https://gradientdamage.com/videos/birkhoff-conjecture-zero-entropy-and-7-more-in-dynamical-systems/) (video and accompanying post, 15 October 2026). The opening chapter, at 0:00–0:21, introduces Banach’s probability-preserving spectrum problem and the release’s claim, linking this manuscript.

## News and blogs
- [Tom Whipple / BBC Inside Science, *The future of mathematics in the age of AI*](https://podscan.fm/podcasts/bbc-inside-science/episodes/the-future-of-mathematics-in-the-age-of-ai) (BBC Radio 4; public episode description and transcript on Podscan, 8 October 2026). The episode description names Banach’s simple Lebesgue-spectrum problem among the release’s claims, without a technical assessment of this manuscript.
