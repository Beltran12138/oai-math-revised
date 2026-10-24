# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [bocowgill (review on google-deepmind/formal-conjectures PR #7152)](https://github.com/google-deepmind/formal-conjectures/pull/7152) (GitHub, 2026-10-12). Approving review saying the proposed Lean statement matches Theorem 1.1 and the manuscript's conventions; it explicitly approves only the statement translation, not a formal proof.

## Formalization
- [OpenAI math release, *Lean scope note for family 329*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/329.md) (lean/docs/329.md, 2026-10-06). The release's scope note: the formalized result covers Theorem 1.1 with $L=B_\infty$, plus a further construction in which the dual-to-primal logarithmic entropy ratio tends to zero as the dimension grows. [family-level]
- [OpenAI math release, *MetricEntropyDuality.lean* (comparator statement)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/MetricEntropyDuality.lean) (lean/ComparatorChallenges). Comparator challenge statement `exists_entropy_duality_counterexample_with_covers` for Theorem 1.1, with explicit finite-cover hypotheses. The proof field in this file is `sorry`, as is usual for a comparator target.
- [anxkhn, *feat(Paper): add the metric-entropy duality counterexample*](https://github.com/google-deepmind/formal-conjectures/pull/7152) (google-deepmind/formal-conjectures PR #7152, opened 2026-10-11, open when checked). Lean 4 statement of Theorem 1.1, pinned to a commit of openai/math; no `formal_proof` attribute is added because no external proof build or Comparator check was run.

## Related prior literature mentioned by others
- [Hu, Peale, Reingold, *Metric Entropy Duality and the Sample Complexity of Outcome Indistinguishability*](https://arxiv.org/pdf/2203.04536) (arXiv:2203.04536, ALT 2022). Already cited by the paper. Its arXiv text describes the Pietsch conjecture as open, with weaker versions proved, and links it to learning-theoretic sample complexity.
- [S. Artstein, V. Milman and S. J. Szarek, *Duality of metric entropy*](https://arxiv.org/abs/math/0407236) (Annals of Mathematics 159, 2004; announced in [C. R. Math. Acad. Sci. Paris 337 (2003), 711–714](https://www.numdam.org/item/CRMATH_2003__337_11_711_0)). Cited in the AI-generated [Open Mathematics Courses lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-duality-conjecture-for-metric-entropy/covering-numbers-and-polar-bodies.html), this establishes the dimension-free comparison when one body is a Euclidean ball, a special case distinguished from the manuscript's unrestricted conjecture.
- [S. Artstein, V. Milman, S. J. Szarek and N. Tomczak-Jaegermann, *On convexified packing and entropy duality*](https://arxiv.org/abs/math/0407238) (Geometric and Functional Analysis 14, 2004). The AI-generated [Open Mathematics Courses lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-duality-conjecture-for-metric-entropy/covering-numbers-and-polar-bodies.html) cites Conjecture 1 and Theorem 2 and presents convexified-packing duality alongside the manuscript's counterexample for ordinary covering numbers.

## Possibly relevant literature (found by the agent, not checked)
- [Artstein, Milman, Szarek, *More on the duality conjecture for entropy numbers*](https://www.numdam.org/item/CRMATH_2003__336_6_479_0) (C. R. Math. Acad. Sci. Paris 336 (2003), 479–482). Proves duality up to a logarithmic factor when one body is an ellipsoid, a precursor to the Euclidean-ball case that the paper discusses in its related-work section; not in the bibliography.
- [Szarek, *Convexity, complexity, and high dimensions*](https://ems.press/books/standalone/21/460) (Proc. ICM 2006, vol. II, 1599–1621, doi:10.4171/022-2/76). ICM survey that lists "metric entropy and its duality" among its topics, which may help place the paper's claim against the status of the conjecture as of 2006; not in the bibliography.

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *The duality conjecture for metric entropy*](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-duality-conjecture-for-metric-entropy/) (Open Mathematics Courses, undated). Three lessons with proofs and exercises explain the manuscript's matrix-to-body conversion, partition compression and finite-field construction; the source states that independent review is incomplete. [AI-generated per source]

## News and blogs
- None found.
