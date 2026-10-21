# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Nikolai Chukhin, *Breaking the Parity Barrier for Constant-Depth Circuits*](https://eccc.weizmann.ac.il/report/2026/248/) (ECCC TR26-248, 11 Oct 2026). Proves $2^{\Omega((n\log n/\log\log n)^{1/(d-1)})}$ lower bounds for depth-$d$ circuits ($d\ge3$) computing a trilinear mod-2 function, combining this paper's restriction lemma (with a new short proof), Håstad's switching lemma and Calabro–Impagliazzo–Paturi sparsification; ChatGPT and Claude assistance is disclosed in the manuscript.
- [Ying Xie, *From Signed Restrictions to Lower Bounds at Every Fixed Depth*](https://zenodo.org/records/23429046) (Zenodo, doi:10.5281/zenodo.23429046, 17 Oct 2026). Extends the depth-three lower bound for this paper's language to every fixed depth $D\ge3$, with bound $2^{\Omega_D((n\log n/\log\log n)^{1/(D-1)})}$, reusing the paper's signed restriction lemma.
- [Xin Li and Yan Zhong, *Short Point Lists for CNFs and Stronger Constant-Depth Circuit Hardness*](https://arxiv.org/abs/2610.27127) (arXiv:2610.27127, also ECCC TR26-261, 19 Oct 2026). Uses a short-description CNF decomposition to prove $2^{\Omega_d((n\log n)^{1/(d-1)})}$ lower bounds at every fixed depth $d\ge3$ for three explicit families, including OpenAI's polynomial evaluator with its original parameters; also states, attributing the observation to Chukhin, that this paper's proof implicitly gives $2^{\Omega(\sqrt{n\log\log n/\log\log\log n})}$.

## Comments and discussion
- [Oded Goldreich, *Comments on Breaking the Parity Barrier for Constant-Depth Circuits*](https://www.wisdom.weizmann.ac.il/~oded/MC/437.html) (Oded's choices no. 437, 2026-10-13). Discusses Chukhin's work as a more accessible development of the OpenAI proof and connects its trilinear target to earlier work on multilinear circuit lower bounds.

## Formalization
- [OpenAI math release, Lean scope notes for result 112 (mirror on mathcommunity/oai-math-revised)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/112.md) (lean/docs/112.md, 2026). Describes the formalized statement as one fixed polynomial-time language whose exact OR–AND–OR circuit size (unrestricted finite fan-in and sharing) eventually exceeds $2^{A\sqrt n}$ for every fixed $A>0$; no fixed exponent $n^{1/2+\varepsilon}$ is claimed.
- [OpenAI, *ComparatorChallenges/DepthThree.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/DepthThree.lean) (openai/math, commit adc7f12). Comparator statement `exists_polynomial_time_language_depth_three_lower_bound` for the main theorem (stated with `sorry` in this file; the proof lives elsewhere in the release's Lean code).

## Related prior literature mentioned by others
- [Oded Goldreich and Avishay Tal, *Matrix Rigidity of Random Toeplitz Matrices*](https://www.wisdom.weizmann.ac.il/~oded/p_rigid.html) (author manuscript, first posted May 2015). Goldreich's comments identify this work's trilinear function, previously studied for canonical depth-three circuits, as the target used in Chukhin's follow-up to the OpenAI result.

## Possibly relevant literature (found by the agent, not checked)
- [C. Calabro, R. Impagliazzo, R. Paturi, *A duality between clause width and clause density for SAT*](https://courses.cs.washington.edu/courses/cse599i/24sp/papers/Calabro-Impagliazzo-Paturi.pdf) (CCC 2006). Improved sparsification lemma; relevant to the paper's sparse-partition lemma (which uses IPZ01 and DHMTW14) and used by Chukhin in the fixed-depth follow-up.
- [A. Golovnev, A. S. Kulikov, R. Williams, *Circuit Depth Reductions*](https://arxiv.org/abs/1811.04828) (arXiv:1811.04828, 2018). Shows every size-$s$ circuit is an OR of $2^{s/3.9}$ 16-CNFs, linking depth-three lower bounds with bounded bottom fan-in (a setting the paper's introduction contrasts with its unbounded-fan-in model) to general circuit lower bounds.

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *Depth-three circuits beyond the square root*](https://kokunoyumeto.github.io/open-math-courses-public/courses/depth-three-circuits-beyond-the-square-root/) (seven-lesson online course, undated). Presents the paper's restriction expansion, backward counting, sunflower partition, explicit language, hard slices and final lower bound with exercises and solutions; the source states that independent review is incomplete. [AI-generated per source]

## News and blogs
- None found.
