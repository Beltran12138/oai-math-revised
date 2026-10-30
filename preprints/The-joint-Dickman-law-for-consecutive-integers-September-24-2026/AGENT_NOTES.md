# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Ji Ho Bae (jbaelaw), *Erdos928*](https://github.com/jbaelaw/Erdos928) (GitHub repository, Lean 4/Mathlib, accessed 2026-10-21). Formalizes in Lean a counting estimate and an explicit implication from the joint Dickman law of this paper to Erdős Problem 928; it explicitly does not re-prove or import the paper's analytic theorem. [AI-generated per source]

## Comments and discussion
- [Thomas Bloom, *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog, 8 Oct 2026). Lists Problem 371 among the release's claimed results, notes that the 84-page PDF proves it as a corollary of a more general joint distribution law and that a Lean formalisation exists, and says he had not checked the proofs or formalisations himself. [family-level]

## Formalization
- [OpenAI math release, *lean/docs/012.md* (scope notes, mirrored)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/012.md) (oai-math-revised, 2026). The release's own scope note: Lean proofs of the joint Dickman law in natural density for $0<a,b<1$ and of density $1/2$ for each ordering, with comparator statement `JointDickman.lean`. [family-level]
- [OpenAI, *PaperMain.lean* (OAI.JointDickmanPaper)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/JointDickman/PaperMain.lean) (openai/math, commit adc7f12). States `joint_law` (Theorem 1), `increasing_order` (Corollary 2) and `decreasing_order`, with proofs imported from `JointDickman.UnconditionalMain`.
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/371.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/371.lean) (formal-conjectures, accessed 2026-10-21). Formal statement of Erdős Problem 371 (density $1/2$ for $P(n+1)>P(n)$, via `Nat.maxPrimeFac` and `HasDensity`), tagged as research-solved and linked to the OpenAI Lean proof; the proof body in this repository is still `sorry`.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs* (PR #6898)](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures, merged 11 Oct 2026). Marks Erdős 371 as solved; the PR notes that the linked proof differs from the repository statement by a routine transport ("density over Icc 2 ⌊X⌋ vs Iio b") that the linked proof does not contain. [family-level]

## Related prior literature mentioned by others
- [Zhiyuan Yang, *Convolution-type Bombieri-Vinogradov theorem with well-factorable weights, and its applications*](https://arxiv.org/abs/2608.13299) (arXiv:2608.13299, Aug 2026, v2 Sep 2026). Proves the lower bound $0.299x$ for $\#\{n\le x:P^+(n)<P^+(n+1)\}$, improving the 0.280 of Yang2026 cited in the paper. The [erdosproblems.com thread for Problem 371](https://www.erdosproblems.com/forum/thread/371) points to it, but the paper's bibliography does not.

## Possibly relevant literature (found by the agent, not checked)
- [Zhiyuan Yang, *Note on the largest prime factors of consecutive integers*](https://arxiv.org/abs/2610.23280) (arXiv:2610.23280, 16 Oct 2026). Gives an alternative proof of the Tao–Teräväinen positive-proportion results on patterns of $P^+$ at consecutive integers, discussed in the paper's "Previous work" section, and a lower bound $\gg x/\log x$ for $P^+(n+1)/P^+(n)\in[1,1+\varepsilon)$; it does not cite the release.
- [Zhiyuan Yang, *On the largest prime factors less than $y$ of consecutive shifted primes*](https://arxiv.org/abs/2609.15166) (arXiv:2609.15166, v1 14 Sep 2026, v2 29 Oct 2026). With $P_y^+(n)$ the largest prime factor of $n$ not exceeding $y$, proves $\#\{n\le x:P_y^+(n)<P_y^+(n+1)\}\sim x/2$ for $3\le y\ll x^{o(1)}$, a truncated analogue of Corollary 1.2; v2 still states the untruncated density $1/2$ as Conjecture 1.1, and its bibliography does not cite the release.

## Digests and expositions
- [eigendash, *openai-math-visualised*](https://github.com/eigendash/openai-math-visualised) (GitHub repository, accessed 2026-10-21). Includes a numerical probe of family 012 up to $6\times10^7$: the density of $P^+(n)<P^+(n+1)$ is reported as 0.499983, with a comparison of the binned joint distribution against the product of Dickman marginals.
- [Bogdan Grechuk, *Prime Factors of Consecutive Integers*](https://functor.network/user/3333/entry/2037) (Functor Network, 2026-10-28). Places the claimed ordinary-density law against earlier logarithmic and almost-all-scales results, explains the density-one-half deduction, and sketches the reduction through weighted factorizations to short-interval estimates.

## News and blogs
- None found.
