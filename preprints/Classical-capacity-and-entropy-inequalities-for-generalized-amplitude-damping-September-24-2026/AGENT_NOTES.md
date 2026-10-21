# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Kun Fang, *The classical capacity of generalized amplitude-damping channels and its strong-converse exponent*](https://arxiv.org/abs/2609.14621) (arXiv:2609.14621v2, 6 Oct 2026). Revised and retitled version of the converse-bound preprint cited by this paper as [Fang2026]; v2 independently states that the capacity of all generalized amplitude-damping channels equals the one-copy Holevo information and adds the exact strong-converse exponent. Its acknowledgments say OpenAI GPT-6 Astra was used to explore proof strategies; it does not cite the OpenAI release.
- [Kenta Kitamura (GitHub: KitaKen1), *qubit-strong-additivity*](https://github.com/KitaKen1/qubit-strong-additivity) (GitHub repository, Lean v4.34.1, draft of 11 Oct 2026). Claims, with a Lean proof, strong Holevo additivity for every qubit-to-qubit channel with any finite-dimensional partner, which would include the Holevo part of this paper's partner-additivity corollary; it lists Fang (2026) and OpenAI (2026) as earlier results for generalized amplitude damping. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, Lean scope note for family 276](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/276.md) (lean/docs/276.md, 6 Oct 2026). The note says the Lean development covers Holevo additivity over all tensor powers, the attained scalar maximum, operational capacity, and attainment by phase-pair product ensembles, while excluding partner-channel additivity and decoding by separate measurements. [family-level]
- [OpenAI math release, comparator statement *AmplitudeDamping.lean*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/AmplitudeDamping.lean) (lean/ComparatorChallenges). Lean statement of the main theorem: the n-use Holevo value is n times the one-use value and equals the scalar maximum, capacity equals the one-use Holevo value, and phase-pair ensembles attain it.
- [QuAIR group, *Classical-Capacity-Qubit-Amplitude-Damping*](https://github.com/QuAIR/Classical-Capacity-Qubit-Amplitude-Damping) (GitHub repository, Lean 4 + Lean-QIT). Lean formalization of the cited Tang–Zhu–Bai–Wang manuscript, covering the zero-temperature (ordinary amplitude-damping) case and the matrix entropy inequalities that this paper extends to the thermal case.

## Related prior literature mentioned by others
- [Z. Tang, C. Zhu, G. Bai, X. Wang, *Classical Capacity and Entanglement Cost of the Amplitude Damping Channel*](https://arxiv.org/abs/2609.28592) (arXiv:2609.28592, 23 Sep 2026). Fang's v2 says its norm-compression proof extends this paper's log-determinant method; also cited in this paper as [TangEtAl2026].

## Possibly relevant literature (found by the agent, not checked)
- [V. Siddhu, A. Chatterjee, K. Jagannathan, P. Mandayam, S. Tayur, *Queue-Channel Capacities with Generalized Amplitude Damping*](https://arxiv.org/abs/2107.13486) (arXiv:2107.13486, 2021). Derives the exact classical capacity of the symmetric generalized amplitude-damping channel (ν = 1/2), relevant to the paper's discussion of the unital point.
- [Stefano Pirandola, *Exact series formulas for the capacities of the amplitude damping channel*](https://arxiv.org/html/2609.31609v1) (arXiv:2609.31609v1, 25 September 2026). Gives a convergent series for the unassisted classical capacity in the ordinary amplitude-damping boundary case of this paper's scalar optimization, with AI-assisted derivations disclosed by the author.

## Digests and expositions
- [Open Mathematics Courses, *Classical capacity of generalized amplitude damping*](https://kokunoyumeto.github.io/open-math-courses-public/courses/classical-capacity-of-generalized-amplitude-damping/) (undated). Five-lesson exposition of the manuscript's log-determinant and block-entropy argument through tensor-power and arbitrary-partner additivity, treating the classical coding theorem as a named hypothesis and stating that independent review is incomplete. [AI-generated per source] [family-level]

## News and blogs
- [r/accelerate, *Most Impactful Math Discoveries from OpenAI's Oct. 6 Math Release*](https://www.reddit.com/r/accelerate/comments/1wzh3ij/most_impactful_math_discoveries_from_openais_oct/) (Reddit, October 2026). Post discussing family 276's capacity claim and possible relevance to noisy quantum communication, disclosing that ChatGPT supplied most of its explanations. [AI-generated per source] [family-level]
