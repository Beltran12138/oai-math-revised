# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Elias Botsford, *Generalized Star Height One for Computations via Run Padding*](https://zenodo.org/records/23254500) (Zenodo preprint, doi:10.5281/zenodo.23254500, 2026-10-09). States that it is motivated by the release's claim that every regular language has generalized star height at most three and studies a complementary height-one phenomenon; it does not name this specific paper. [family-level]

## Comments and discussion
- None found.

## Formalization
- [mathcommunity/oai-math-revised, *lean/docs/134.md: Generalized star height at most three*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/134.md) (release Lean scope notes). Says the formalization proves the uniform bound three, which implies this paper's bound of thirteen, and does not encode the paper's construction steps separately. [family-level]
- [OpenAI, *lean/OAI/Computability/StarHeight/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Computability/StarHeight/Main.lean) (openai/math repository). Contains the theorem `OAI.GeneralizedStarHeight.main`, stating `HasHeightAtMost L 3` for every regular `L` over a finite alphabet, reduced to finite-monoid recognition and `FiniteRecognition.recognized_height_three`. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Jean-Éric Pin, *Open problems about regular languages, 35 years later*](https://cs.uwaterloo.ca/%7Eshallit/DC2015/pin.pdf) (talk slides, Brzozowski 80, 2015-06-24). Slides 9–10 note that no language of generalized star height greater than one was known and recall that if the height-at-most-one languages form a variety then all regular languages have height at most one; this bears on the paper's distinction between uniform boundedness and the height-one question.

## Digests and expositions
- [Azmat, *Generalized Star Height Problem: How OpenAI’s Two-Split Proof Sets a Three-Level Ceiling*](https://binaryverseai.com/generalized-star-height-problem-openai-proof/) (Binary Verse AI, 2026-10-18). Explains the height-three manuscript’s two splits, shift tables and suffix decoder, situates the companion bounds of thirteen and four, and distinguishes exposition from an independent correctness audit. [family-level]

## News and blogs
- None found.
