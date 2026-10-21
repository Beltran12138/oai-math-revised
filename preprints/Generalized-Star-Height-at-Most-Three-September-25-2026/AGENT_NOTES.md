# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Elias Botsford, *Generalized Star Height One for Computations via Run Padding*](https://zenodo.org/records/23254500) (Zenodo preprint, doi:10.5281/zenodo.23254500, 2026-10-09). States that it is motivated by the release's claim that every regular language has generalized star height at most three and studies a complementary height-one phenomenon (run padding, actions with at most one nontrivial cycle per letter). [family-level]

## Comments and discussion
- [gignico on Hacker News, comment in the thread "Sharing AI progress in mathematics"](https://news.ycombinator.com/item?id=49989310) (Hacker News, 2026-10-07). Quoting this paper's title, the commenter calls it "an open problem in automata theory I worked on for more than one year before giving up" and says they are curious about the proof.
- [rnbnnnn on Hacker News, *Three nested stars suffice in generalized regex [pdf]*](https://news.ycombinator.com/item?id=50174042) (Hacker News story 50174042, 2026-10-20). A link post to this paper's PDF, accompanied only by a short poem from the submitter and no further discussion.

## Formalization
- [mathcommunity/oai-math-revised, *lean/docs/134.md: Generalized star height at most three*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/134.md) (release Lean scope notes). Says the formalization proves that every regular language over a finite alphabet has a generalized expression over the same alphabet of star height at most three, with complement in the same free monoid. [family-level]
- [OpenAI, *lean/OAI/Computability/StarHeight/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Computability/StarHeight/Main.lean) (openai/math repository). Contains the theorem `OAI.GeneralizedStarHeight.main`, stating `HasHeightAtMost L 3` for every regular `L` over a finite alphabet, reduced via `OAI.Computability.StarHeight.Recognition` to finite-monoid recognition and `FiniteRecognition.recognized_height_three`. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Jean-Éric Pin, *Open problems about regular languages, 35 years later*](https://cs.uwaterloo.ca/%7Eshallit/DC2015/pin.pdf) (talk slides, Brzozowski 80, 2015-06-24). Slides 9–10 note that no language of generalized star height greater than one was known and recall that if the height-at-most-one languages form a variety then all regular languages have height at most one; this bears on the paper's remark that it does not decide whether height one always suffices.

## Digests and expositions
- [Azmat, *Generalized Star Height Problem: How OpenAI’s Two-Split Proof Sets a Three-Level Ceiling*](https://binaryverseai.com/generalized-star-height-problem-openai-proof/) (Binary Verse AI, 2026-10-18). Explains this manuscript’s two splits, shift tables and suffix decoder, situates the companion bounds of thirteen and four, and distinguishes exposition from an independent correctness audit.
- [Wikipedia, *Generalized star-height problem*](https://en.wikipedia.org/wiki/Generalized_star-height_problem) (encyclopedia article, accessed 2026-10-21). Cites this paper and describes the bound of three as a claim from the October 6, 2026 release, noting that whether the bound can be lowered to two or one remains open.

## News and blogs
- None found.
