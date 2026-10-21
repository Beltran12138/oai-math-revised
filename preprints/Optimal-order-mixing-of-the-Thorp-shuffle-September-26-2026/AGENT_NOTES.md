# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [acprk (GitHub), *Remark R5: Thorp shuffle 1600d → 24d*](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R5-thorp-24d) (openai-math-remarks, local draft, undated). Re-selects parameters in this paper's first stage and combines them with the companion's Fourier transfer to claim mixing after 24d shuffles (45d using this paper alone); asymptotic, not formalized, reviewed only by AI. [AI-generated per source]
- [public-observatory (GitHub), *thorp-shuffle-cutoff: an open research agenda on cutoff for the Thorp shuffle*](https://github.com/public-observatory/thorp-shuffle-cutoff) (GitHub repository, October 2026). A research agenda on whether the Thorp shuffle has cutoff at 2·log₂N, taking Theorem 1.1 of this paper as its starting point; its [reading notes](https://github.com/public-observatory/thorp-shuffle-cutoff/blob/main/writeups/literature.md) (2026-10-11) say the paper leaves the leading constant and cutoff open. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 238*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/238.md) (lean/docs/238.md, 2026). States that the formalization proves full-deck total-variation convergence after $1600d$ shuffles together with the 2d−O(1) support lower bound, using the comparator files ThorpFirstReciprocal.lean and ThorpRemaining.lean. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Y. Jiang, *A subquadratic upper bound for the mixing time of the Thorp shuffle*](https://arxiv.org/abs/2610.18884) (arXiv:2610.18884, 3 Oct 2026). Independent preprint proving a full-deck bound of order d^{5/3} for n=2^d, improving Morris's O(d^3); relevant for comparison with Theorem 1.1's O(d) bound. It does not mention the release. [family-level]

## Digests and expositions
- [Latent Seminar, *Optimal logarithmic mixing of the Thorp shuffle*](https://lowrank.github.io/latent-seminar/OpenAI-Math/238-thorp-shuffle) (expository notes, 2026-10-06). Outlines all twelve manuscripts’ proof methods and formalization boundaries, explicitly disclaiming independent full-proof verification. [family-level]
- [heyprof, *Thorp shuffle: how often until the deck is random?*](https://www.heyprof.app/en/demo/thorp-mischen) (interactive exposition, undated). Illustrates the family’s full-deck mixing question with small-deck distributions, single-card marginals, and the support bound. [family-level]

## News and blogs
- [Joe Halliwell and Claude Opus 5.5, *Does any of the OpenAI maths have real-world consequences?*](https://joehalliwell.com/posts/openai-maths.html) (blog, 2026-10-08). Discusses this paper’s $1600d$ bound in connection with format-preserving encryption and its limited immediate practical implications. [AI-generated per source]
