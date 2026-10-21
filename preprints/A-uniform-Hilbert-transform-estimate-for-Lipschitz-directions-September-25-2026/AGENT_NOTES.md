# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 083: Hilbert transforms along Lipschitz directions*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/083.md) (lean/docs/083.md, 2026). The release's own scope notes say the formalization proves inner-truncation-uniform $L^2$ bounds for hard truncations with $0<\varepsilon\le R\le 1/(10^6K)$ for $K$-Lipschitz unit fields, plus principal-value, weak-(2,2) and $L^2$-extension statements at a fixed short scale for 1-Lipschitz fields. [family-level]
- [OpenAI, *LipschitzHilbert.lean (comparator statement)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LipschitzHilbert.lean) (openai/math, commit adc7f12). This is a statement-only file (proofs left as `sorry`) giving the theorems `main` (with `ShortHilbertConclusion a C`) and `uniform_truncation` that the formal proof is checked against. [family-level]
- [OpenAI, *Main.lean (OAI.LipschitzHilbert.main)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/LipschitzHilbert/Main.lean) (openai/math, commit adc7f12). This is the Lean proof file for `main` and `uniform_truncation`; it calls `laceyLiInput_proved` and imports modules including `Geometry/LaceyLiProof`, so the external Lacey–Li input appears to be formalized as well. [family-level]

## Related prior literature mentioned by others
- [Michael Lacey and Xiaochun Li, *On a Conjecture of E. M. Stein on the Hilbert Transform on Vector Fields*](https://arxiv.org/abs/0704.0808) (arXiv:0704.0808; Memoirs of the AMS 205, no. 965, 2010). The [Prove2Me discussion of this manuscript](https://prove2.me/collections/oai-math?offset=20) identifies this memoir as the source of the conjectural framework and conditional estimates relating directional Hilbert transforms to maximal operators.
- [Francesco Di Plinio, Shaoming Guo, Christoph Thiele and Pavel Zorin-Kranich, *Square functions for bi-Lipschitz maps and directional operators*](https://arxiv.org/abs/1706.07111) (arXiv:1706.07111; Journal of Functional Analysis 275, 2018). The [Prove2Me discussion of this manuscript](https://prove2.me/collections/oai-math?offset=20) highlights this work's reduction from uniform vertical-frequency-band estimates to the full short principal-value bound, a predecessor explicitly acknowledged in the manuscript.

## Possibly relevant literature (found by the agent, not checked)
- [I. Assani, *On A. Zygmund differentiation conjecture*](https://arxiv.org/abs/math/0609827) (arXiv:math/0609827, 2006). The introduction traces Stein's question to Zygmund's differentiation conjecture for Lipschitz fields; this preprint proves a Zygmund-type differentiation result for rescaled Lipschitz fields at shifts below the reciprocal Lipschitz constant, matching the short-scale normalisation used here.
- [N. Liu and H. Yu, *Hilbert transforms along variable planar curves: Lipschitz regularity*](https://arxiv.org/abs/2104.12058) (arXiv:2104.12058, 2021). It proves $L^p$ bounds for Hilbert transforms along variable curves depending on a two-variable function with small Lipschitz norm, a curved, non-directional relative of the paper's Lipschitz-only hypotheses.

## Digests and expositions
- [Latent Seminar, *Hilbert transforms along Lipschitz directions*](https://lowrank.github.io/latent-seminar/OpenAI-Math/083-lipschitz-directional-hilbert-transform) (6 October 2026). This exposition distinguishes uniform truncation bounds from maximal-truncation estimates and outlines the frequency-band reduction, constant-one phase inequality and angular hierarchy, while explicitly disclaiming independent verification of the complete proofs. [family-level]

## News and blogs
- None found.
