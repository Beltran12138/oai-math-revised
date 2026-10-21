# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Dani Dorfman and Uri Zwick, *Strategy recovery for Mean-Payoff Games is as hard as solving them from scratch*](https://arxiv.org/abs/2610.25188) (arXiv:2610.25188, 18 Oct 2026). Reduces solving mean-payoff games to recovering optimal strategies from known values; its "Note added in proof" ([HTML version](https://arxiv.org/html/2610.25188)) cites this preprint ("OpenAI recently announced a quasipolynomial-time algorithm for solving MPGs") and adds that its reductions remain meaningful since the algorithm is not polynomial-time.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 104*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/104.md) (lean/docs/104.md, release of 6 Oct 2026). The notes list this paper as an accompanying paper, but the formalized statements are the randomized companion's zero-threshold algorithm and a finite counterexample to Truffet's elimination step; the deterministic main theorem is not formalized. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Ali Asadi, Krishnendu Chatterjee, Ruichen Luo, *Algorithms with Smoothed Polynomial-Time Complexity for Deterministic Discounted-sum and Mean-payoff Games*](https://arxiv.org/abs/2610.14150) (arXiv:2610.14150, 9 Oct 2026). The introduction contrasts this paper with smoothed results on ergodic graphs (Loff–Skomra); this newer paper claims smoothed polynomial complexity for a strategy-iteration variant on general game graphs and does not mention the OpenAI release.

## Digests and expositions
- [Latent Seminar, *Quasipolynomial algorithms for mean-payoff games*](https://lowrank.github.io/latent-seminar/OpenAI-Math/104-mean-payoff-games) (7 October 2026). Explains the four manuscripts' potential comparisons, recursive methods, stochastic discounting, and parity strategy composition, explicitly without independently verifying the complete proofs. [family-level]
- [AI Proved What?, *Who wins in the long run?*](https://aiprovedwhat.com/episodes/104-quasipolynomial-mean-payoff-games/) (Episode 104, October 2026; status updated 19 October 2026). Provides an animated exposition and transcript covering all four claims, the binary-weight complexity distinction, and the reported limits of Lean coverage. [AI-generated per source] [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, 10 October 2026). Identifies family 104 among families whose formal statements cover less than the announced results, specifically flagging the deterministic algorithms and their extensions. [family-level]
