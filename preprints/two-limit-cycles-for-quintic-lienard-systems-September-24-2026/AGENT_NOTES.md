# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Hilbert's sixteenth problem: uniform bounds for limit cycles — Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/143.md) (lean/docs/143.md, release of 6 October 2026). States that the formalization proves Theorem 1.1 (at most two limit cycles for every real F with deg F ≤ 5, and exactly two for some F), with no sign, parity, hyperbolicity or amplitude restriction; it does not cover the companion manuscript's uniform bound for arbitrary planar polynomial vector fields. [family-level]
- [OpenAI math release, *QuinticLienard.lean (comparator statement)*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/QuinticLienard.lean) (lean/ComparatorChallenges/QuinticLienard.lean). The standalone statement of the two-part theorem (encard ≤ 2 for all F of degree ≤ 5; encard = 2 for some F), with the proof left as `sorry` as a comparator target.
- [OpenAI math release, *OAI.QuinticLienard.main*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/OAI/Analysis/LienardCycles/Main.lean) (lean/OAI/Analysis/LienardCycles/Main.lean). The release's proof of the main theorem, assembled from `upper_bound` and `Sharpness.sharpness` in the same development.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Hebai Chen, Leshan Chen and Yu Xiao, *Limit cycles of slow-fast quintic Lienard systems*](https://arxiv.org/abs/2610.13080) (arXiv:2610.13080, 9 October 2026). Independently proves that for each fixed real quintic F, $\dot x=y-F(x)$, $\dot y=-\varepsilon x$ has at most two limit cycles for small ε > 0, with a two-cycle example; it covers the slow–fast regime of Theorem 1.1, presents itself as complementing Li–Lu, and does not mention the release.
- [Chen Cao, Nasrin Sadri, Yilei Tang and Zhaoxia Wang, *Global Dynamics and Periodic-Annulus Bifurcations in a Reversible Quintic Liénard System*](https://arxiv.org/html/2610.26699) (arXiv:2610.26699, 19 October 2026). A study of a different (reversible) quintic Liénard family whose introduction states that the maximum number of limit cycles of a general classical quintic Liénard equation "is still unknown"; it does not mention the release.
- [Valery A. Gaiko, *Liénard's system and Smale's problem*](https://arxiv.org/abs/math/0611143) (arXiv:math/0611143, November 2006). An earlier preprint claiming a solution of Smale's thirteenth problem on the maximum number of limit cycles of Liénard polynomial systems, by field-rotation methods; relevant as prior claimed work on the bound addressed in Theorem 1.1.

## Digests and expositions
- [Singh-AP, *ai-math-papers-explained: Uniform bounds for planar polynomial limit cycles*](https://github.com/Singh-AP/ai-math-papers-explained/blob/main/papers/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026) (GitHub, accessed 2026-10-21). A beginner-level explainer filed under the uniform-bounds paper that also covers this companion's theorem, proof outline, a two-cycle example and its Lean formalization; the README states that the slides, infographics, report and audio were generated with NotebookLM. [AI-generated per source] [family-level]

## News and blogs
- [Azmat, *Hilbert's 16th Problem: OpenAI's Limit-Cycle Proof Explained*](https://binaryverseai.com/hilberts-16th-problem-uniform-limit-cycle/) (Binary Verse AI, 10 October 2026). A blog explainer of the family that describes this paper's result as covering a restricted family with at most two limit cycles; it quotes no outside experts. [family-level]
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (self-published audit, findings dated 10 October 2026). Finding G1 distinguishes the family's general uniform-bound claim from the quintic Liénard theorem covered by its Lean statements at the audited commit `fd4aeeb2`. [family-level]
