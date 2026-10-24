# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-23.

## Follow-up works
- None found.

## Comments and discussion
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*, Combinatorics and more](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (blog, 2026-10-07). Lists this paper among the release's results, saying it "gives counterexamples to the original conjecture, even among graphs with independence number at most two", and notes the earlier disproof of the odd-minor strengthening.

## Formalization
- [OpenAI, Lean scope note for family 157 (`lean/docs/157.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/157.md) (openai/math release, 2026-10-06). The release's formalization proves $h(G)<26m/75+2/3<m/2\le\chi(G)$ for arbitrarily large graphs with $\alpha(G)\le2$; the fractional strengthening and the Colin de Verdière consequence are stated to be outside its scope. [family-level]
- [Edouard Bonnet, *hadwiger-counterexample*](https://github.com/EdouardBonnet/hadwiger-counterexample) (GitHub; local kernel replay reported 2026-10-11). Lean development that vendors the release's construction and, per its README, also derives the fractional-chromatic consequence (`FractionalCounterexample.lean`); submitted to the Lax archive as `lax-342547`.

## Related prior literature mentioned by others
- [Marcus Kühn, Lisa Sauermann, Raphael Steiner, Yuval Wigderson, *Disproof of the Odd Hadwiger Conjecture*](https://arxiv.org/abs/2512.20392) (arXiv:2512.20392, 2025-12-23). Earlier disproof of the odd-minor strengthening, which Kalai's post connects to this result (the manuscript also cites it).
- [Freddie Illingworth and Raphael Steiner, *Disproof of the dominating Hadwiger conjecture*](https://arxiv.org/abs/2609.35361) (arXiv:2609.35361, 2026-09-28). Xie's survey, Section 8.3.3, compares this AI-discovered construction with the manuscript's independence-two examples while distinguishing dominating clique models from ordinary clique minors. [AI-generated per source]

## Possibly relevant literature (found by the agent, not checked)
- [Jofre Costa, Eric Luu, David R. Wood, Jung Hon Yip, *Verifying Hadwiger's Conjecture for Examples of Graphs with α(G) = 2*](https://arxiv.org/abs/2512.17114) (arXiv:2512.17114, 2025-12-18). Surveys and extends tools for Hadwiger's conjecture in the $\alpha(G)=2$ setting of Theorem 1.1 and proves variants for inflations of specific graph classes.
- [António Girão, Sergey Norin, Youri Tamitegama, Jane Tan, *Two Relaxations of the Dominating Hadwiger's Conjecture*](https://arxiv.org/abs/2608.12126) (arXiv:2608.12126, 2026-08-12). Studies the Illingworth–Wood dominating strengthening of Hadwiger's conjecture, which Corollary 1.2 would also refute if correct.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090v1) (arXiv:2610.17090, 2026-10-12). Section 8.3.3 describes the hole relation, the entropy-minimizing container argument and the collision machinery, rating the method "new" and noting that "the argument gives neither an explicit graph nor an explicit clique-minor number"; the survey states it did not compile the Lean development. [AI-generated per source]

## News and blogs
- [Azmat, *Hadwiger Conjecture: How OpenAI's Counterexample Proof Breaks an 83-Year-Old Coloring Rule*](https://binaryverseai.com/hadwiger-conjecture-openai-counterexample/) (BinaryVerse AI, 2026-10-18). Explains the manuscript's parity construction, four-hole obstruction and connected-matching bound, and distinguishes the documented ordinary-counterexample formalization from the fractional-coloring claim.
