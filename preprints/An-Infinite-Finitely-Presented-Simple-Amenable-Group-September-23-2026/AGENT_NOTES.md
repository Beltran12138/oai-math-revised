# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Matthew C. B. Zaremsky, *Some open problems*](https://zaremsky.github.io/open_problems.pdf) (author's problem list, version dated October 8, 2026). The paper cites the July 12, 2026 version (Problem 10, "Find a finitely presented (or F∞), infinite, simple, amenable group."); in the October 8 version this problem is struck through with the note "Update 10/8/26: I'll just cross out problems solved by AI." [cites earlier version]

## Formalization
- [OpenAI math release, *Lean scope notes for family 253*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/253.md) (lean/docs/253.md, 2026-10-06). The release's scope note: the Lean result is the bare existence statement, with amenability in Følner form; the paper's later general claims about central kernels and enlargements across families are not covered.
- [OpenAI, *lean/OAI/GroupTheory/SimpleAmenable/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/SimpleAmenable/Main.lean) (github.com/openai/math, commit adc7f12). Lean theorem `main` asserting that some group satisfies `Infinite G ∧ Group.IsFinitelyPresented G ∧ IsSimpleGroup G ∧ FolnerAmenable G`.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Mustafa Gökhan Benli, Rostislav Grigorchuk and Pierre de la Harpe, *Amenable groups without finitely presented amenable covers*](https://link.springer.com/article/10.1007/s13373-013-0031-5) (Bulletin of Mathematical Sciences 3, 73–131, 2013). Studies obstructions to amenable finitely presented covers, including Problem 1.12 for the Juschenko–Monod simple amenable groups, which is background for the paper's finitely presented central cover of its polygon exchange group.
- [Kate Juschenko, Volodymyr Nekrashevych, Mikael de la Salle, *Extensions of amenable groups by recurrent groupoids*](https://arxiv.org/abs/1305.2637) (arXiv:1305.2637; Invent. Math. 206 (2016)). A general amenability criterion based on recurrent orbital Schreier graphs covering full groups of Cantor minimal systems, relevant to the paper's comparison of its amenability argument with the Juschenko–Monod and extensive-amenability methods.
- [Hiroki Matui, *Topological full groups of one-sided shifts of finite type*](https://arxiv.org/abs/1210.5800) (arXiv:1210.5800, 2012). Shows that full groups of one-sided irreducible shifts of finite type are of type F∞ with simple commutator subgroups, contrasting with the minimal-subshift case the paper discusses via Matui 2006.
- [Volodymyr Nekrashevych, *Finitely presented groups associated with expanding maps*](https://arxiv.org/abs/1312.5654) (arXiv:1312.5654, 2013). Constructs finitely presented groups of dynamical origin with simple commutator subgroups, relevant to the paper's strategy for obtaining finite presentation for full-group-type groups.

## Digests and expositions
- None found.

## News and blogs
- None found.
