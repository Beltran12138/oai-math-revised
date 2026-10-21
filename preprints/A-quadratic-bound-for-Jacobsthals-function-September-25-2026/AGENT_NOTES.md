# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Matěj Kripner, Václav Rozhoň, Robert Šámal, Martin Šindelář and Adrián Zámečník, *Small witnesses for eventual Erdős–Straus binomial divisibility*](https://hexagonmath.org/pdf/2610.00239v1) (Hexagon:2610.00239v1, 2026-10-14). Section 1.3 cites the strengthened Jacobsthal bound when comparing polynomial coprimality sieves, and states explicitly that its proof uses no Jacobsthal estimate. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [mathcommunity/oai-math-revised, *Lean scope note for family 021*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/021.md) (release Lean docs, 2026). The scope note says the formalization proves the strengthened bound $h(k)\le Ck^2/(\log\log(3k))^2$ uniformly over positive moduli and signed interval starts, and keeps the quadratic bound as a separate statement.
- [OpenAI, *QuadraticBound.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean) (openai/math, commit adc7f12). Contains the release's theorem `erdos_970_quadratic` for the quadratic Jacobsthal bound.
- [google-deepmind/formal-conjectures, *ErdosProblems/970.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/970.lean#L30) (formal-conjectures, accessed 2026-10-21). States $h(k)\le Ck^2$ (`erdos_970`) and the iterated-log variant, marks both as research-solved with this paper as the source, and links to the release's Lean proofs; the proof bodies in this file are `sorry`.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures PR #6898, merged 2026-10-11). The batch PR that marked Erdős 970 solved and added the iterated-log variant with a formal-proof link. [family-level]
- [mo271, 30k30 et al., *GreensOpenProblems/46: green_46.improve_upper is answered by the improved Jacobsthal bound*](https://github.com/google-deepmind/formal-conjectures/issues/6908) (formal-conjectures issue #6908, 2026-10-07 to 2026-10-19). Argues via the Chinese remainder theorem that this paper's bound settles the upper-bound question in Green's Open Problem 46; a commenter reports a Lean formalization of that reduction depending only on the standard axioms.
- [30k30, bocowgill et al., *feat(GreensOpenProblems/46): mark green_46.improve_upper solved*](https://github.com/google-deepmind/formal-conjectures/pull/7183) (formal-conjectures PR #7183, merged 2026-10-19). Marks Green 46 `improve_upper` as solved with answer $(x+1)^2/(\log\log 3(x+1))^2$ from this paper; the contributor reports kernel replay of both Jacobsthal comparator challenges, while the reviewer notes they inspected the bridge statements but did not independently replay the full proof chain.
- [veljjanoski, *feat(ErdosProblems/687): add Erdős Problem 687*](https://github.com/google-deepmind/formal-conjectures/pull/6864) (formal-conjectures PR #6864, merged 2026-10-17). Adds Erdős 687 and marks part ii, $Y(x)=o(x^2)$, as research-solved through this paper's bound, with a `formal_proof` link to 30k30's derivation.
- [30k30, *erdos-687/glue/JacobsthalTo687.lean*](https://github.com/30k30/scholia/blob/b072c89c3edac06521868e32cc15b2bc91bd8533/erdos-687/glue/JacobsthalTo687.lean#L319) (30k30/scholia, commit b072c89). An independent Lean development that imports the release's `OAI.NumberTheory.Jacobsthal.Main` and uses the Chinese remainder theorem to derive $Y(x)=o(x^2)$ (Erdős 687 part ii) and the Green 46 upper-bound statement.
- [AItoBit, *erdos-687-quantitative-bound*](https://github.com/AItoBit/erdos-687-quantitative-bound) (GitHub, 2026). A Lean project that transfers a uniform quadratic Jacobsthal hypothesis to $Y(x)=O((x/\log x)^2)$ for Erdős 687; the README says the transfer builds, while plugging in the release's theorem is still pending. [AI-generated per source]

## Related prior literature mentioned by others
- [Alexander Kalmynin and Sergei Konyagin, *A polynomial analogue of Jacobsthal function*](https://arxiv.org/abs/2302.00459v2) (arXiv:2302.00459v2, 3 December 2023). Proves lower bounds for a polynomial version of Jacobsthal's function at products of primes below $y$; the Hexagon follow-up discusses it alongside this paper's interval bound.

## Possibly relevant literature (found by the agent, not checked)
- [M. Ziller, J. F. Morack, *Algorithmic concepts for the computation of Jacobsthal's function*](https://arxiv.org/abs/1611.03310) (arXiv:1611.03310, 2016/2017). Computes Jacobsthal's function of primorials for primes up to 251, complementing the computational results (Hajdu–Saradha, Costello–Watts, Ziller 2019) discussed in the introduction.

## Digests and expositions
- [Gradient Damage, *Jacobsthal’s Function: OpenAI Claims the Quadratic Bound*](https://gradientdamage.com/videos/jacobsthals-function-openai-claims-the-quadratic-bound/) (video exposition, 16 October 2026). A short animation illustrating covered runs for the first one to nine primes and describing the improvement over Iwaniec's bound; it identifies itself as an illustration rather than a proof.

## News and blogs
- [David H. Bailey, *OpenAI stuns mathematicians with 722 new papers*](https://mathscholar.org/2026/10/openai-stuns-mathematicians-with-722-new-papers/) (Math Scholar blog, 2026-10-07, updated 2026-10-19). Lists "Quadratic bound for Jacobsthal's function" among the release's highlights and states the bound $h(k)\ll k^2/(\log\log 3k)^2$, without further discussion. [family-level]
