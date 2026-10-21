# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 127: Average sensitivity of polynomial threshold functions*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/127.md) (lean/docs/127.md, 2026-10-06). The release's own scope note says the formalization proves the bound $8d\sqrt n$ with $\mathrm{sgn}(0)=1$ (the asymptotic bound, not the exact-extremizer conjecture), and links the comparator statement `ComparatorChallenges/GotsmanLinial.lean`. [AI-generated per source]
- [OpenAI math release, *Lean file `OAI/Combinatorics/GotsmanLinial/Main.lean`*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/GotsmanLinial/Main.lean) (github.com/openai/math, commit adc7f12, October 2026). The theorem `gotsmanLinialStatement` concludes `averageSensitivity (polynomialThreshold p) ≤ 8 * d * Real.sqrt n` for $1\le d\le n$, i.e. the paper's Theorem 1.1.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Cristopher Moore and Alexander Russell, *Heat and Noise on Cubes and Spheres: The Sensitivity of Randomly Rotated Polynomial Threshold Functions*](https://arxiv.org/abs/1408.5425) (arXiv:1408.5425, August 2014). Its abstract says it proves an average-case version of the Gotsman–Linial conjecture for randomly rotated PTFs restricted to the cube, an earlier partial result toward the $O(d\sqrt n)$ bound not cited in the paper's introduction.

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *Average sensitivity of threshold functions*](https://kokunoyumeto.github.io/open-math-courses-public/courses/average-sensitivity-of-threshold-functions/) (Open Mathematics Courses, undated). Three lessons explain the paper's one-sided coupling inequality, weighted grading, anticommutator edge count, and noise-sensitivity consequence, with exercises and a statement that independent review is incomplete. [AI-generated per source]
- [Gist.Science, *A compensated coupling bound for the average sensitivity of polynomial threshold functions*](https://gist.science/paper/rs/rs-11323154) (summary of Research Square rs-11323154, 2026-10-13). This AI-generated synopsis attributes a refinement of OpenAI's coupling argument to Prathmesh Lagdive, Vaibhav Aglave, and Suraj Damre; the linked original manuscript could not be accessed during collection. [AI-generated per source]

## News and blogs
- None found.
