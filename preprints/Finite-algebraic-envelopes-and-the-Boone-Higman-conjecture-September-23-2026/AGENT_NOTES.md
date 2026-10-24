# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Matt Zaremsky, reaction in *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (Proofs and Prompts, 2026-10-08). Zaremsky says the release shows that his group's sufficient condition for the Boone–Higman conjecture "always works" and compares its affine-like action mechanism to their 2025 advance; the reaction is also critical of how the result was released. [family-level]
- [Peter Cameron, comment on *A fable*](https://cameroncounts.wordpress.com/2026/10/09/a-fable/) (Peter Cameron's Blog, 9 October 2026). Cameron connects the announced Boone–Higman result to Bleak and collaborators' hyperbolic-group theorem while cautioning that the new claims were not yet established truth.

## Formalization
- [OpenAI math release, *Lean scope notes for family 250* (lean/docs/250.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/250.md) (OpenAI math release, 2026-10-06). The release's scope notes state that the Lean development proves the full equivalence in Theorem 1.1 (computable word problem for a finite generating set iff an embedding into a finitely presented simple group), with the comparator statement in `lean/ComparatorChallenges/BooneHigman.lean`. [family-level]
- [lean-eval benchmark, *Kuznetsov's theorem: finitely presented simple groups have solvable word problem* (`boone_higman_simple`)](https://lean-lang.org/eval/problems/boone_higman_simple/) (Lean FRO lean-eval benchmark, undated). An independent Lean benchmark statement of the classical ingredient behind the implication (ii)⇒(i) of Theorem 1.1; on the page the proof is `sorry`.
- [lean-eval benchmark, *Boone–Higman theorem (easy direction)* (`boone_higman_embedding`)](https://lean-lang.org/eval/problems/boone_higman_embedding/) (Lean FRO lean-eval benchmark, undated). An independent Lean benchmark statement of the easy direction of Boone–Higman's Theorem I (stated there for finitely presented G), which the paper cites as [BH74, Theorem I]; on the page the proof is `sorry`.

## Related prior literature mentioned by others
- [James Belk, Collin Bleak, Francesco Matucci and Matthew C. B. Zaremsky, *Hyperbolic groups satisfy the Boone–Higman conjecture*](https://arxiv.org/abs/2309.06224) (arXiv:2309.06224, 2023; v3, 20 August 2025). This hyperbolic-group special case is the earlier advance highlighted by Cameron in his discussion of the release. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Francesco Fournier-Facio, Xiaolei Wu, Matthew C. B. Zaremsky, *Abstract twisted Brin–Thompson groups*](https://arxiv.org/abs/2603.24687) (arXiv:2603.24687, 2026-03-25). Its abstract says that, if the Boone–Higman conjecture holds, a related conjectural characterization of groups with solvable word problem within twisted Brin–Thompson groups follows; this is relevant to the consequences of Theorem 1.1.
- [Matthew C. B. Zaremsky, *Embedding finitely presented self-similar groups into finitely presented simple groups*](https://arxiv.org/abs/2405.09722) (arXiv:2405.09722, accepted to Bull. London Math. Soc.). A previously known positive case of the conjecture (groups embedding in finitely presented self-similar groups, including finitely generated subgroups of GL_n(Q)), not among the positive cases listed in the introduction.
- [Mailton Rego Almeida, Alex Carrazedo Dantas, Altair Santos de Oliveira-Tosti, *On the Self-Similarity of Permutational Wreath Products and Their Embedding into Finitely Presented Simple Groups*](https://arxiv.org/abs/2609.01868) (arXiv:2609.01868, 2026-09-01). A further recent positive case of the conjecture (certain wreath products Z^d ≀_X G), not among the positive cases listed in the introduction.
- [Fan Wu, Xiaolei Wu, Mengfei Zhao, Zixiang Zhou, *Embedding groups into boundedly acyclic groups*](https://arxiv.org/abs/2407.07703) (arXiv:2407.07703, to appear in J. London Math. Soc.). Uses twisted Brin–Thompson groups to embed every finitely generated group in a finitely generated (boundedly acyclic) simple group, which compares with the introduction's discussion of Thompson's finitely generated simple overgroups.

## Digests and expositions
- [AI Proved What?, *Decidable means simple inside? Three AI preprints claim the Boone–Higman conjecture*](https://aiprovedwhat.com/episodes/250-boone-higman-conjecture/) (episode 250, October 2026). This AI-assisted video and transcript distinguish the three claimed results and outline the affine-action and higher-finiteness constructions. [AI-generated per source] [family-level]

## News and blogs
- [Azmat, *Boone Higman Conjecture Proof: How OpenAI Bridges the Finite-Presentation Gap*](https://binaryverseai.com/boone-higman-conjecture-openai-proof/) (Binary Verse AI, 13 October 2026). The article traces this manuscript's algebra, affine Steinberg group, kernel-annihilation and mapping-torus construction, while distinguishing reported formalization from independent verification.
