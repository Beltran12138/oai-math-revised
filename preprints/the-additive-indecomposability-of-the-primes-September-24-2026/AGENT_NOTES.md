# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Paolo Leonetti, *On the inverse Goldbach problem*](https://arxiv.org/abs/2610.15758) (arXiv:2610.15758, 11 Oct 2026). Proves upper and lower counting-function bounds for a hypothetical decomposition of the primes and a lower bound for ternary sumsets; its introduction cites this paper and says the claim "has not yet been verified by the math community."
- [Christian Elsholtz and Julia Stadlmann, *The large sieve inequality and additive decompositions of sums of squares*](https://arxiv.org/abs/2610.20554) (arXiv:2610.20554, 14 Oct 2026). Proves a large-sieve estimate for sets that miss residue classes modulo prime squares, applies it to sums of two squares, and notes that OpenAI "claimed a full resolution of Ostmann's problem"; the authors state that their work predates the claim.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Ostmann’s inverse Goldbach conjecture: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/013.md) (lean/docs/013.md). Reports formalization of the full infinite-symmetric-difference statement for two nontrivial subsets of the nonnegative integers and of the two-infinite-summands case, with comparator files `OstmannComplete.lean` and `OstmannPrimes.lean`.
- [google-deepmind/formal-conjectures, *FormalConjectures/ErdosProblems/431.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/431.lean) (formal-conjectures). States both the infinite-summands case and the full Ostmann statement, marked "research solved" and citing this paper; the theorem bodies are `sorry` and link to the Lean proofs in the openai/math repository.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures PR #6898, merged 11 Oct 2026). Marks Erdős 431 as solved and adds a proof link for the Ostmann variant; the review discussion does not address this problem. [family-level]
- [Shinsuke-Hamaji, *ostmann-proof-lean4*](https://github.com/Shinsuke-Hamaji/ostmann-proof-lean4) (GitHub repository, 2026). A third-party repository that describes itself as a Lean 4 verification of Ostmann's conjecture that is "overriding OpenAI's frozen Result 013"; its relation to the release's Lean code is not documented.

## Related prior literature mentioned by others
- [Terence Tao and Tamar Ziegler, *Infinite partial sumsets in the primes*](https://arxiv.org/abs/2301.10303) (arXiv:2301.10303, 2023). Cited on [erdosproblems.com/431](https://www.erdosproblems.com/431) as an unconditional construction of infinite sequences $A$ and $B$ with $a_i+b_j$ prime for $i<j$; this is a partial-sumset counterpart to the full-sumset statement proved here.
- [Andrew Granville, *A Note on Sums of Primes*](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/note-on-sums-of-primes/C310501E3CF2AEC4BBE5933855E394E1) (Canad. Math. Bull. 33(4), 1990). Cited on [erdosproblems.com/431](https://www.erdosproblems.com/431) as a conditional result under the prime $k$-tuples conjecture: an infinite sequence in which the average of any two terms is prime.
- [Ben J. Green and Adam J. Harper, *Inverse questions for the large sieve*](https://arxiv.org/abs/1311.6176) (arXiv:1311.6176, 2013-11-24). The [数学ビジュアライズ exposition](https://mathvis.sankakutech.com/posts/inverse-goldbach) discusses its conditional inverse-sieve route to Ostmann’s conjecture as background to the release paper’s claimed approach without a general quadratic classification.

## Possibly relevant literature (found by the agent, not checked)
- [Imre Z. Ruzsa, *Additive decomposition of signed primes*](https://arxiv.org/abs/2204.14013) (arXiv:2204.14013, 2022). Under the prime-tuple hypothesis, shows that the set of signed primes is a sumset; this is relevant to the paper's restriction to positive primes and summands in $\mathbb N_0$ (Theorem 1.1).

## Digests and expositions
- [数学ビジュアライズ, *OpenAIのAIが証明した「逆ゴールドバッハ予想」：素数は2つの集合の和に分けられない*](https://mathvis.sankakutech.com/posts/inverse-goldbach) (数学ビジュアライズ, 2026-10-12). This Japanese exposition presents sumset examples, residue restrictions, the finite-summand reduction, and an outline of the manuscript’s proof following its introduction.
- [Gradient Damage, *Ostmann’s Inverse Goldbach Conjecture: The Primes Aren’t A + B*](https://gradientdamage.com/videos/ostmanns-inverse-goldbach-conjecture-the-primes-arent-a-b/) (Gradient Damage, 2026-10-13). This short animation illustrates the claimed result through finite computations for two-element summands and explicitly distinguishes the illustration from a proof.

## News and blogs
- [Thomas Bloom, *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog, 8 Oct 2026). Has a section headed "Primes are not a sumset" that summarizes the claimed result as Problem 431, notes that the proof has been formalised, and says the PDF is 80 pages. [family-level]
- [OfficeChai Team, *OpenAI Has Also Included Proofs For 23 Erdos Problems In Its Latest Math Proof Drop*](https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/) (OfficeChai, 9 Oct 2026). Lists Problem 431 in one bullet as a proof of Ostmann's conjecture with a Lean formalisation.
