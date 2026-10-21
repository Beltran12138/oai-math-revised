# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 126: Exponential semidefinite complexity of perfect matching*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/126.md) (lean/docs/126.md, October 2026). The release's own scope note: the formalized comparator statements give superpolynomial bounds (PSD rank of the selected unshifted perfect-matching slack matrix, and the size of exact affine semidefinite lifts, exceed $n^C$ for every fixed $C>0$), not the paper's exponential bound for every fixed shift $0<\rho<1$. [AI-generated per source] [family-level]
- [OpenAI math release, *ComparatorChallenges/MatchingAffineLift.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MatchingAffineLift.lean) (openai/math, commit adc7f12). The comparator statement `affine_lift_lower_bound` says that for every $C>0$ an affine PSD lift of size $r$ of the perfect matching polytope has $n^C<r$ for large even $n$; this file only states the result, with the proof left as `sorry` and developed separately in MatchingPSD. [AI-generated per source]

## Related prior literature mentioned by others
- [Gábor Braun et al., *The matching problem has no small symmetric SDP*](https://arxiv.org/abs/1504.00703) (arXiv:1504.00703, 2 April 2015; revised 30 November 2016). Cited as the source of the compact-SDP question; it proves an exponential lower bound under symmetry assumptions, whereas the release manuscript claims a bound for arbitrary real PSD factors.

## Possibly relevant literature (found by the agent, not checked)
- [J. Briët, D. Dadush, S. Pokutta, *On the existence of 0/1 polytopes with high semidefinite extension complexity*](https://arxiv.org/abs/1305.3268) (arXiv:1305.3268, 2013). Proves non-constructively that 0/1 polytopes with semidefinite extension complexity $2^{\Omega(n)}$ exist; context for Corollary 1.2, which claims such a bound for the explicit perfect matching polytope.
- [H. Fawzi, J. Gouveia, P. A. Parrilo, R. Z. Robinson, R. R. Thomas, *Positive semidefinite rank*](https://arxiv.org/abs/1407.4095) (arXiv:1407.4095; Math. Program. 153 (2015)). A survey of PSD rank, the quantity bounded in Theorem 1.1, and of its relation to semidefinite representations of polytopes.
- [G. Schoenebeck, *Linear Level Lasserre Lower Bounds for Certain k-CSPs*](https://www.schoeneb.people.si.umich.edu/papers/Lasserre.html) (FOCS 2008). Linear-level Lasserre/SoS lower bounds for XOR-type systems, related to the Grigoriev-type parity functional on expanding graphs built in the paper's parity section.
- [P. Austrin, K. Risse, *Perfect Matching in Random Graphs is as Hard as Tseitin*](https://arxiv.org/abs/2201.10835) (arXiv:2201.10835; TheoretiCS 1 (2022)). Reduces Tseitin formulas to perfect-matching formulas to prove Sum-of-Squares degree lower bounds; the paper's proof also realizes an expander parity system inside perfect matchings.

## Digests and expositions
- [Open Mathematics Courses, *Semidefinite lifts of the perfect matching polytope*](https://kokunoyumeto.github.io/open-math-courses-public/courses/semidefinite-lifts-of-the-perfect-matching-polytope/) (online course, undated). Seven lessons explain the manuscript's PSD factorizations, cell averaging, orthogonal splitting, Fourier smoothing and parity obstruction, with proofs and exercises; the site credits Claude Opus 5.5 and states that independent review is incomplete. [AI-generated per source]

## News and blogs
- None found.
