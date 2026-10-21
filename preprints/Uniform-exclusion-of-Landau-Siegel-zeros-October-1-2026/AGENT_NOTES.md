# Automatically collected context

Collected by an AI agent (Claude Opus 5.5) on 2026-10-20.

## Follow-up works
- [William D. Banks, *On the OpenAI proof that Landau-Siegel zeros do not exist*](https://arxiv.org/abs/2610.15483) (arXiv:2610.15483, 2026-10-11). Gives a detailed direct proof of this paper's argument with explicit constants ((1−β)log q ≥ 3.0×10⁻³ for q ≥ 10¹⁰), extended to all q ≥ 3 via the computation of Lu–Zaman–Zhao.
- [Bryce Kerr, *A simpler proof that there are no Landau–Siegel zeros*](https://arxiv.org/abs/2610.21099) (arXiv:2610.21099, 2026-10-15). Presents a streamlined version of this paper's proof.
- [Ben Green, *On Landau–Siegel zeros*](https://hexagonmath.org/2610.00311v1) (hexagon:2610.00311, v1 2026-10-17, v2 2026-10-18). Gives a variant of this paper's argument (cited as its reference [3]); its provenance statement says the arguments are due to ChatGPT prompted by the author, with human-written text.
- [Terence Tao, *A sketch of the proof of non-existence of Siegel zeroes*](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/) (blog post, 2026-10-19). Expository sketch of the argument following Green's formulation, also mentioning the Banks and Kerr digestions and further unlinked preprints by Jacob Pescador and Kevin Barretto.

## Expert comments and discussion
- [Ben Green, comment on Tao's blog](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/#comment-698405) (2026-10-19). Reports having received separate 4-page and 3-page proofs (by Jacob Pescador and Kevin Barretto) and mentions a planned communal write-up.
- [Anurag Sahay and Terence Tao, comments on Tao's blog](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/#comment-698406) (2026-10-19). Sahay asks how the fixed choice of √2 relates to Deuring–Heilbronn-type biquadratic methods; Tao [replies](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/#comment-698407) that only the degree of the extension matters, not the choice of discriminant.
- [Kyle Pratt, comment on Tao's blog](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/#comment-698411) (2026-10-19). Compares the OpenAI/Kerr/Green arguments with Dobrowolski's method for height lower bounds.
- [Terence Tao, comment on his blog](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/#comment-698421) (2026-10-19). Describes the proof as a polynomial method related to Stepanov's method, with Masser's 1981 zero estimate as a key ingredient.
- [Hector Pasten, quoted in Scientific American](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (2026-10-08). Says the no-Siegel-zero result "settles the question" if correct.
- [Ben Green, quoted in the Proofs and Prompts reactions roundup](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (2026-10-08). Mentions "a second, short, proof of no Siegel zeros" alongside the 7/8 zero-free region.
- [Alex Kontorovich, X post as quoted in Zvi's LessWrong post](https://www.lesswrong.com/posts/eyqxBuxXCaamNSxBB/new-math-from-openai) (post 2026-10-06; roundup 2026-10-09). Reacts to the release noting "no Siegel zeros either" (the X post itself could not be opened by the agent).

## Formalization
- [OpenAI, Lean scope note for family 003](https://github.com/openai/math/blob/main/lean/docs/003.md) (openai/math, 2026-10). The comparator statement SiegelZeros.lean formalizes the uniform bound 1−β ≥ c/log q with an unspecified constant c.

## Related prior literature mentioned by others
- [Rick F. Lu, Asif Zaman, Haonan Zhao, *Numerical Computations Concerning Landau-Siegel Zeros*](https://arxiv.org/abs/2602.03626) (arXiv:2602.03626, 2026-02-03). Numerical verification up to modulus 10¹⁰, used by Banks to cover small conductors.
- [Masser (1981 zero estimate), Laurent (interpolating polynomials), Bombieri–Vaaler (Siegel's lemma), Stepanov's method, named in Tao's sketch](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/) (2026-10-19). Tao lists these as the classical tools the argument is related to.
- [whataifound.org entry comparing with Siegel (1935) and Yitang Zhang's 2022 preprint](https://whataifound.org/finding/2026-10-06-quasi-riemann-hypothesis) (2026-10-07). Notes the paper gives no explicit constant and contrasts it with Siegel's ineffective bound and Zhang's weaker claimed bound.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- None found.

## News and blogs
- [Peter Hall and Joseph Howlett, *The most exciting claims from OpenAI's heap of new proofs*, Scientific American](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (2026-10-08). News overview that covers the no-Siegel-zero claim.
