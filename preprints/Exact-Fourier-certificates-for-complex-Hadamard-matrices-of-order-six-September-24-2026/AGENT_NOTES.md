# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Hao-Yu Sun, *Mutually unbiased bases: common states, completion, and extension obstructions*](https://arxiv.org/abs/2610.12180) (arXiv:2610.12180, 2026-10-08). Cites this preprint alongside its companion, states "Neither preprint is a premise of the proofs in this article," and proves an unextendibility result for a specific dimension-six MUB triple. [family-level]

## Comments and discussion
- [mo271 and commenters, *OpenQuantumProblems/13: `mutuallyUnbiasedBases_dim6` has answer 3*](https://github.com/google-deepmind/formal-conjectures/issues/6918) (google-deepmind/formal-conjectures issue #6918, opened 2026-10-07). A comment of 2026-10-11 reports a re-implementation of this paper's μ(6) ≤ 5 certificate from the LaTeX in exact rational arithmetic, with matching table sizes and ranks; the comment says the Lean proof was not built. [family-level] [AI-generated per source]

## Formalization
- [OpenAI math release, Lean scope note for family 266](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/266.md) (lean/docs/266.md, 2026). The release's Lean development proves the Fourier vanishing statement for order-six Hadamard matrices not equivalent to Tao's matrix, a family bound of five, and a supporting cube-fiber cancellation lemma (`MUBSix.lean`, `HadamardCubeFiber.lean`), distinguishing these from the companion paper's exclusion of four arbitrary bases. [family-level]
- [Google DeepMind formal-conjectures, *FormalConjectures/OpenQuantumProblems/13.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/OpenQuantumProblems/13.lean) (GitHub, accessed 2026-10-21). Marks the variant `mutuallyUnbiasedBases_dim6_bounds.variants.upper_five` (μ(6) ≤ 5) research solved with a `formal_proof` link to the release's Lean proof and cites this preprint, while leaving the dimension-six maximum open with `sorry`. [cites earlier version] [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Anonymous, *No Szöllősi matrix lies in a quadruplet of mutually unbiased bases in dimension six*](https://zenodo.org/records/23051062) (Zenodo, unrefereed preprint, 2026-09-30). Claims to exclude the Szöllősi family from MUB quadruplets, which bears on the MMVW conjecture mentioned in this paper's introduction (Conjecture 3 and Proposition 4.2 of MatolcsiEtAl2025).
- [Gary McConnell, Harry Spencer, Afaq Tahir, *Evidence for and against Zauner's MUB Conjecture in ℂ⁶*](https://arxiv.org/abs/2103.08703) (arXiv:2103.08703, 2021). Finite-field evidence on bounds for MUBs in dimension six, a context for Theorem 1.2's bound N(6) ≤ 5.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090v1) (arXiv:2610.17090, 2026-10-12). Section 9.3.4 describes the phase cover, tangent refinement and companion Fourier certificates, distinguishes their formalization scopes, and states that the headline computation was not independently rerun for this survey. [AI-generated per source] [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit dated 2026-10-10). Entry F-533 reports exact checks of the single-matrix, cubic-pair and mixed-moment finite certificates at release commit fd4aeeb2, while the separate MUBSix kernel-check entry records that its job stopped before Comparator ran. [cites earlier version]
