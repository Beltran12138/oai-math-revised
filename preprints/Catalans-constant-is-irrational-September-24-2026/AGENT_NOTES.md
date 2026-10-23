# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-23.

## Follow-up works
- [Rohit Kumar Jha, *A finite irrationality measure for Catalan's constant*](https://zenodo.org/records/23237269) (Zenodo preprint, doi:10.5281/zenodo.23237269, 2026-10-08). Extends this paper's determinant proof by bounding complementary minors uniformly, claiming $|G-p/q|>q^{-10^8}$ for large $q$; the abstract states the exponent bound is formalized in Lean.
- [Marcos Costa Santos Carreira, *General designs and an irrationality exponent for Catalan's constant*](https://zenodo.org/doi/10.5281/zenodo.23326324) (Zenodo preprint, doi:10.5281/zenodo.23326325, 2026-10-12). Gives four conditions on the five integer design parameters of this paper's argument under which the proof still works, a design with a larger certified gap, and the bound $\mu(G)<2715$ using ingredients from Jha and Litsey; prepared with assistance from Claude per the record.
- [Marcos Costa Santos Carreira, *Determinant constructions for the Dirichlet beta value at four*](https://zenodo.org/doi/10.5281/zenodo.23326646) (Zenodo preprint, doi:10.5281/zenodo.23326647, 2026-10-12). Tests whether this paper's determinant method extends to $\beta(4)$ and reports computational denominator obstructions, without claiming a proof.
- [Sean Litsey, *An Irrationality Measure for Catalan's Constant*](https://hexagonmath.org/abs/2610.00187v5) (hexagon:2610.00187, v1 2026-10-10, v5 2026-10-18). Builds on this paper's proof to claim $\mu(G)\le 740$, with a Lean 4 formalization stated in the abstract. [AI-generated per source]
- [Sean Litsey, *Irrationality measures for $G\pm5\pi^2/48$ and $L(2,\chi_{-3})$*](https://hexagonmath.org/abs/2610.00401v1) (hexagon:2610.00401v1, 2026-10-20). Applies a variant of this paper's determinant method, using rectangular Löwner matrices of digamma differences, to claim $\mu(G\pm5\pi^2/48)\le38.35$ and $\mu(L(2,\chi_{-3}))\le23.82$, stated as formalized in Lean 4. [AI-generated per source]
- [Hrishik Sai Bojnal (fringewidth) / Claude, *catalan-exponent*](https://github.com/fringewidth/catalan-exponent) (GitHub, certification dated 2026-10-15). Re-runs Carreira's Theorem 35 with a different design to claim $\mu(G)<2402$; it does not change the construction from this paper, and the README says no second person has checked the instantiation. [AI-generated per source]
- [Shawn Krisman, *One of β(4), β(6),..., β(36) is irrational*](https://hexagonmath.org/abs/2610.00285v2) (hexagon:2610.00285v2, 2026-10-16). Cites this paper and says it was prompted by it; the abstract describes its own construction and does not say it uses this paper's method. [AI-generated per source]

## Comments and discussion
- [Persiflage (galoisrepresentations.org), *A Brief Digest of Some New OpenAI Results*](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/) (blog, 2026-10-08). Item 7 discusses this paper: it sees new ideas or optimizations, says "certain optimizations are taking place without being motivated at all", and notes no analogous OpenAI proof for $L(2,\chi_{-3})$ yet.
- [Marcos Costa Santos Carreira, *catalan-designs* repository](https://github.com/MarcosCarreira/catalan-designs) (GitHub, 2026-10). Contains, alongside Carreira's two notes above, a verification report on this paper and the scripts and logs behind its computations; prepared with assistance from Claude per the acknowledgement.
- [நா. கணேசன் (Dr. N. Ganesan) (@naa_ganesan), post on X](https://x.com/naa_ganesan/status/2107845798578749721) (2026-10-07). Points to the 44-page preprint, suggests it "can be made into arxiv readable paper", and notes that an earlier attempt by Zhi-Wei Sun "had failed scrutiny".
- [UnstableReserves (@UnstableReserve), post on X](https://x.com/UnstableReserve/status/2109926974856523922) (2026-10-13). Reports an independent exact rebuild of the paper's mod-101 certificate ("all 144 pivots") and a check of the $\zeta(2)$ cancellation for $N=1,2$.

## Formalization
- [OpenAI, Lean scope note for family 005](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/005.md) (openai/math release, 2026-10-06). States that the release's Lean formalization proves irrationality of $G=\sum_{j\ge0}(-1)^j/(2j+1)^2$ and links the comparator statement.
- [OpenAI, comparator statement `Catalan.lean`](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/Catalan.lean) (openai/math, 2026-10-06). Mathlib-only statement `OAI.InternalCatalan.catalan_irrational` of the main theorem, which the release's proof is checked against.
- [google-deepmind/formal-conjectures, `FormalConjectures/Wikipedia/Irrational.lean`](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/Irrational.lean#L26) (formal-conjectures, 2026-10). Marks `irrational_catalanConstant` as `research solved`, citing this paper and linking the release's Lean proof.
- [Rohit Kumar Jha, *catalan-measure* Lean development and verification report](https://github.com/rohitkrjha/catalan-measure) (GitHub, v1, 2026-10-08). Reports a Lean build, transitive axiom audit and kernel replay for Jha's quantitative extension, noting the checks reused pinned dependency caches.
- [Sean Litsey / Claude, *catalan-irrationality-measure*](https://github.com/slitsey/catalan-irrationality-measure) (GitHub, 2026-10). Lean development of the claimed $\mu(G)\le740$, including 478 files from this paper's formalization; the README says independent-kernel replay and comparator acceptance are pending, and it gives updated companion bounds $34.74$ and $15.50$. [AI-generated per source]

## Related prior literature mentioned by others
- [Wadim Zudilin, *A determinantal approach to irrationality*](https://arxiv.org/abs/1507.05697v2) (arXiv:1507.05697v2, 2016-02-02; Constructive Approximation, 2017). The Prove2Me exposition identifies this determinantal irrationality criterion and its Catalan obstruction as background to this paper's strategy; it is also cited in the manuscript.
- [Frank Calegari, Vesselin Dimitrov and Yunqing Tang, *The linear independence of $1$, $\zeta(2)$, and $L(2,\chi_{-3})$*](https://arxiv.org/abs/2408.15403v2) (arXiv:2408.15403v2, 2024-09-16). Litsey's Hexagon follow-up cites this result as prior work for its extension of the Catalan construction to $L(2,\chi_{-3})$.
- [Zhi-Wei Sun, *Catalan's constant is irrational*](https://arxiv.org/abs/2609.04176) (arXiv:2609.04176, 2026-09-03). Earlier preprint claiming the same result; the OpenAI manuscript reportedly states it uses nothing from it.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- None found.

## News and blogs
- [David H. Bailey, *OpenAI stuns mathematicians with 722 new papers*, Math Scholar](https://mathscholar.org/2026/10/openai-stuns-mathematicians-with-722-new-papers/) (blog, 2026-10-07, updated 2026-10-19). Reports OpenAI's claimed proof that Catalan's constant is irrational and describes it as a problem at least 70 years old.
