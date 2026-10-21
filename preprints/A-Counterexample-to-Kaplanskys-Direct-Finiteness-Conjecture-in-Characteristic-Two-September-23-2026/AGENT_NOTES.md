# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [Michael Chapman, in *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (proofsandprompts.com, 2026-10-08). Lists "the refutations to the Kaplansky conjectures" among the release results on problems he "grew up on", without discussing this manuscript in detail. [family-level]

## Formalization
- [OpenAI, *Lean scope note for family 197* (`lean/docs/197.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/197.md) (openai/math release, 2026-10-06). States that the formalization covers the characteristic-two counterexample, including a finitely presented version with an element of odd prime order and a terminating search recipe; nonsoficity is outside the formalized statements.
- [mo271, KevorkianPhilippe and others, *Wikipedia/SurjunctiveGroup: `gottschalk_surjunctivity_conjecture` is false*](https://github.com/google-deepmind/formal-conjectures/issues/6919) (formal-conjectures issue #6919, 2026-10-07 to 2026-10-19). Proposes restating Gottschalk's conjecture as false on the basis of this preprint and its odd-characteristic companion; the release's Lean proofs cover injectivity and non-surjectivity but not continuity or shift-equivariance, for which a commenter supplied a Lean bridge, and a commenter notes the finitely presented group appears only in the characteristic-two Lean statement.
- [KevorkianPhilippe, *fix(Wikipedia/SurjunctiveGroup): `gottschalk_surjunctivity_conjecture` is false*](https://github.com/google-deepmind/formal-conjectures/pull/7440) (formal-conjectures PR #7440, merged 2026-10-19). Restates the conjecture as false, citing this preprint and the odd-characteristic companion and flagging that continuity and shift-equivariance are not part of the linked proof; the approving reviewer (bocowgill) says they checked the non-surjunctivity conclusions (Corollary 7.3) and "relied on the reported build and axiom checks without independently rerunning the external proof."
- [The Formal Conjectures Authors, *Gottschalk’s surjunctivity conjecture — SurjunctiveGroup.lean*](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/Wikipedia/SurjunctiveGroup.lean) (GitHub, accessed 21 October 2026). This Lean statement file cites both characteristic companions but retains `sorry` in the counterexample declarations and notes that the linked odd-characteristic proof omits continuity and shift equivariance. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, Chapter 3 "Nonsofic groups exist"](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) (OpenAI, updated 2026-08-06). An earlier claimed explicit nonsofic group; relevant to the introduction's statement that this construction "supplies a finitely presented counterexample to the assertion that every group is sofic."
- [Francesco Fournier-Facio, *A torsion-free non-sofic group*](https://arxiv.org/abs/2608.02025) (arXiv:2608.02025, August 2026). Further nonsofic examples, including finitely presented ones, from the same technical criterion as the August OpenAI result; relevant to the nonsoficity consequence of Theorem 1.1.
- [Michal Doucha, Jakub Gismatullin, *On dual surjunctivity and applications*](https://arxiv.org/abs/2008.10565) (arXiv:2008.10565, 2020). Proves that dual surjunctive groups satisfy direct finiteness over all fields of positive characteristic, so Theorem 1.1 would also imply that $G$ is not dual surjunctive; complements the surjunctivity discussion in Section 7.
- [Ken Dykema, Timo Heister, Kate Juschenko, *Finitely presented groups related to Kaplansky's Direct Finiteness Conjecture*](https://arxiv.org/abs/1112.1790) (arXiv:1112.1790, 2011). Introduces finitely presented "ULIE" groups that are universal for one-sided inverses in group rings, which may be compared with the finitely presented group of Theorem 1.1; not in this preprint's bibliography, although the torsion-free companion cites it.
- [Henry Bradford, Francesco Fournier-Facio, *Hopfian wreath products and the stable finiteness conjecture*](https://arxiv.org/abs/2211.01510) (arXiv:2211.01510, 2022). Relates Kaplansky's stable finiteness conjecture to the Hopf property of wreath products, so a counterexample may have consequences there.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090v1) (arXiv:2610.17090, 2026-10-12). Section 8.4.2 summarizes this construction: the incidence criterion (Thm 3.1), the polynomial pairing (Prop 2.3), the hole trades with the local lemma, and the HNN packing. It also lists caveats, for example that the prescription was not executed; per the paper, the first extraction for each family used AI readings.
- [OpenAI, *reasoning summary `kaplansky-direct-finiteness-characteristic-two.pdf`*](https://github.com/openai/math/blob/main/reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf) (openai/math release, 2026-10-06). An abridged summary of the model's reasoning for this result, included in the release. [AI-generated per source]
- [AI Proved What?, *One-sided inverse? Kaplansky’s direct-finiteness conjecture*](https://aiprovedwhat.com/episodes/197-torsion-free-group-algebra-not/) (Episode 197, October 2026). This illustrated exposition compares all four papers, explains their construction ideas, and distinguishes their claims and formalization scope. [AI-generated per source] [family-level]

## News and blogs
- [Vinod Chugani, *OpenAI's AI Math Breakthroughs: What the Latest Results Mean*](https://www.datacamp.com/blog/openai-math-breakthroughs-what-the-latest-results-mean) (DataCamp, 2026-10-08). Has a short section on this characteristic-two result, noting that a Lean formalization is listed.
- [Kingy.ai, *OpenAI's 722 Math Manuscripts: The Results, Proofs, Compute and Costs*](https://kingy.ai/blog/openai-math-722-manuscripts-results-proofs-compute-costs/) (October 2026). Discusses family 197 and contrasts the torsion-free headline with the Lean scope page, which covers the characteristic-two and odd-characteristic constructions with torsion. [family-level]
- [Hraness, *Mathematician reactions to OpenAI's 372 math results*](https://hraness.com/reading/mathematician-reactions-to-openais-372-math-results) (October 2026). Reproduces a ranked list by Will DePue (X) placing the family 197 counterexamples at #27. [family-level]
