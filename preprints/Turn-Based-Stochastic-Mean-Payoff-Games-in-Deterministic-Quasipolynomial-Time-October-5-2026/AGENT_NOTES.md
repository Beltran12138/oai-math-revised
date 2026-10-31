# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Ashkan Soleymani and Gabriele Farina, *A Quasipolynomial Algorithm for $\ell_\infty$ Contractions*](https://arxiv.org/abs/2610.30122) (arXiv:2610.30122, 21 Oct 2026). Its [Applications paragraph](https://arxiv.org/html/2610.30122v1) states that the algorithm "solves SSGs exactly in quasipolynomial time" and, via Andersson–Miltersen equivalences, that the bound extends to turn-based stochastic parity, mean-payoff, discounted-payoff and terminal-payoff games; Section 2 cites this paper as concurrent work that exploits monotonicity of value operators. [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 104*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/104.md) (lean/docs/104.md, release of 6 Oct 2026). The notes describe the randomized zero-threshold theorem and a finite counterexample to Truffet's elimination procedure, and list only the two September 25 mean-payoff papers; this paper's stochastic result is not formalized. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Marcello Mamino, *Strategy Recovery for Stochastic Mean Payoff Games*](https://arxiv.org/abs/1506.04641) (arXiv:1506.04641, 15 Jun 2015). This paper outputs only the nonnegative-value set, not optimal strategies; Mamino shows that finding optimal positional strategies for stochastic mean-payoff games, even when all values are known, is as hard as solving the games.

## Digests and expositions
- [Latent Seminar, *Quasipolynomial algorithms for mean-payoff games*](https://lowrank.github.io/latent-seminar/OpenAI-Math/104-mean-payoff-games) (7 October 2026). Explains the four manuscripts' potential comparisons, recursive methods, stochastic discounting, and parity strategy composition, explicitly without independently verifying the complete proofs. [family-level]
- [AI Proved What?, *Who wins in the long run?*](https://aiprovedwhat.com/episodes/104-quasipolynomial-mean-payoff-games/) (Episode 104, October 2026; status updated 19 October 2026). Provides an animated exposition and transcript covering all four claims, the binary-weight complexity distinction, and the reported limits of Lean coverage. [AI-generated per source] [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, 10 October 2026). Identifies family 104 among families whose formal statements cover less than the announced results, specifically flagging the deterministic algorithms and their extensions. [family-level]
