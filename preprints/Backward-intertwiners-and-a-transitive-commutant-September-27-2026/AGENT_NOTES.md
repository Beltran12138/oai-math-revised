# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Invariant projections, hyperinvariant subspaces, and transitive algebras: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/293.md) (OpenAI Math Release, lean/docs/293.md, 2026-10-06). Describes the Lean scope for this paper: on every separable infinite-dimensional complex Hilbert space, a nonzero quasinilpotent operator whose commutant is transitive, proper and strongly closed. [family-level]
- [OpenAI math release, *BackwardIntertwiners.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BackwardIntertwiners.lean) (Comparator challenge, commit adc7f12, 2026). Comparator statement `OAI.BackwardIntertwiners.direct_algebra_corollary` (Corollary 1.2: $T\ne0$, $\|T^n\|^{1/n}\to0$, transitive, proper, SOT-closed commutant); the theorem body in this statement file is `sorry`.
- [anxkhn, *feat(Paper): add the hyperinvariant-subspace counterexample*](https://github.com/google-deepmind/formal-conjectures/pull/7000) (google-deepmind/formal-conjectures PR #7000, from [issue #6995](https://github.com/google-deepmind/formal-conjectures/issues/6995), opened 2026-10-08). Independent Lean statement of Corollary 1.2 (quasinilpotence via root-norm limit, hyperinvariance against all commuting operators) without the extra commutant-algebra assertions or a `formal_proof` link; an approving review by bocowgill (2026-10-10) states "The root-norm limit and invariance under every commuting bounded operator match the source," and the PR is open as of 2026-10-21. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [M. F. Gamal', *On existence of hyperinvariant subspaces for quasinilpotent operators with a nonsymmetry in the growth of the resolvent*](https://arxiv.org/abs/2404.04348) (arXiv:2404.04348, 2024). Shows that a resolvent-growth asymmetry forces nontrivial hyperinvariant subspaces of quasinilpotent operators; the operator $S$ of Theorem 1.1 with $\|S^n\|\le\exp(-10\lfloor(n+1)^2/4\rfloor)$ must fail that hypothesis.
- [I. B. Jung, E. Ko and C. Pearcy, *Hyperinvariant subspaces for a class of quasinilpotent operators*](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/online/111414/hyperinvariant-subspaces-for-a-class-of-quasinilpotent-operators) (Studia Math. 245 (2019) 289–296, doi:10.4064/sm171209-18-1). Gives hyperinvariant subspaces for a structurally defined subclass of quasinilpotent Hilbert-space operators; the operator of Corollary 1.2 must lie outside that subclass.
- [Sa Ge Lee, *The Hyperinvarinat Subspace Problem*](https://arxiv.org/abs/2306.13940) (arXiv:2306.13940, 2023). Short preprint whose abstract claims to solve the hyperinvariant subspace problem for Hilbert spaces; bears directly on the negative answer stated in Corollary 1.2.
- [S. I. Ansari, *The transitive algebra problem has an affirmative answer*](https://arxiv.org/abs/1307.7317) (arXiv:1307.7317, 2013; withdrawn by the author "due to a gap in the paper"). Earlier claimed affirmative answer to the transitive algebra problem, which the paper's strongly closed proper transitive commutant addresses in the negative.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/abs/2610.17090) (arXiv:2610.17090, 2026-10-12). Section 9.4.3 and Table 3 survey family 293, classifying this paper's "backward intertwiner over an ergodic base" as new and noting that no Lean development was compiled for the survey. [family-level]
- [Claude Opus 5.5 / Open Mathematics Courses, *A backward intertwiner and a transitive commutant*](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-hyperinvariant-subspace-problem/a-transitive-commutant.html) (Open Mathematics Courses, n.d.). This lesson develops the backward-intertwiner and transitivity argument and explains the connection to the companion's invariant-projection theorem, which the course does not prove; the site states that independent review is incomplete. [AI-generated per source] [family-level]

## News and blogs
- None found.
