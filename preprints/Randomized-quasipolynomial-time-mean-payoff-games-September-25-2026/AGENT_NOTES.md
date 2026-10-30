# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Ashkan Soleymani and Gabriele Farina, *A Quasipolynomial Algorithm for $\ell_\infty$ Contractions*](https://arxiv.org/abs/2610.30122) (arXiv:2610.30122, 21 Oct 2026). Its [Section 2](https://arxiv.org/html/2610.30122v1) cites this paper, among all four family papers, as concurrent work that exploits monotonicity of value operators, and contrasts this with its own algorithm for "arbitrary $\ell_\infty$-nonexpansive maps without assuming monotonicity"; its Introduction claims consequences for deterministic mean-payoff games via known reductions. [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 104*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/104.md) (lean/docs/104.md, release of 6 Oct 2026). Describes two formalized statements: this paper's randomized algorithm, which outputs the complete zero-threshold winning set with probability at least 7/8 in quasipolynomial bit time on every tape, and a finite counterexample to one step of Truffet's elimination procedure (the subject of this paper's appendix). [family-level]
- [OpenAI math release, *RandomizedMeanPayoff.lean* (comparator statement)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/RandomizedMeanPayoff.lean) (lean/ComparatorChallenges, release of 6 Oct 2026). States `OAI.randomized_quasipolynomial_mean_payoff`: a fixed randomized machine halts on every random tape within $2^{C(\log_2(L+2))^2}$ steps and is correct on at least 7/8 of tapes; the proof is not in this comparator file.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Dani Dorfman and Uri Zwick, *Strategy recovery for Mean-Payoff Games is as hard as solving them from scratch*](https://arxiv.org/abs/2610.25188) (arXiv:2610.25188, 18 Oct 2026). This paper's certified output includes positional strategies for both players, and Dorfman–Zwick prove that recovering strategies from values is as hard as solving the game; their note added in proof cites the deterministic companion, not this paper.
- [Ali Asadi, Krishnendu Chatterjee, Ruichen Luo, *Algorithms with Smoothed Polynomial-Time Complexity for Deterministic Discounted-sum and Mean-payoff Games*](https://arxiv.org/abs/2610.14150) (arXiv:2610.14150, 9 Oct 2026). The introduction contrasts randomness in the input (Loff–Skomra's smoothed model) with randomness in the algorithm; this newer paper extends smoothed polynomial bounds to general game graphs and does not mention the OpenAI release.
- [Bruno Loff and Mateusz Skomra, *Smoothed analysis of policy iteration and value iteration for deterministic discounted and mean-payoff games played on any graph*](https://arxiv.org/abs/2610.22149) (arXiv:2610.22149, 15 Oct 2026; accepted for SODA 2027). This paper's introduction contrasts its fixed inputs with the authors' earlier Gaussian-perturbation bounds on ergodic graphs; the new paper claims smoothed polynomial time on any game graph and does not mention the OpenAI release.

## Digests and expositions
- [Latent Seminar, *Quasipolynomial algorithms for mean-payoff games*](https://lowrank.github.io/latent-seminar/OpenAI-Math/104-mean-payoff-games) (7 October 2026). Explains the four manuscripts' potential comparisons, recursive methods, stochastic discounting, and parity strategy composition, explicitly without independently verifying the complete proofs. [family-level]
- [AI Proved What?, *Who wins in the long run?*](https://aiprovedwhat.com/episodes/104-quasipolynomial-mean-payoff-games/) (Episode 104, October 2026; status updated 19 October 2026). Provides an animated exposition and transcript covering all four claims, the binary-weight complexity distinction, and the reported limits of Lean coverage. [AI-generated per source] [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, 10 October 2026). Identifies family 104 among families whose formal statements cover less than the announced results, specifically flagging the deterministic algorithms and their extensions. [family-level]
