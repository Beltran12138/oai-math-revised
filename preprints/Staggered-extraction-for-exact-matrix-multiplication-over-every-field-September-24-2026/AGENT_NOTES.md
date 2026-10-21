# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Matrix multiplication with exponent at most 9/4 — Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/107.md) (OpenAI math release, lean/docs/107.md, 2026-10-06). Lists this paper as accompanying the Lean development, which records the unconditional bound $\omega(F)<2.371054886006746$ for every field, counting additions, subtractions and multiplications in division-free programs, with no numerical inequalities left as hypotheses. [family-level]
- [Jeroen Zuiddam, *ω(F) ≤ 9/4 over every field, in Lean*](https://github.com/jzuiddam/omega-nine-quarters-all-fields) (Lean 4 repository, verification reported 2026-10-07). Generalizes the family’s complex $9/4$ proof to every field through modified Fourier periods and descent, reporting kernel and Comparator verification and disclosing Claude assistance. [family-level]
- [Sela Navot, *Matrix multiplication over arbitrary fields*](https://github.com/selanavot/matrix-multiplication-all-fields) (Lean 4 repository, verification reported 2026-10-06). Extends the family’s $9/4$ proof to arbitrary fields, with exact coefficient identities, positive-slack operation bounds and documented kernel replay, developed by GPT-6 Astra and GPT-6.1 Sol under Navot’s direction. [AI-generated per source] [family-level]
- [Sela Navot, *Matrix multiplication: ω ≤ 9/4 over every ring*](https://github.com/selanavot/omega_le_nine_quarters_all_rings) (Lean 4 repository, version 0.1.0; accessed 2026-10-21). Extends the family’s $9/4$ construction through exact integer tensor identities to division-free programs over arbitrary associative unital rings, including noncommutative rings, with verification records and an accompanying manuscript. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Oliver Proudfoot and Andrew Perrault (olliepro), *LeanMMBound: Cross-Level Laser Extraction for Faster Matrix Multiplication formalized in Lean*](https://github.com/olliepro/LeanMMBound) (GitHub, 2026-10-07). Independent Lean-checked bound ω < 2.3710449 over every commutative ring, obtained by sharing extraction across recursion levels of the laser method; relevant to this paper's all-fields bound ω < 2.371054886 and its cross-depth joint extraction. [AI-generated per source]
- [Reza Bosagh Zadeh, *A faster matrix multiplication algorithm through structured optimization*](https://arxiv.org/abs/2610.10593) (arXiv:2610.10593, 2026-10-06). Claims ω < 2.37115924 by further optimization within the combination-loss framework, improving on Dupont et al.; relevant as a contemporaneous laser-method bound to compare with this paper's ω < 2.371054886.

## Digests and expositions
- None found.

## News and blogs
- [Carlos Toledo, *OpenAI’s math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, 2026-10-10). Entry F-214 reports certification of the paper’s finite parameter calculation from five integer arrays, distinguishing that calculation from the full asymptotic theorem.
