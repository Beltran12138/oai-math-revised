# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [JohnDriscollAcademic and maintainer MColbrook, AIM (Open Applied Problems) pull request #35, *Update Vlasov-Maxwell problem with new findings*](https://github.com/MColbrook/AIM/pull/35) (GitHub, 7–13 Oct 2026). The problem tracker records this paper as resolving AIM 073 ("Large-data global classical solutions of relativistic Vlasov–Maxwell"). The maintainer notes that the linked comparator theorem ends in `by sorry` and that AIM therefore claims no Lean-verified status. [AI-generated per source]
- [kieransquared1, *Comment on “OpenAI drops 722 math papers written by internal reasoning model”*](https://www.reddit.com/r/Physics/comments/1wzgqwn/comment/pecerhy/) (r/Physics, accessed 2026-10-21). The commenter, who identifies themselves as a mathematician working in this area, reports that nonstandard terminology and notation make the manuscript's central idea difficult to identify; their expertise is self-reported.

## Formalization
- [OpenAI math release, *Lean scope note 362: Global smoothness for relativistic Vlasov–Maxwell*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/362.md) (family 362, release 2026-10-06). The scope note says the formalized statement covers global existence, smoothness on finite horizons, compact phase support and uniqueness among classical solutions, with no smallness, symmetry or neutrality assumption, and links the VlasovMaxwell comparator statement. [AI-generated per source] [family-level]
- [OpenAI, *lean/OAI/Analysis/VlasovMaxwell/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Analysis/VlasovMaxwell/Main.lean) (openai/math, Oct 2026). The main declaration `OAI.RVM.global_classical_solution` is derived from `global_classical_of_uniform_physical_increment`, with the development split into subfolders (Continuation, Flow, Geometry, LocalPDE, Maxwell, Population, Regularity, Retarded).
- [OpenAI, *lean/ComparatorChallenges/VlasovMaxwell.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/VlasovMaxwell.lean) (openai/math, Oct 2026). The standalone comparator statement `global_classical_solution (d : Datum) (hd : Admissible d)`, with the proof left as `sorry`; it is the file referred to in the AIM discussion above.
- [MathVet, *Family 362 formalization review and checking record*](https://math.vet/openai-math/data.json) (review of openai/math at fd4aeeb2, generated 2026-10-20). The family-specific record rates the formal statement as matching the headline and reports a sandboxed Comparator pass, while the project's methodology identifies the reading as AI-assisted and pre-referee. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Xuecheng Wang, *Global solution of the 3D relativistic Vlasov-Maxwell system for the large radial data*](https://arxiv.org/abs/2003.14192) (arXiv:2003.14192, 2020). Proves large-data global existence under spherical symmetry, bearing on the paper's survey of symmetric and large-data results, which cites only the same author's cylindrical-symmetry papers.
- [Markus Kunze, *Yet another criterion for global existence in the 3D relativistic Vlasov-Maxwell system*](https://arxiv.org/abs/1406.1517) (arXiv:1406.1517, 2014). A continuation criterion based on an $L^2_x$ bound for a velocity-averaged quantity, related to the continuation criteria listed in the paper's introduction.
- [Neel Patel, *Three New Results on Continuation Criteria for the 3D Relativistic Vlasov-Maxwell System*](https://arxiv.org/abs/1607.07416) (arXiv:1607.07416, 2016). Refines the Kunze and Luk–Strain continuation criteria, including a version with a time-varying support plane, related to the Luk–Strain results the paper cites.
- [Christophe Cheverry and Slim Ibrahim, *The relativistic Vlasov-Maxwell system: Local smooth solvability for weak topologies*](https://arxiv.org/abs/2306.11812) (arXiv:2306.11812, 2023). Local smooth solvability via a representation formula for momentum spreading, related to the paper's local existence and uniqueness step; the Xie survey reports that the release's reasoning summary cites it, although the paper does not.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090v1) (arXiv:2610.17090, 12 Oct 2026). Section 8.2.3 summarizes the paper's new tools (signed momentum-increment bootstrap, Prop. 2.1; signed force identity along source labels, Lemma 6.1; direction-change counting and selection, §§4, 7, 8) and lists caveats, including a small margin in the exponent comparison and a discrepancy between the paper and the reasoning summary. [family-level]
- [Azmat, *Vlasov Maxwell System: How OpenAI Tackled a Decades-Old Plasma Physics Problem*](https://binaryverseai.com/vlasov-maxwell-system-openai-global-regularity/) (Binary Verse AI, 2026-10-11). Walks through the manuscript's signed momentum cancellation, direction and occupation estimates, bootstrap closure and momentum-doubling argument, and discusses the scope of the claimed result.

## News and blogs
- [Kingy AI, *OpenAI's 722 Math Manuscripts: The Results, Proofs, Compute and Costs*](https://kingy.ai/blog/openai-math-722-manuscripts-results-proofs-compute-costs/) (blog, Oct 2026, updated 9 Oct). A section on family 362 sketches the signed-momentum-increment and doubling-time strategy and notes that the reasoning summary itself says the cited continuation theorem does not supply the new estimates. [family-level]
