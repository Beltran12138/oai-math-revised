# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Scott Aaronson, *The Mathocalypse*](https://scottaaronson.blog/?p=10169) (Shtetl-Optimized, October 2026). Lists the sub-n log n FFT among the release's TCS results, describing it as "breaking a barrier that had stood since the 1960s"; in the comments, b_jonas discusses the unit-cost coefficient model. [family-level]

## Formalization
- [OpenAI math release, *Lean scope note for family 130*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/130.md) (lean/docs/130.md). The comparator `ExactFourier.lean` formalizes this paper's Theorem 1.1: for every c > 0 and N_0 ≥ 2, some n ≥ N_0 has an exact DFT circuit with fewer than c n log_2 n gates, with no all-length, bounded-coefficient, conditioning or bit-complexity claim; the synthesis appendix is excluded. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Josh Alman, *Kronecker Products, Low-Depth Circuits, and Matrix Rigidity*](https://arxiv.org/abs/2102.11992) (arXiv:2102.11992, STOC 2021). Gives circuits for Kronecker powers of fixed-size matrices, including Walsh–Hadamard circuits with large coefficients that sidestep bounded-coefficient lower bounds; relevant to the paper's discussion of tensor-power circuits (the bibliography cites only Alman–Li 2025 on this theme).
- [Nir Ailon, *Tighter Fourier Transform Complexity Tradeoffs*](https://arxiv.org/abs/1404.1741) (arXiv:1404.1741, 2014–2015). Shows that speeding up the FFT by a factor b forces Ω(n) ill-conditioned intermediate steps, which bears on the paper's point that its circuits allow arbitrary intermediate conditioning (the bibliography cites arXiv:1305.4745 and arXiv:1403.1307, not this one).
- [Christos H. Papadimitriou, *Optimality of the fast Fourier transform*](https://projects.csail.mit.edu/jacm/jacm79.html) (J. ACM 26(1):95–102, 1979). A classical optimality result for FFT addition counts under restrictions on the algorithm's graph; relevant to the paper's survey of lower bounds proved under restrictions on the algorithm.
- [Pavel Pudlák, *A Note On the Use of Determinant for Proving Lower Bounds on the Size of Linear Circuits*](https://eccc.weizmann.ac.il/report/1998/042) (ECCC TR98-042, 1998). Gives determinant-based lower bounds for bounded-coefficient linear circuits, extending the Morgenstern argument that Theorem 1.1 avoids by allowing unbounded coefficients.

## Digests and expositions
- [Perplexity / Orply, *Exact Fourier Cost Has Vanishing Normalized Growth on a Subsequence*](https://orply.com/articles/perplexity/130-2-finite-tensor-savings-and-exact-fourier-circuits-e64ecc42) (Orply, 2026-10-11). An AI-assisted rendering summarizing the paper's nonuniform circuit model, finite tensor saving, width-preserving Fourier transfer and price-function contradiction. [AI-generated per source]

## News and blogs
- [Peter Hall and Joseph Howlett, *The most exciting claims from OpenAI's heap of new proofs*](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (Scientific American, 2026-10-08). Has a short section on paper 130's sub-n log n Fourier result, described mainly through the uniform (log n)^(1−10^−13) bound. [family-level]
