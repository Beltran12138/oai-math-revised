# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Thomas Bloom, *Erdős problems in the OpenAI proofs*, with comment thread (MalekZ, jleng01, Thomas Bloom)](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog and forum, 8–12 Oct 2026). Bloom summarizes the claimed bound for all k ≥ 3, notes that a bound of this shape was already known for k=3 (Kelley–Meka), and says the Lean code "appears to prove the weaker bound" exp(-(log log N)^{1+c_k})N. In the comments, jleng01 calls the proof "largely a synthesis of previous work on the problem," and Bloom agrees that it shows existing techniques "pushed sufficiently far" suffice.

## Formalization
- [OpenAI, *Erdős’s reciprocal-sum conjecture and quasipolynomial Szemerédi bounds: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/159.md) (lean/docs/159.md, 6 October 2026). States that the formalization proves the reciprocal-sum corollary (progressions of every length with positive common difference), with a [proof declaration in Conclusions.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Progressions/Results/Conclusions.lean), and that the quantitative bound on r_k(N) is outside the formal statement. [family-level]
- [OpenAI, *ErdosReciprocal.lean* Comparator challenge](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ErdosReciprocal.lean) (openai/math, commit adc7f12). Defines `ReciprocalProgressionTheorem` (a non-summable reciprocal sum implies `HasAP A k` for all k). The proof in the challenge file is left as `sorry` by design, to be supplied by the solution module.
- [google-deepmind/formal-conjectures, *ErdosProblems/3.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/3.lean#L36) (formal-conjectures). Marks `erdos_3` as research solved, cites this paper as [OAI26] and links the OpenAI Lean proof; also states Kelley–Meka, Bloom–Sisask, Green–Tao, Gowers and Leng–Sah–Sawhney bounds as variants.
- [MathVet, *fidelity-table.csv* (row 159)](https://raw.githubusercontent.com/mathvet/mathvet/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv) (mathvet/mathvet, Oct 2026). Records coverage as "partial" and a comparator pass for `ErdosReciprocal`, noting that the quantitative Szemerédi bound is not stated.
- [Neal McBurnett, *openai-math-lean-tooling configs.csv*](https://raw.githubusercontent.com/nealmcb/openai-math-lean-tooling/824beb05b35eb09eeb8c8571be7dbb61975c2e46/results/cmp-all/configs.csv) (run started 10 Oct 2026). Independent Comparator re-run with `ErdosReciprocal` status "accepted" (solution module `OAI.Combinatorics.Progressions.Main`, about 2472 s check time, 14.3 GiB peak RSS).
- [plasma-ai, *E0003 claim page: 2026_09_23_openai*](https://github.com/plasma-ai/erdos/blob/main/wiki/problems/additive_combinatorics/E0003/claims/2026_09_23_openai.md) (plasma-ai/erdos wiki, 7 Oct 2026). Records Corollary 1.2 as accepted after building `OAI.Erdos3.manuscriptReciprocalProgressionTheorem` and checking that it uses only standard axioms; states that Theorem 1.1's proof is not covered.

## Related prior literature mentioned by others
- [Thomas F. Bloom and Olof Sisask, *Breaking the logarithmic barrier in Roth’s theorem on arithmetic progressions*](https://arxiv.org/abs/2007.03528) (arXiv:2007.03528, 7 July 2020; revised 1 September 2021). Kalai’s October 2026 post identifies this three-term reciprocal-sum result as the predecessor to the manuscript’s claimed extension to every finite progression length.

## Possibly relevant literature (found by the agent, not checked)
- [Sarah Peluse, *Finding arithmetic progressions in dense sets of integers*](https://arxiv.org/abs/2509.22962) (arXiv:2509.22962, Sept 2025). Survey of recent higher-order Fourier progress behind the k ≥ 5 bounds that the introduction's prior-bounds discussion builds on.
- [Joni Teräväinen and Mengdi Wang, *On the Green-Tao theorem for sparse sets*](https://arxiv.org/abs/2603.09281) (arXiv:2603.09281, Mar 2026). Proves a quantitative relative-density bound exp(-(log log log N)^{c_k}) for k-AP-free subsets of the primes, which bears on the paper's claim that it recovers the Green–Tao relative-density theorem.

## Digests and expositions
- [Azmat, *Erdős–Turán Conjecture: How OpenAI Tackled the Arithmetic Progression Barrier*](https://binaryverseai.com/erdos-turan-conjecture-openai-proof/) (BinaryVerse AI, 11 October 2026). Outlines the manuscript’s density-increment argument using triangular polynomial cells and distinguishes its quantitative bound, reciprocal-sum consequence, and published Lean scope.
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/abs/2610.17090) (arXiv:2610.17090, 12 Oct 2026). Has a family card for 159 (Section 8.3.5) and labels the triangular polynomial cells with precision budgets as a "new architecture"; it calls its novelty verdicts provisional. [family-level]

## News and blogs
- [José Hdz. Stgo., *The long-awaited simple proof of the Green-Tao theorem is finally here!*](https://elr3to.blogspot.com/2026/10/the-long-awaited-proof-of-green-tao-is.html) (Apuntes misceláneos, 7 October 2026). Observes that the manuscript’s Corollary 1.2, together with divergence of the sum of reciprocals of primes, implies arbitrarily long arithmetic progressions in the primes.
