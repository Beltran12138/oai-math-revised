# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 280*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/280.md) (release documentation, 2026-10-06). According to these notes, the Lean statement covers only clause (1) of Theorem 1.1 (polynomial energy bounds, CKLW strong locality, irreducible conformal net), excluding complete rationality, complete unitarity, the braided tensor equivalence and the extension correspondence.
- [OpenAI math release, *VertexAlgebraNet.lean* (comparator challenge)](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/VertexAlgebraNet.lean) (github.com/openai/math, 2026). Comparator statement `OAI.MinimalVertex.main` for clause (1): for a simple, unitary, strongly rational CFT-type VOA, polynomial energy bounds, CKLW strong locality and an irreducible conformal net structure on the interval algebras; the proof is left as `sorry` in this challenge file. Comparator challenge files leave the proof as `sorry` by design; `VertexAlgebraNet.json` names the module `OAI.RepresentationTheory.VertexAlgebra.MinimalComparator` as the release's proof of this statement.
- [OpenAI math release, *MinimalComparator.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/RepresentationTheory/VertexAlgebra/MinimalComparator.lean) (github.com/openai/math, commit adc7f12). Solution module that proves the comparator statement `main` by reduction to `source_main_clause_one`, imported from `OAI.RepresentationTheory.VertexAlgebra.MainClauseOne`.

## Related prior literature mentioned by others
- [Sebastiano Carpi, Yasuyuki Kawahigashi, Roberto Longo and Mihály Weiner, *From vertex operator algebras to conformal nets and back*](https://arxiv.org/abs/1503.01260) (arXiv:1503.01260, 2015; revised 2018). The exposition by みしぇる沖 explicitly identifies this work as the correspondence framework underlying the manuscript's energy-bound and strong-locality claims.

## Possibly relevant literature (found by the agent, not checked)
- [B. Gui, *Unitarity of the modular tensor categories associated to unitary vertex operator algebras, I*](https://arxiv.org/abs/1711.02840) (arXiv:1711.02840, Commun. Math. Phys. 366 (2019)). Part I of the series whose Part II is cited; it constructs inner products on intertwining-operator spaces and studies energy bounds of intertwining operators, which relates to the complete-unitarity and charged-field-bound claims (Theorem 1.1(2)).
- [J. E. Tener, *Geometric realization of algebraic conformal field theories*](https://arxiv.org/abs/1611.01176) (arXiv:1611.01176, Adv. Math. 349 (2019)). Builds conformal nets from unitary VOAs via bounded localized operators obtained by geometric (Segal-type) smoothing, an alternative route to the vacuum-net construction in Theorem 1.1(1) and the annulus regularization of Section 3.
- [J. E. Tener, *Representation theory in chiral conformal field theory: from fields to observables*](https://arxiv.org/abs/1810.08168) (arXiv:1810.08168, Selecta Math. 25 (2019), 76). Extends geometric interpolation to modules and builds local intertwiners from VOA intertwining operators, which relates to the module-integration claim (Theorem 1.1(3)) and the fusion comparison.
- [B. Gui, *Categorical extensions of conformal nets*](https://arxiv.org/abs/1812.04470) (arXiv:1812.04470, Commun. Math. Phys. 383 (2021)). Introduces categorical extensions to compare the ribbon categories of unitary VOAs and conformal nets, a framework underlying the braided equivalence in Theorem 1.1(5).
- [Sebastiano Carpi and Tiziano Gaudio, *Conformal Nets from Minimal W-Algebras*](https://link.springer.com/article/10.1007/s00220-025-05468-2) (Communications in Mathematical Physics 406, article 300, 2025-10-30). Its strong graded locality and complete rationality results for strongly rational unitary minimal W-algebras provide a model-class comparison for Theorem 1.1(1) and (4), in the broader vertex-superalgebra and graded-local-net setting.

## Digests and expositions
- [みしぇる沖, *〖論文解説〗Strongly rational unitary vertex operator algebras and conformal nets〖OpenAI〗*](https://note.com/oki_math/n/n85bdb68fa0cd) (note.com, 2026-10-11). This Japanese exposition explains the distinction between locality of unbounded fields and strong locality of their generated algebras, then describes the manuscript's claimed unitarizability and representation-category correspondence.

## News and blogs
- None found.
