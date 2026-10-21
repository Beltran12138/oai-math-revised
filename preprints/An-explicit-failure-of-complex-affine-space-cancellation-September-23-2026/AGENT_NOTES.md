# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [queelius (fork of piiiico/openai-math-counterexamples), *openai-math-counterexamples*](https://github.com/queelius/openai-math-counterexamples) (GitHub repository, accessed 2026-10-21). Its row 047 reports an independent exact-arithmetic recomputation of the identities in the stabilization step (the route to $A[w]\cong\mathbb C^{[5]}$) as "holds", and states that the non-polynomiality of $A$ (Sections 3–6) was not checked. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *lean/docs/047.md: Zariski cancellation and affine fibrations over the complex numbers (Lean scope note)*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/047.md) (OpenAI Math Release, 2026-10-06). The note says the Lean formalization covers the explicit four-dimensional cancellation counterexample (Theorem 1.1) but not the stable-coordinate consequence or the general line-bundle lifting statement. [family-level]
- [OpenAI, *lean/ComparatorChallenges/ComplexCancellation.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ComplexCancellation.lean) (openai/math, commit adc7f12). This is the comparator statement `MainStatement` for the explicit ring $A=\mathbb C[p,s,u,F,J]/(H)$: a finitely generated domain of Krull dimension 4 with $A[t]$ polynomial in 5 variables and $A$ not polynomial in 4 variables; as usual for comparator challenge statements, its proof is left as `sorry` in this file.
- [google-deepmind/formal-conjectures, *FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean) (formal-conjectures, 2026). The Zariski cancellation statement from Gupta's ICM survey is restated here as false in characteristic zero, with a variant `false_complex_four` for $\mathbb C^{[4]}$; both cite this paper, are tagged "research solved", and link to OpenAI's Lean development as `formal_proof`.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs* (PR #6898)](https://github.com/google-deepmind/formal-conjectures/pull/6898) (google-deepmind/formal-conjectures, opened 2026-10-07, merged 2026-10-11). This pull request marked Zariski cancellation as refuted ("false over ℂ, n = 4") and added the `false_complex_four` variant linked to the release's Lean proof; none of the visible review comments discuss this result. [family-level]

## Related prior literature mentioned by others
- [Neena Gupta, *The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry*](https://arxiv.org/abs/2208.14736) (arXiv:2208.14736, 2022-08-31). The AI Proved What? exposition links this survey for the characteristic-zero background to the claimed fourfold counterexample; it is also in the manuscript's bibliography.
- [Neena Gupta, *On Zariski's Cancellation Problem in positive characteristic*](https://arxiv.org/abs/1309.1368) (arXiv:1309.1368, 2013-09-05). The AI Proved What? exposition cites this earlier failure of cancellation in every dimension at least three in positive characteristic when explaining the paper's complex case; it is also in the manuscript's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [A. Dubouloz and P. Ghosh, *Algebraic families of higher dimensional $\mathbb A^1$-contractible affine varieties non-isomorphic to affine spaces*](https://arxiv.org/abs/2501.09613) (arXiv:2501.09613, January 2025). This paper builds characteristic-zero smooth $\mathbb A^1$-contractible varieties in every dimension $\ge 4$ that are not affine spaces, presented as candidate counterexamples to Zariski cancellation; this bears on the introduction's account of the characteristic-zero problem as open in dimensions $\ge 3$.
- [P. Ghosh and A. Pal, *A new family of counterexamples to the Zariski Cancellation Problem in positive characteristic*](https://arxiv.org/abs/2404.13803) (arXiv:2404.13803, April 2024). It gives a further positive-characteristic family of counterexamples in dimension $\ge 3$, distinct from Gupta's; the paper's history of positive-characteristic counterexamples cites only Asanuma and Gupta.
- [P. Das and A. K. Dutta, *A Note on Residual Variables of an Affine Fibration*](https://arxiv.org/abs/2002.02128) (arXiv:2002.02128; J. Pure Appl. Algebra 218 (2014), 1792–1799). It proves stable polynomiality over $R[W]$ for residual variables of affine fibrations over Noetherian domains, which relates to the residual-coordinate stabilization the paper takes from El Kahoui–Ouali and Dutta–Lahiri.
- [C. F. Venegas R. and H. J. Venegas R., *Cancellation problem via locally nilpotent derivations*](https://arxiv.org/abs/2512.15590) (arXiv:2512.15590, December 2025, revised February 2026). This survey covers locally nilpotent derivation and Makar-Limanov invariant methods for cancellation, the general technique the paper uses to show $A\not\cong\mathbb C^{[4]}$.

## Digests and expositions
- [AI Proved What?, *Cancel a line? Zariski cancellation over the complex numbers*](https://aiprovedwhat.com/episodes/047-zariski-cancellation-affine-fibrations-complex/) (episode 047, October 2026). This video and transcript outline the explicit equation, stabilization, degeneration and additive-action obstruction, and the claimed stable-coordinate and affine-fibration consequences. [AI-generated per source] [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, findings dated 2026-10-10). The report lists family 047's Dolgachev–Weisfeiler affine-fibration claims among conclusions broader than the formal statement checked in the release. [family-level]
