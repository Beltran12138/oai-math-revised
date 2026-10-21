# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 137: One-tape time simulation in two-fifths-power space*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/137.md) (lean/docs/137.md, release of 6 October 2026). Describes the scope of the Lean formalization of the capped $\widetilde O(T^{2/5})$ and uncapped $\widetilde O((t+2)^{2/5})$ simulators under the stated access assumptions, excluding general multitape simulation, hierarchy consequences, and bounded-space-halting results. [AI-generated per source]
- [OpenAI math release, *OneTapeSpace.lean (Comparator challenge statement)*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/OneTapeSpace.lean) (openai/math, commit fd4aeeb). The comparator file states the two main results, `Fifths.Single.capped` and `Fifths.Single.unknown`, for a one-writable-tape machine under an access hypothesis, with a space bound of the form $c\,T^{2/5}(\log(T+2))^e$.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Hopcroft, Ullman, *Relations between time and tape complexities*](https://projects.csail.mit.edu/jacm/References/hopcroftu1968:414.html) (J. ACM 15(3):414–427, 1968). The paper credits the classical $O(\sqrt t)$ one-read/write-tape simulation, which Theorem 1 improves, to Hopcroft and Ullman only through Williams's account; this appears to be the original source and is not in the paper's bibliography.
- [Y. Shalunov, *Improved Bounds on the Space Complexity of Circuit Evaluation*](https://arxiv.org/abs/2504.20950) (arXiv:2504.20950, v1 April 2025, v2 June 2025). Reduces circuit evaluation directly to Cook–Mertz tree evaluation and recovers a $\sqrt t\log t$-space simulation of time-$t$ machines, which may be relevant to the paper's separate $\widetilde O(\sqrt T)$ multitape simulation.

## Digests and expositions
- [Latent Seminar, *One-tape computation in two-fifths-power space*](https://lowrank.github.io/latent-seminar/OpenAI-Math/137-one-tape-space-simulation) (Latent Seminar, 2026-10-07). Explains the block/epoch construction, retained-guess accounting, reusable-register interpolation, and the resulting two-fifths exponent; the page states that it has not independently verified the complete proof.

## News and blogs
- None found.
