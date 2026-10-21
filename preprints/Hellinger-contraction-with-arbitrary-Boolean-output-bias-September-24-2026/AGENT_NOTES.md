# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [V. K. Ky, *The Hellinger Conjecture for Antipodal Boolean Functions*](https://arxiv.org/abs/2610.10618) (arXiv:2610.10618, 7 Oct 2026). Gives a spectral proof of the balanced Hellinger inequality for antipodal (sign-reversing) Boolean functions and extends it to arbitrary independent binary-input channels; Section 1.2 cites OpenAI's family-119 entry as an announcement of the Hellinger inequality for arbitrary output bias, without verifying it.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 119: The Courtade–Kumar and Hellinger conjectures*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/119.md) (lean/docs/119.md, 2026). The family's Lean development covers only the companion paper's soft-channel and Courtade–Kumar results and does not cover this paper's Hellinger inequality. [family-level]
- [D. P. Woodruff et al., *general-courtade-kumar-lean*](https://github.com/dpwoodru/general-courtade-kumar-lean) (GitHub, release v1.2 dated 2026-10-01). An independent Lean 4 proof of the Courtade–Kumar inequality, which this paper derives as a corollary of the Hellinger inequality; it accompanies arXiv:2609.24931 and does not formalize the Hellinger inequality.

## Related prior literature mentioned by others
- [P. Durcik, M. Fraccaroli and J. Roos, *A weak Hellinger inequality for noisy Boolean channels*](https://arxiv.org/abs/2609.28534) (arXiv:2609.28534, v1 22 Sep 2026, v2 29 Sep 2026). Cited by Ky's follow-up; proves the Hellinger inequality of Theorem 1.1 for Boolean functions with any mean but with the full noisy output $Y$ replaced by a one-bit statistic $g(Y)$, computer-assisted and formalized in Lean 4.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [AI Proved What?, *The best bit? The Courtade–Kumar and Hellinger conjectures*](https://aiprovedwhat.com/episodes/119-courtade-kumar-hellinger-conjectures/) (Episode 119, October 2026). This AI-assisted video and transcript explain both manuscripts’ claims and proof strategies and distinguish the contraction paper’s Lean scope from the Hellinger paper’s exact-arithmetic certificates. [AI-generated per source] [family-level]

## News and blogs
- None found.
