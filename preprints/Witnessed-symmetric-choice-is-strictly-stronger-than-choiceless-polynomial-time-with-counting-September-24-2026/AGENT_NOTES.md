# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Lean scope notes for family 243*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/243.md) (release documentation, October 2026). The first scope paragraph says the witnessed-symmetric-choice result is not included, while a second paragraph and a comparator link (WitnessedChoice.lean) in the same notes describe a formalization of this result. [family-level]
- [OpenAI, *ComparatorChallenges/WitnessedChoice.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/WitnessedChoice.lean) (openai/math, commit adc7f12). States `WitnessedChoice.main : BGS.MainStatement`, proof left as `sorry` in this file: there is a sentence with exactly one `wsc` operator that is Boolean on all finite inputs, and no `wsc`-free sentence has the same models.
- [OpenAI, *OAI/Computability/WitnessedChoice/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Computability/WitnessedChoice/Main.lean) (openai/math, commit adc7f12). Proves `main : BGS.MainStatement` by instantiating the separating sentence and evaluating it on a zero-charge grid input (true) and a unit-charge input (false).

## Related prior literature mentioned by others
- [Andreas Blass, Yuri Gurevich and Saharon Shelah, *Choiceless polynomial time*](https://arxiv.org/abs/math/9705225v1) (arXiv:math/9705225v1, 15 May 1997). The AI Proved What? exposition identifies this work as the source of the choiceless model and the counting noncapture conjecture motivating the family. [family-level]
- [Anuj Dawar, David Richerby and Benjamin Rossman, *Choiceless Polynomial Time, Counting and the Cai–Fürer–Immerman Graphs*](https://www.cl.cam.ac.uk/~ad260/papers/CPT-CFI.pdf) (author preprint, 13 August 2007; Annals of Pure and Applied Logic, 2008). The AI Proved What? exposition contrasts this work's rank-restricted counting lower bounds with the family's claimed separation allowing unrestricted finite set rank. [family-level]
- [Moritz Lichter and Pascal Schweitzer, *Choiceless Polynomial Time with Witnessed Symmetric Choice*](https://arxiv.org/abs/2205.14003v3) (arXiv:2205.14003v3, 10 February 2023). The AI Proved What? exposition attributes to these authors the witnessed-choice operator whose strict expressive gain over CPT with counting is claimed in this paper.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [AI Proved What?, *Is there a logic for polynomial time?*](https://aiprovedwhat.com/episodes/243-choiceless-polynomial-time/) (episode 243, October 2026). This AI-assisted video and transcript outline both separating queries, the charged-grid construction and the rank-independent support argument, and report small-grid computations performed for the exposition. [AI-generated per source] [family-level]

## News and blogs
- None found.
