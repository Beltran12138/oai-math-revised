# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Per Alexandersson, Lilan Dai, *Flip classes and elementary expansions of vertical-strip LLT polynomials*](https://arxiv.org/abs/2610.26294) (arXiv:2610.26294, 19 Oct 2026). Proves elementary positivity of flip-class sums for vertical-strip LLT polynomials; its introduction cites this paper's Theorem 1.1 as having proved that the elementary coefficients of the chromatic quasisymmetric function of every natural unit-interval graph lie in ℕ[q].

## Comments and discussion
- [Joshua P. Swanson, *Status of the Stanley–Stembridge conjecture*](https://mathoverflow.net/questions/481860/status-of-the-stanley-stembridge-conjecture/482378) (MathOverflow answer, update 2026-10-07). Swanson discusses OpenAI's Shareshian–Wachs paper, describes its exposition as opaque, and says its approach appears independent of Hikita's proof and the Griffin–Mellit–Romero–Weigl–Wen proof.

## Formalization
- [OpenAI, *Shareshian–Wachs elementary positivity: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/169.md) (OpenAI mathematics release, 2026-10-06). The scope note reports a formal elementary expansion over $\mathbb N[q]$, indexed by permitted nondescent permutations and weighted by graph inversions, for every finite number of color variables, and links the comparator statement.
- [OpenAI, *lean/ComparatorChallenges/ElementaryPositivity.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ElementaryPositivity.lean) (openai/math, 2026). Comparator statement: `elementaryPositivityWitness` returns a `PermutationWitness` (a partition `theta σ` per nondescent permutation and the expansion identity in `MvPolynomial (Fin r) (Polynomial ℕ)` for every `r`); the body is left as `sorry` for the comparator. Comparator challenge files leave the proof as `sorry` by design; `ElementaryPositivity.json` names the module `OAI.Combinatorics.Chromatic.Main` as the release's proof of this statement.
- [OpenAI, *lean/OAI/Combinatorics/Chromatic/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Chromatic/Main.lean) (openai/math, 2026). The release's construction of `elementaryPositivityWitness`, built from a finite-search table (`selectedTable`, `exists_successful_table`) in the `ElementaryPositivity` namespace.

## Related prior literature mentioned by others
- [Tatsuyuki Hikita, *A proof of the Stanley–Stembridge conjecture*](https://arxiv.org/abs/2410.12758) (arXiv:2410.12758, 2024-10-16; revised 2025-12-25). Swanson's discussion contrasts OpenAI's approach with Hikita's probabilistic formula, which establishes the Stanley–Stembridge specialization at $q=1$.
- [Sean T. Griffin, Anton Mellit, Marino Romero, Kevin Weigl and Joshua Jeishing Wen, *On Macdonald expansions of $q$-chromatic symmetric functions and the Stanley–Stembridge Conjecture*](https://arxiv.org/abs/2504.06936) (arXiv:2504.06936, 2025-04-09). This Macdonald-expansion proof rederives Hikita's formula and is the approach from which Swanson says OpenAI's argument appears independent.

## Possibly relevant literature (found by the agent, not checked)
- [Foster Tom, *A signed $e$-expansion of the chromatic quasisymmetric function*](https://arxiv.org/abs/2311.08020) (arXiv:2311.08020, 2023-11-14; revised 2024-05-08). Its signed elementary expansion for all natural unit interval graphs and sign-reversing involution for $K$-chains provide a comparison for the paper's positive permutation-indexed formula (Theorem 1.1) and the finite cancellation construction in Section 6.
- [Tatsuyuki Hikita, *(q,t)-chromatic symmetric functions*](https://arxiv.org/abs/2503.23597) (arXiv:2503.23597, 2025). Gives a probabilistic interpretation of the e-expansion coefficients used in Hikita's Stanley–Stembridge proof; relevant to the paper's discussion of Hikita's rational q-weights versus coefficientwise ℕ[q]-positivity.
- [Soojin Cho, Seonjeong Park, *Permutation module decomposition of the cohomology of Hessenberg varieties associated with lollipop graphs*](https://arxiv.org/abs/2607.03284) (arXiv:2607.03284, 3 Jul 2026). Constructs a permutation-module decomposition of Hessenberg cohomology (a Cho–Hong–Lee conjecture) for lollipop graphs; related to the paper's Corollary 1.2, which gives only an abstract isomorphism to sums of Young permutation modules.
- [Boris Kafidov, *Log-concavity of elementary coefficients for low-rank abelian Hessenberg graphs, with a counterexample in general*](https://arxiv.org/abs/2607.20595) (arXiv:2607.20595, Jul 2026). Studies unimodality/log-concavity of the elementary coefficients c_λ(q), the part of the Shareshian–Wachs conjecture the paper explicitly does not address.

## Digests and expositions
- [SymCat (symmetricfunctions.com), *Chromatic symmetric functions in the elementary basis*](https://www.symmetricfunctions.com/chromaticEexpansion.htm) (page dated 2026-10-07). Discusses the paper's Theorem 1.1 and Section 6, explaining that its permutation statistic uses auxiliary geometric choices and ordered finite matchings, and notes that the separate elementary-unimodality conjecture remains open.

## News and blogs
- None found.
