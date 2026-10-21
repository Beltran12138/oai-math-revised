# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 322: Tingley’s sphere-isometry problem*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/322.md) (lean/docs/322.md, release scope note, 2026). The release's own scope note says the formalized result gives a unique surjective real-linear isometric extension for arbitrary nonzero real Banach spaces, with real (not complex) linearity in the complex case, and links the comparator statement. [family-level]
- [OpenAI, *TingleySphereIsometry.lean* (comparator statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/TingleySphereIsometry.lean) (openai/math, commit adc7f12). The comparator statement `OAI.Tingley.tingley_sphere_isometry_full` asserts a `X ≃ₗᵢ[ℝ] Y` agreeing with f on the sphere, given by the radial formula, and unique among real-linear extensions; the comparator file itself leaves the proof as `sorry`.
- [OpenAI, *Extension.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/SphereIsometry/Extension.lean) (openai/math, `lean/OAI/Analysis/SphereIsometry/`). This file contains the proof of `tingley_sphere_isometry_full`, assembled from imported modules such as `DefectAttainment` and `ChordContradiction`; the full dependency chain was not checked or rebuilt.
- [anxkhn, *Add Tingley's sphere-isometry extension theorem*](https://github.com/google-deepmind/formal-conjectures/issues/6983) (google-deepmind/formal-conjectures issue #6983, 2026-10-08). Proposes adding the existence part of Theorem 1.1 as a statement and notes that the radial formula and uniqueness follow from linearity and agreement on the sphere.
- [anxkhn, *feat(Paper): add Tingley's sphere-isometry theorem*](https://github.com/google-deepmind/formal-conjectures/pull/6988) (google-deepmind/formal-conjectures PR #6988, opened 2026-10-08, open as of 2026-10-21). Adds a Lean statement only, without a proof or `formal_proof` attribute; a reviewer (bocowgill) approved it on 2026-10-10 after checking the statement against Theorem 1.1, and the PR author reports AI assistance (OpenCode).

## Related prior literature mentioned by others
- [Gabriele Darbo, *Punti uniti in trasformazioni a codominio non compatto*](https://www.numdam.org/item/RSMUP_1955__24__84_0/) (Rendiconti del Seminario Matematico della Università di Padova 24, 84–92, 1955). The Exact Mathematics with AI exposition identifies Darbo’s fixed-point theorem as the classical tool used to obtain aligned extremal chords; the reference is also in the paper's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [V. Kadets and M. Martín, *Extension of isometries between unit spheres of finite-dimensional polyhedral Banach spaces*](https://arxiv.org/abs/1206.4839) (arXiv:1206.4839; J. Math. Anal. Appl. 2012). A positive answer to Tingley's problem for finite-dimensional polyhedral spaces, a special case of Theorem 1.1; not cited in the bibliography, which lists other finite-dimensional results (Tingley, Banakh).
- [A. M. Peralta, *A survey on Tingley's problem for operator algebras*](https://arxiv.org/abs/1801.02473) (arXiv:1801.02473, 2018). Surveys the operator-algebra and facial-structure programme that the introduction summarizes through Fernández-Polo–Peralta, Mori and Mori–Ozawa; not in the bibliography.
- [J. Nakamura and R. Tanaka, *Rigidity of unit spheres in finite-dimensional real normed spaces*](https://arxiv.org/abs/2609.31096) (arXiv:2609.31096, 2026-09-25). Shows that finite-dimensional real normed spaces with isometric unit spheres are linearly isometric (a question of Kadets and Martín), the "object-level" consequence the release's family summary draws from Theorem 1.1; the preprint does not mention the OpenAI paper.
- [K. Kudaybergenov, M. Ibragimov and A. Arziev, *Isometries of Unit Spheres of SFS-Spaces and a Geometric Approach to Tingley's Problem*](https://arxiv.org/abs/2610.19626) (arXiv:2610.19626, 2026-10-14). Proves a positive answer for finite-dimensional real neutral strongly facially symmetric spaces with the joint Peirce property, cases within the scope of Theorem 1.1; the preprint does not mention the OpenAI paper.

## Digests and expositions
- [Exact Mathematics with AI (publication responsibility: Ryotaro Tanaka), *A reader’s reconstruction of the chord argument for Tingley’s problem*](https://exactmathematics.org/topics/tingley-chord-argument/) (Expository Note, version 1, 2026-10-14). This 21-page reconstruction develops the convex invariant-set construction and chord-coordinate comparison, attributes the argument to the September 23 manuscript, and explicitly disclaims independent human proof review or Lean formalization. [AI-generated per source]
- [Open Mathematics Courses, *Tingley’s problem*](https://kokunoyumeto.github.io/open-math-courses-public/courses/tingleys-problem/) (online course, undated). Four lessons with proofs, examples and solved exercises explain the manuscript’s radial-defect, ultrapower and Darbo arguments; the source credits Claude Opus 5.5 with writing and self-checking and says independent review is incomplete. [AI-generated per source]
- [Latent Seminar, *Tingley’s sphere-isometry extension*](https://lowrank.github.io/latent-seminar/OpenAI-Math/322-tingley-sphere-isometries) (2026-10-06). Outlines defect attainment, the return-map noncompactness estimate and the final chord contradiction, explicitly limiting its review to statements, introductions and selected proof mechanisms. [family-level]

## News and blogs
- None found.
