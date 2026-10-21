# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Kenta Kitamura, *centered-ball-maximal-endpoint*](https://github.com/KitaKen1/centered-ball-maximal-endpoint) (GitHub repository, October 2026). Proposes a Lean 4 proof of the centered Euclidean-ball endpoint gradient bound in every dimension, citing this paper as "a research starting point"; the repository says independent mathematical review is still pending. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for 085 (Endpoint Sobolev regularity of centered disk averages)*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/085.md) (release Lean docs, 2026-10-06). Describes the formalizations of the signed finite-band estimate and the full planar Sobolev-input endpoint gradient bound, with links to their comparator statements; a BV-input extension is explicitly outside its scope. [family-level]
- [OpenAI math release, *DiskMaximal.lean comparator statement*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/DiskMaximal.lean) (openai/math, commit adc7f12). The Lean statement `OAI.CenteredDiskEndpoint.main_endpoint` gives the endpoint bound for integrable planar f with integrable weak gradient.
- [Kenta Kitamura, *Add a conjecture: endpoint gradient bound for the centered ball maximal operator in every dimension*](https://github.com/google-deepmind/formal-conjectures/issues/6938) (google-deepmind/formal-conjectures issue #6938, 2026-10-08). Proposes adding the d ≥ 2 centered-ball version of Hajłasz–Onninen Question 1 to formal-conjectures; the issue itself does not mention this paper. [AI-generated per source]
- [Kenta Kitamura, *Formalize the centered ball maximal endpoint and mark it as solved*](https://github.com/google-deepmind/formal-conjectures/pull/7129) (google-deepmind/formal-conjectures PR #7129, opened 2026-10-11, open at time of collection). Formalizes Hajłasz–Onninen Question 1 for centered balls and links external Lean proofs, which a reviewer reports rebuilding with Lean 4.33.1 and passing the Comparator checks. [AI-generated per source]

## Related prior literature mentioned by others
- [Piotr Hajłasz and Jani Onninen, *On boundedness of maximal functions in Sobolev spaces*](https://afm.journal.fi/article/view/135096) (Ann. Acad. Sci. Fenn. Math. 29 (2004)). The source of Question 1, which the follow-up repository, the formal-conjectures issue and the PR all take as their target statement; it is also in the paper's bibliography.
- [Panu Lahti and Julian Weigt, *The centered maximal operator removes the non-concave Cantor part from the gradient*](https://arxiv.org/abs/2510.01936v1) (arXiv:2510.01936v1, 2025-10-02). The AI Proved What? exposition highlights this work's conditional upgrade from BV to Sobolev regularity in connection with the manuscript's separate variation-bound and singular-part-removal steps.

## Possibly relevant literature (found by the agent, not checked)
- [Emanuel Carneiro, *Regularity of maximal operators: recent progress and some open problems*](https://arxiv.org/abs/1912.04625) (arXiv:1912.04625, 2019). A survey with fifteen open problems in this area; relevant to the paper's account of the status of the Hajłasz–Onninen endpoint question and earlier endpoint results.
- [Emanuel Carneiro and Cristian González-Riquelme, *Gradient bounds for radial maximal functions*](https://arxiv.org/abs/1906.01487) (arXiv:1906.01487; Ann. Fenn. Math. 46 (2021)). Proves W^{1,1} gradient bounds for centered heat-flow and Poisson maximal operators on radial data in ℝ^d, a higher-dimensional centered endpoint result not listed in the paper's "Earlier endpoint results" subsection.
- [Panu Lahti, *On the regularity of the maximal function of a BV function*](https://arxiv.org/abs/2007.05752) (arXiv:2007.05752, 2020). Shows that if the non-centered maximal function of an SBV function is BV, then it is Sobolev, which bears on the paper's final step removing the singular part of the derivative measure of Mf.
- [Emanuel Carneiro and Julian Weigt, *On the variation and asymptotics of maximal functions*](https://arxiv.org/abs/2610.18544) (arXiv:2610.18544, 2026-10-13). A later paper on the variation of centered convolution-type maximal operators in higher dimensions; its introduction calls the Hajłasz–Onninen question generally open in higher dimensions and does not mention this paper.

## Digests and expositions
- [Latent Seminar, *Endpoint gradients of the centered disk maximal function*](https://lowrank.github.io/latent-seminar/OpenAI-Math/085-centered-maximal-gradient) (2026-10-06). A graduate-level exposition outlining the signed finite-band estimate, disk-moment cancellation, multiscale accounting and removal of singular derivatives; it disclaims independent proof verification or a Lean audit. [family-level]
- [AI Proved What?, *How much steeper? The centered disk maximal function at p = 1*](https://aiprovedwhat.com/episodes/085-endpoint-sobolev-regularity-centered-disk/) (Episode 085, October 2026). An animated exposition and transcript illustrating the endpoint claim with cone-function computations and outlining the proof strategy; it states that the project has not run the Lean check. [AI-generated per source] [family-level]

## News and blogs
- None found.
