# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 7 Oct 2026). Lists the symmetric and general Mahler proofs with Hanner and simplex equality cases, links them to his earlier discussions of faces, flags and symplectic geometry, and says the results still need to be verified by human mathematicians. [family-level]

## Formalization
- [OpenAI math release, *Lean scope note for family 087*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/087.md) (lean/docs/087.md). States that the formalization proves $\inf_{z\in\mathrm{int}\,K}|K||(K-z)^\circ|\ge(n+1)^{n+1}/(n!)^2$ with equality exactly for simplices and excludes the functional inequality; another sentence of the same note says the nonsymmetric conjecture is not included. [family-level]
- [OpenAI math release, *Theorem.lean* (`general_mahler`)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/Convex/GeneralMahler/Theorem.lean) (openai/math, commit adc7f12). Lean statement of the sharp general inequality for compact convex bodies with nonempty interior, with equality exactly for simplices; the comparator challenge is `GeneralMahler.lean`.

## Related prior literature mentioned by others
- [Matthieu Fradelizi, Mathieu Meyer, Artem Zvavitch, *Volume Product*](https://arxiv.org/abs/2301.06131) (arXiv:2301.06131, Jan 2023). Survey of the general (Santaló-point) volume product and its known special cases, used by Agentic Economy's Mahler article for the history and definitions behind the symmetric and general claims. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090) (arXiv:2610.17090, 12 Oct 2026). Its family-087 card (Section 8.2.2) records that the general-body argument relies on about twenty selected decimal constants and SymPy certificates, and that its initial inspection found symmetric Lean coverage only. [family-level] [AI-generated per source]
- [OpenAI Math Digest, *The Mahler Conjecture for General Convex Bodies*](https://masataka123.github.io/OpenAI-Math-Digest/ja/papers/general-mahler/) (Japanese exposition, undated). Reading guide tracing the dual-cone Laplace reduction, Gaussian projections, matrix comparison and simplex rigidity, noting that full certificate recomputation and independent verification remain incomplete. [AI-generated per source]

## News and blogs
- [Agentic Economy, *OpenAI's Mahler claim: the route through an 87-year-old problem*](https://aecon.ai/blog/openai-mahler-volume-product) (aecon.ai, 8 Oct 2026). Contrasts the symmetric and general proof strategies, their equality classifications and the released reasoning summary, without claiming independent proof certification. [family-level]
