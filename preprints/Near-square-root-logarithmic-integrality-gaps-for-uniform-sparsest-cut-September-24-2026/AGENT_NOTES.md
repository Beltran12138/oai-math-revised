# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 117*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/117.md) (release Lean docs, 2026-10-06). Describes the formalized statement as an existential sequence of uniform-demand Goemans–Linial instances with positive relaxation optimum and integrality gap at least $c\sqrt{\log n}/(\log\log n)^3$, and links the comparator statement. [family-level]
- [OpenAI, *UniformSparsestCut.lean (comparator statement `mainGap`)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformSparsestCut.lean) (openai/math, commit adc7f12). Lean statement of Theorem 1.1, the ratio $\mathrm{OPT}/\mathrm{glValue}$ along a sequence $n_j\to\infty$; the proof is a `sorry` placeholder, which is how comparator challenge files are written.
- [OpenAI, *OAI/Combinatorics/SparsestCut/Main.lean (`OAI.UniformSparsestCut.mainGap`)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/SparsestCut/Main.lean) (openai/math, commit adc7f12). The release's Lean proof of the main gap theorem, assembled from lemmas in other modules of the same directory.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Georgios Stamoulis, *Integrality Gap Bounds for the Goemans-Linial SDP on Finite Abelian Cayley Graphs*](https://arxiv.org/abs/2609.05368) (arXiv:2609.05368, 2026-09-04). Studies the same Goemans–Linial relaxation of uniform sparsest cut on abelian Cayley graphs, showing exactness in some cases and a family with gap exactly 16/15; it bears on the paper's discussion of uniform-demand gap lower bounds.

## Digests and expositions
- None found.

## News and blogs
- None found.
