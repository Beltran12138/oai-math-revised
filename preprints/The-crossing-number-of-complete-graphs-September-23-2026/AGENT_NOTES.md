# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [J. Balogh, N. Layman, B. Lidický, F. Pfender, G. Salazar, S. Spiro, J. Volec, *Crossing numbers of complete bipartite graphs*](https://arxiv.org/abs/2610.25204) (arXiv:2610.25204, 18 Oct 2026). Uses flag algebras to obtain asymptotic lower bounds of 0.9899 times the Hill value for complete graphs and 0.96936 times the Zarankiewicz value for balanced complete bipartite graphs; its abstract notes that both conjectures "were claimed to be true in manuscripts by OpenAI dated Sep 23, 2026", and it cites both manuscripts while describing its results as preceding them. [family-level]
- [A. Hubard, C. S. Ndiaye, O. Solé-Pi, *Crossing numbers of simplicial complexes*](https://arxiv.org/abs/2610.21017) (arXiv:2610.21017, 14 Oct 2026). Studies a higher-dimensional generalized Harary–Hill conjecture and gives a proof of Harary–Hill for antipodal drawings; a footnote says a solution to the Zarankiewicz and Hill conjectures was announced as the manuscript was about to be made public, without naming the source. [family-level]
- [M. Balko, *Proof of the Harary–Hill conjecture: an exposition*](https://arxiv.org/abs/2610.34444) (arXiv:2610.34444, 25 Oct 2026). Presents a streamlined variant of this paper's proof (a planarization proof of the cycle identity, a weaker Lemma 4, vertex isolation by factoring, and a sign-based final contradiction), extends it to give ocr+(K_n) = pcr+(K_n) = Z(n), and derives crossing numbers of further families such as K_{2k} minus a perfect matching and K_m □ C_n for even n. The author discloses ChatGPT assistance and states having independently checked, rewritten and verified all mathematical arguments; the paper also notes an independent exposition in preparation by G. Salazar.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 165* (mirrored on mathcommunity/oai-math-revised)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/165.md) (release, 6 Oct 2026). The release's Lean scope note states that the formalization proves cr(K_n) = Z(n) for n ≥ 3 with a matching two-page drawing, crossings counted as points, and links the comparator statements `CompleteCrossing.lean` and `BipartiteCrossing.lean`. [family-level]

## Related prior literature mentioned by others
- [S. Felsner, *Antipodal Pairs and Crossing Numbers of Complete Graphs*](https://page.math.tu-berlin.de/~felsner/Paper/antipodal.pdf) (preprint, 2026). Treats Hill's formula as a conjecture and studies antipodal pairs in optimal drawings; Balko's exposition cites its Theorem 9 as the reduction behind a consequence of the Harary–Hill formula and its Section 3 for the upper bound on K_{2k} minus a perfect matching.

## Possibly relevant literature (found by the agent, not checked)
- [B. M. Ábrego, O. Aichholzer, S. Fernández-Merchant, D. McQuillan, B. Mohar, P. Mutzel, P. Ramos, R. B. Richter, B. Vogtenhuber, *Bishellable drawings of K_n*](https://arxiv.org/abs/1510.00549) (arXiv:1510.00549, 2015, rev. 2018). Extends the shellability criterion cited in the introduction to the weaker bishellability condition, which also forces the Harary–Hill bound; it is not in the bibliography.

## Digests and expositions
- [Open Mathematics Courses, *Crossing numbers of complete and complete bipartite graphs*](https://kokunoyumeto.github.io/open-math-courses-public/courses/crossing-numbers-of-complete-graphs/) (undated). Eight lessons develop the manuscripts' normalization, cycle pairing, interpolation, subspace inequality and matching constructions, with proofs and exercises; the site attributes writing and self-checking to Claude Opus 5.5 and states that independent review is incomplete. [AI-generated per source] [family-level]
- [Gradient Damage, *The Harary–Hill conjecture: why 18 dots need 1,008 crossings*](https://gradientdamage.com/openai-math/harary-hill-conjecture/) (12 Oct 2026). An introductory exposition of the complete-graph formula with an illustrative animation, also introducing the companion bipartite claim and distinguishing illustration from proof verification. [family-level]

## News and blogs
- [ぶちょう (rivas_bucho), *OpenAI's 722 Math Papers Are Not a Story of 'Leaving Humans Behind'—An Introductory Guide to 8 Key Topics*](https://note.com/rivas_bucho/n/n66b30b192bcd?hl=en) (note.com, 9 Oct 2026). A general-audience overview whose brick-factory section says No. 165 "claims to have solved both this problem and its sibling, Hill's conjecture" with a Lean proof, and recalls the gap in Zarankiewicz's 1954 proof. [family-level]
