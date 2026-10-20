# Automatically collected context

Collected by an AI agent (Claude Opus 5.5) on 2026-10-20. Not reviewed by a human; may be incomplete or wrong. Corrections: open an issue.

## Follow-up works
- None found.

## Expert comments and discussion
- [bocowgill, review of formal-conjectures PR #7440](https://github.com/google-deepmind/formal-conjectures/pull/7440) (2026-10-19). Approving reviewer states they checked the non-surjunctivity conclusion in Corollary 7.3 and Section 8 of the two direct-finiteness preprints and that the shift formula and continuity hold, while relying on reported build and axiom checks rather than rerunning the external proof.
- [Michael Chapman, in *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (proofsandprompts.com, 2026-10-08). Includes "the refutations to the Kaplansky conjectures" among the release items he reacts to; the remark is not specific to this manuscript.

## Formalization
- [OpenAI, *Lean scope note for family 197*](https://github.com/openai/math/blob/main/lean/docs/197.md) (openai/math release, 2026-10-06). The release formalizes the characteristic-two counterexample, including a finitely presented version with an element of odd prime order and a terminating search recipe; the nonsoficity conclusion is stated to be outside the formalized statements.
- [mo271 and others, *Wikipedia/SurjunctiveGroup: `gottschalk_surjunctivity_conjecture` is false*](https://github.com/google-deepmind/formal-conjectures/issues/6919) (formal-conjectures issue #6919, 2026-10-07 to 2026-10-19). Discussion of restating Gottschalk's conjecture as false, noting that the release's Lean proofs cover injectivity and non-surjectivity of the map but not continuity or shift-equivariance; a commenter (KevorkianPhilippe) supplied a Lean bridge for those properties.
- [KevorkianPhilippe, *fix(Wikipedia/SurjunctiveGroup): `gottschalk_surjunctivity_conjecture` is false*](https://github.com/google-deepmind/formal-conjectures/pull/7440) (formal-conjectures PR #7440, merged 2026-10-19). Restates the conjecture as false citing this manuscript and its odd-characteristic companion, links the release's `OAI.OddKaplansky.main_theorem`, and flags the continuity/equivariance step as not part of the linked proof.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, Chapter 3 "Nonsofic groups exist"](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) (OpenAI, 2026-08-01). An earlier claimed explicit nonsofic group (the unit group of the binary Leavitt algebra), relevant to the manuscript's remark that its group gives a finitely presented nonsofic example; this earlier work is not in the manuscript's bibliography.
- [Aadit Agrawal, *A Non-Sofic Group and the Fall of Connes's Rigidity Conjecture*](https://blog.ecitis.org/openai-sofic-groups-connes-rigidity/) (blog.ecitis.org, 2026-08-04). Exposition of the August nonsofic result that lists direct finiteness in positive characteristic and surjunctivity as open for that group.
- [Francesco Fournier-Facio, *A torsion-free non-sofic group*](https://arxiv.org/abs/2608.02025) (arXiv:2608.02025, August 2026). Gives further nonsofic examples, including torsion-free ones, via the same technical criterion as the August OpenAI result.
- [Gábor Kun, Andreas Thom, *Nonsofic wreath products of residually finite groups*](https://arxiv.org/abs/2608.06222) (arXiv:2608.06222, August 2026). Analyzes the mechanism behind the first nonsofic group and produces further nonsofic wreath products and group doubles.
- [Sauers, *A Surjunctive Group That Is Not Sofic*](https://data.palomar-registry.org/entries/PALOMAR-2026-09-14-000002-v1.json) (Palomar entry PALOMAR-2026-09-14-000002, [GitHub](https://github.com/SauersML/group-approximation), 2026-09-14). Lean formalization claiming a finitely generated surjunctive nonsofic group, which bears on how nonsoficity and non-surjunctivity relate for the manuscript's group.
- [Ken Dykema, Timo Heister, Kate Juschenko, *Finitely presented groups related to Kaplansky's Direct Finiteness Conjecture*](https://arxiv.org/abs/1112.1790) (arXiv:1112.1790, 2011). Introduces finitely presented "ULIE" groups that are universal for one-sided invertible elements in group rings and shows the conjecture can be tested on them, so the manuscript's construction may also be read in that framework; not in the manuscript's bibliography.
- [Henry Bradford, Francesco Fournier-Facio, *Hopfian wreath products and the stable finiteness conjecture*](https://arxiv.org/abs/2211.01510) (arXiv:2211.01510, 2022). Relates Kaplansky's stable finiteness conjecture to the Hopf property of wreath products, so a counterexample may have consequences there.

## Coverage
- [Zeli (Hacker News aggregator), *OpenAI drops 700 math preprints, many disproving famous conjectures*](https://zeli.app/story/49985740) (2026-10-06). Release summary that names the characteristic-two direct-finiteness counterexample among highlighted titles.
- [Kingy.ai, *OpenAI's 722 Math Manuscripts: The Results, Proofs, Compute and Costs*](https://kingy.ai/blog/openai-math-722-manuscripts-results-proofs-compute-costs/) (October 2026). Discusses families 196/197 and notes a scope difference between the family headline (torsion-free example) and the Lean scope page.
- [Hraness, *Mathematician reactions to OpenAI's 372 math results*](https://hraness.com/reading/mathematician-reactions-to-openais-372-math-results) (October 2026). Reproduces a ranked list by Will DePue (X) placing the family 197 counterexamples at #27.
- [OpenAI, *Reasoning summary for family 197*](https://github.com/openai/math/blob/main/reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf) (openai/math release, 2026-10-06). The release includes an abridged summary of the model's reasoning for this result.
- [Emergent Mind, *OpenAI Math Explorer: result 197*](https://www.emergentmind.com/openai-math-explorer/results/197) (catalogue page, October 2026). Third-party catalogue entry with an AI-generated explainer.
