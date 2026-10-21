# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Perfect completeness for 2-to-1 games* (Lean scope note)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/105.md) (lean/docs/105.md, October 2026). The release's scope note states that the formalized result is the full Theorem 1.1 reduction from binary 3SAT (fixed rational δ, value 1 vs. at most δ, exact two-element fibers, explicit unweighted constraints, runtime in the input bit length) and links the Comparator statement `ComparatorChallenges/PerfectCompleteness.lean`.

## Related prior literature mentioned by others
- [Yumou Fei, Dor Minzer and Shuo Wang, *On the Hardness of 4-to-1 Games with Perfect Completeness*](https://eccc.weizmann.ac.il/report/2026/179/) (ECCC TR26-179, 14 Sep 2026; revised 8 Oct 2026). Proves the perfect-completeness 4-to-1 analogue at arbitrarily small soundness and is cited by the paper; Fortnow's exposition and Quanta compare it with the 2-to-1 result, including their shared consequence for coloring three-colorable graphs with any fixed number of colors.

## Possibly relevant literature (found by the agent, not checked)
- [Dinur, Mossel, Regev, *Conditional Hardness for Approximate Coloring*](https://arxiv.org/abs/cs/0504062) (arXiv:cs/0504062, 2005). Derives hardness of approximate coloring (chromatic number at most q vs. at least Q, for q ≥ 4) from Khot's 2-to-1 conjecture, which bears on the paper's coloring consequences in Section 1.3; the paper does not cite it.

## Digests and expositions
- [Prepared with Claude for Lance Fortnow, *Perfect Completeness for 2-to-1 Games: An expository account of the proof*](https://github.com/fortnow/AI-Papers/blob/main/perfect-completeness-2-to-1-expository.tex) (github.com/fortnow/AI-Papers, 15 Oct 2026; [PDF](https://github.com/fortnow/AI-Papers/blob/main/perfect-completeness-2-to-1-expository.pdf)). An expository rewrite aimed at complexity theorists covering the tree of function spaces, partition-valued questions, the three soundness stages and the three external black-box theorems; it states that its author did not run the Lean check. [AI-generated per source]
- [Open Mathematics Courses, *2-to-1 games with perfect completeness*](https://kokunoyumeto.github.io/open-math-courses-public/courses/two-to-one-games-with-perfect-completeness/index.html) (undated). A ten-lesson exposition of the proof with examples and solved exercises that treats three external theorems as named hypotheses and identifies itself as written and self-checked by Claude Opus 5.5 with independent review incomplete. [AI-generated per source]

## News and blogs
- [Ben Brubaker (Quanta Magazine), *As AI Closed In on 'Unique Games' Proof, Researchers Raced to Beat the Machines*](https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/) (Quanta, 7 Oct 2026). Covers the race between the Fei–Minzer–Wang 4-to-1 paper and the OpenAI release, reporting that the release included a Lean-verified proof in an AI-generated manuscript that no independent experts had reviewed, and quotes Braverman and Minzer on AI-driven research.
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 7 Oct 2026). Item 18 identifies the perfect-completeness 2-to-1 announcement separately from Unique Games and connects it to Kalai's 2018 discussion of the 2-to-2 Games Theorem and the perfect-completeness question.
