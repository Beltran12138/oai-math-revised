# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Annanay Kapila, *Subset Sum in time O(2^{0.4877n})*](https://hexagonmath.org/2610.00261v1) (hexagon:2610.00261v1, 15 Oct 2026). States that it builds on this paper, keeping its framework of isolation, capped preliminary search, modular checksum and alias subtraction, replacing the alias procedure and using 43 checksum filters, and claiming exponent 0.4877; results of this paper are restated in an appendix and Arb-based scripts check numerical inequalities. [AI-generated per source]
- [Joshua Wharton, *A conditional refinement of the Subset Sum exponent to 0.487676*](https://github.com/JoshuaQFEX/subset-sum-bound/blob/dcb002174cb1e06213e171c9f5ff6b063fdf2c40/paper.tex) (GitHub manuscript, 20 October 2026). Refines parameters and transfers certificates from Kapila's follow-up, retaining explicit dependence on the underlying algorithmic and analytic premises. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [Joshua Wharton, *Lean formalisation: scope and reproduction*](https://raw.githubusercontent.com/JoshuaQFEX/subset-sum-bound/master/FORMALIZATION.md) (GitHub, updated 20 October 2026). Reports compiled Lean proofs for finite certificates, numerical inequalities, isolation and supporting lemmas in the conditional refinement, while leaving continuous moment bounds as hypotheses and the complete solver's operation-count guarantee unproved. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Jesus Salas, *Beyond Worst-Case Subset Sum: An Adaptive, Structure-Aware Solver with Sub-$2^{n/2}$ Enumeration*](https://arxiv.org/abs/2503.20162) (arXiv:2503.20162, v1 Mar 2025, v3 Dec 2025). An earlier preprint that also claims a worst-case bound of roughly $O^*(2^{n/2-\varepsilon})$ for Subset Sum (via a technique it calls "Controlled Aliasing"), the type of statement made in Theorem 1.1; not cited in this paper.
- [Marcin Mucha, Jesper Nederlof, Jakub Pawlewicz, Karol Węgrzycki, *Equal-Subset-Sum Faster Than the Meet-in-the-Middle*](https://arxiv.org/abs/1905.02424) (arXiv:1905.02424, 2019). Beats the meet-in-the-middle bound in the worst case for the related Equal-Subset-Sum problem, relevant to the paper's "Related approaches" discussion of representation methods and worst-case savings.
- [Yiming Gao, Yansong Feng, Honggang Hu, Yanbin Pan, *Subset Balancing and Generalized Subset Sum via Lattices*](https://arxiv.org/abs/2604.04656) (arXiv:2604.04656, Apr 2026). Gives lattice-based algorithms for Subset Balancing and Generalized Subset Sum, the setting of the Randolph–Węgrzycki work that the paper contrasts with ordinary Subset Sum.

## Digests and expositions
- [we-solve research archive, *OpenAI claim summary for CS-153*](https://we-solve.github.io/contributions/worst-case-subset-sum-below-the-half-exponent/attempt-1/r1/) (we-solve, 6 Oct 2026). A short literature report summarizing the claimed uniform $O(2^{0.49n})$ algorithm from this manuscript; it states the platform has not examined or verified the material. [AI-generated per source]
- [Sankalp Thakur, *Speed Limits I: Multiplying, Transforming, Factoring*](https://transientlabs.ai/the-deep-end/speed-limits-multiplying) (Deep End Era, episode 81, undated). Includes segments on the claimed Subset Sum time improvement at 40:22 and how a referee would test it at 44:10, with disclosed AI-generated scripting and synthetic narration. [AI-generated per source]
- [dimenwarper, *oai-math-vids*, video 30 "Subset Sum in O(2^0.49n) time (138)"](https://github.com/dimenwarper/oai-math-vids) (GitHub, Oct 2026). A 4:50 narrated explainer video on this family's result in an unofficial series of Manim videos on the release. [AI-generated per source] [family-level]
- [Wikipedia contributors, *Subset sum problem*, “OpenAI” subsection](https://en.wikipedia.org/wiki/Subset_sum_problem) (Wikipedia, accessed 21 October 2026). Briefly summarizes both the release's time-exponent claim and its companion time–space claim within an overview of Subset Sum algorithms. [family-level]

## News and blogs
- None found.
