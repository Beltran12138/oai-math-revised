# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Kenta Kitamura (KitaKen1), *Lean proof of smooth isometric embeddings into four-space*](https://github.com/KitaKen1/smooth-isometric-embeddings-r4) (GitHub repository with manuscript "public draft 1", 9 October 2026). Claims to strengthen this paper's immersion result to a smooth isometric embedding of closed orientable surfaces in ℝ⁴, crediting the immersion result to OpenAI and providing a non-peer-reviewed Lean development with a self-reported Lean Comparator pass. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 333*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/333.md) (lean/docs/333.md). The scope note says the formalization proves that every closed smooth Riemannian surface admits a smooth isometric immersion into ℝ⁴, with no orientability assumption; the comparator statement is [SurfaceImmersion.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SurfaceImmersion.lean). [family-level]
- [KitaKen1, *Formalize smooth isometric embeddings of closed orientable surfaces in four-space and mark it as solved*](https://github.com/google-deepmind/formal-conjectures/pull/7211) (google-deepmind/formal-conjectures PR #7211, opened 12 October 2026; open at time of collection). Adds the closed orientable embedding strengthening to formal-conjectures as "research solved", linking the external Lean proof above and resolving [issue #7048](https://github.com/google-deepmind/formal-conjectures/issues/7048); a reviewer asks for proof certification in the formal-conjectures environment before merge.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Qing Han and Marta Lewicka, *Isometric immersions and applications*](https://arxiv.org/abs/2310.02566) (arXiv:2310.02566, October 2023; review for Notices of the AMS). Section 2.3 surveys the smallest target dimension (smooth embedding of compact surfaces in ℝ¹⁰ by Gromov and Günther, Poznyak's local version in ℝ⁴), giving context for the paper's comparison with Nash's dimension 17 and Gromov's ℝ⁵.
- [Deane Yang, *Gunther's proof of Nash's isometric embedding theorem*](https://arxiv.org/abs/math/9807169) (arXiv:math/9807169, July 1998). Exposition of Günther's proof, which avoids Nash–Moser iteration and improves the target dimension, relevant to the paper's dimension comparison and its remark that no global inverse of the linearized metric map is needed.
- [Qing Han and Jia-Xing Hong, *Isometric embedding of Riemannian manifolds in Euclidean spaces*](https://find.library.upatras.gr/Record/52369?lng=en) (AMS Mathematical Surveys and Monographs 130, 2006; library record). Standard monograph on local and global isometric embedding of surfaces, relevant to the paper's discussion of the Janet–Cartan local theory and its comparison with ℝ³.

## Digests and expositions
- [Latent Seminar, *Smooth isometric immersions of surfaces into four-space*](https://lowrank.github.io/latent-seminar/OpenAI-Math/333-smooth-surface-immersions-four-space) (expository article, 2026-10-07). Explains the manuscript's primitive metric additions, smooth correction iteration and preservation of normal geometry, stating that it does not independently verify the proof or audit the Lean development. [family-level]
- [Gradient Damage, *Every OpenAI Math Result, Part 4 of 4: L = BPL, Integer Multiplication and 82 More*](https://gradientdamage.com/videos/every-openai-math-result-part-4-of-4-l-bpl-integer-multiplication/) (video, 2026-10-14). Chapter 75, from 25:44, gives a brief illustrated introduction to the four-dimensional immersion result, with animations identified as illustrations rather than proofs. [family-level]

## News and blogs
- None found.
