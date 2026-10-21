# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 088*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/088.md) (lean/docs/088.md, release of 2026-10-06). States that the formalized counterexample is T₁₀ × T₁₀ with ratio 22,355,476/22,020,096 > 1 (comparator statements `ProjectionCounterexample.lean` and `ProjectionVolume.lean`); the exponential-excess result for large dimensions is not included. [family-level]
- [anxkhn, *Add the exact product counterexample to Brannen's simplex maximum*](https://github.com/google-deepmind/formal-conjectures/issues/7146) (google-deepmind/formal-conjectures issue #7146, opened 2026-10-11, open). Proposes adding the explicit dimension-20 witness and exact ratio from Theorem 1 of this paper, without the exponential consequence.
- [anxkhn, *feat(Paper): add Brannen's product counterexample*](https://github.com/google-deepmind/formal-conjectures/pull/7151) (google-deepmind/formal-conjectures PR #7151, opened 2026-10-11, open, one approving review 2026-10-12). Only the rational comparison is proved there; the geometric identity for the projection-body volume is left as a `sorry`, with no `formal_proof` attribute.

## Related prior literature mentioned by others
- [Yibin Feng, Shengnan Hu, Weiru Liu and Lei Xu, *On the Reverse Projection Inequality*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/743/12781--2026.8.26.pdf) (MathSciDoc:2608.23002, 2026). The Open Mathematics Courses exposition cites this earlier construction of counterexamples with at most $n+2$ facets in every dimension $n\ge9$ as context for the paper's dimension-20 Cartesian-product construction.

## Possibly relevant literature (found by the agent, not checked)
- [E. Lutwak, D. Yang, and G. Zhang, *A new affine invariant for polytopes and Schneider's projection problem*](https://math.nyu.edu/~dy444/papers/trans.pdf) (Trans. Amer. Math. Soc. 353 (2001), 1767–1779). Gives an asymptotically optimal upper bound for |ΠK|/|K|^{n-1} for centrally symmetric bodies; relevant to the paper's discussion of how upper constants grow with dimension (where it cites only Henk 2025).
- [C. Saroglou, *Volumes of projection bodies of some classes of convex bodies*](https://cambridge.org/core/journals/mathematika/article/abs/volumes-of-projection-bodies-of-some-classes-of-convex-bodies/D6FD86056999DA0B98279D85CE02B4C9) (Mathematika 57 (2011), no. 2, 329–353, doi:10.1112/S0025579311001860). Confirms some three-dimensional conjectures of Brannen on the maximum of this ratio for zonoids, cones and double cones; context for the status of Brannen's simplex conjecture before this paper and Feng–Hu–Liu–Xu.

## Digests and expositions
- [Claude Opus 5.5 / Open Mathematics Courses, *Projection bodies and products of simplices*](https://kokunoyumeto.github.io/open-math-courses-public/courses/projection-bodies-and-products-of-simplices/index.html) (October 2026). Three lessons explain Cauchy's formula, affine covariance, multiplicativity, the simplex value, and the paper's dimension-20 counterexample and exponential excess, with proofs and exercises; the source says independent review is incomplete. [AI-generated per source]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit at commit fd4aeeb2, 10 October 2026). Entry F-174 reports an exact-arithmetic check of the printed ratio for the dimension-20 product-of-simplices counterexample.
