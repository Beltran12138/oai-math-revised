# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [OpenAI, *A uniform influence bound for hypergraph properties*](https://github.com/openai/math/blob/main/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) (OpenAI Math Release preprint, 2026-10-05). The companion manuscript in the same release says it reproduces this paper's Fourier estimate and vertex-block restriction argument, and replaces the graph degree estimate with an r-uniform one to get the exponent r/(r-1). [AI-generated per source] [family-level]
- [P. M. Aronow and Patrick Lopatto, *Existence of the $q$-Colorability Threshold for Sparse Random Graphs*](https://hexagonmath.org/abs/2610.00608v1) (hexagon:2610.00608v1, 2026-10-29). The introduction cites this paper's $O((\log n)^{-2})$ bound as a claim of an unrefereed preprint, alongside Friedgut–Kalai and Bourgain–Kalai, and notes that such additive bounds in $p$ give no shrinking relative window at $p=\Theta(1/n)$; its own window of $O(n(\log n)^{-3/2})$ edges for $q$-colorability is proved by other means. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 186 (lean/docs/186.md)*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/186.md) (release Lean documentation, 2026-10-06). The scope note reports formalization of the threshold-width bound $2^{19}\log(1/(2\varepsilon))/(\log n)^2$ of Theorem 1.1, uniform over nontrivial increasing relabeling-invariant graph properties, $n\ge2$, and $0<\varepsilon<1/2$, checked against the comparator statement `ComparatorChallenges/SharpThreshold.lean`. [family-level]

## Related prior literature mentioned by others
- [Gil Kalai, *Boolean Functions: Influence, threshold and noise*](https://gilkalai.wordpress.com/wp-content/uploads/2017/01/7ecmkalr.pdf) (7ECM lecture write-up, posted January 24, 2017). Kalai points to this survey in his October 2026 discussion of both papers; Sections 5.1–5.2 explain sharp thresholds and influence bounds under symmetry, including the earlier Bourgain–Kalai graph-property estimate. [family-level]
- [Jean Bourgain and Gil Kalai, *Threshold Intervals under Group Symmetries*](https://library.slmath.org/books/Book34/files/bourkalai.pdf) (Convex Geometric Analysis, MSRI Publications vol. 34, 1998). Aronow and Lopatto cite Theorem 1 of this announcement for the $(\log n)^{-2+\delta}$ width and note that its derivative form restricts how close $p$ may be to 0 or 1; the stated condition is $\log(p(1-p))^{-1}\lesssim\log\log n$, the kind of restriction absent from the uniform-in-$p$ statement of Theorem 1.2 here.

## Possibly relevant literature (found by the agent, not checked)
- [R. Rossignol, *Threshold for monotone symmetric properties through a logarithmic Sobolev inequality*](https://arxiv.org/abs/math/0511607) (arXiv:math/0511607; Ann. Probab. 34(5), 2006). The paper improves the general threshold-width bound for symmetric monotone properties, i.e. the edge-transitive O(log(1/(2ε))/log n) baseline that the introduction cites as [FK96, Theorem 1.1].

## Digests and expositions
- None found.

## News and blogs
- None found.
