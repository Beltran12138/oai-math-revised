# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release / oai-math-revised, *Lean scope notes for family 279*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/279.md) (lean/docs/279.md, 2026). The release's scope document describes the formalization as a uniform circuit family over a fixed finite gate set that outputs the complete prime factorization with probability exactly one, with polynomial-time uniformity and polynomial worst-case gate and qubit bounds.
- [OpenAI, *ExactQuantumFactoring.lean* (comparator challenge statement)](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/ExactQuantumFactoring.lean) (github.com/openai/math, 2026). Lean statement `exact_quantum_factoring : MainTheorem` with 20 fixed gate names (NOT, CNOT, Toffoli, Hadamard, phase, with inverse and single-control flags), TM2-based polynomial-time uniformity, polynomial qubit and instruction bounds, and success probability exactly 1; the proof in this challenge file is `sorry` by design. `ExactQuantumFactoring.json` names the module `OAI.Computability.QuantumFactoring.Main` as the release's proof of this statement.
- [OpenAI, *OAI/Computability/QuantumFactoring/Main.lean* (solution module)](https://github.com/openai/math/blob/main/lean/OAI/Computability/QuantumFactoring/Main.lean) (github.com/openai/math, 2026). Proves `exact_quantum_factoring` by assembling `PhysicalTree.finalCircuit` with its uniformity, resource and correctness lemmas from imported files.

## Related prior literature mentioned by others
- [M. Mosca and C. Zalka, *Exact quantum Fourier transforms and discrete logarithm algorithms*](https://arxiv.org/abs/quant-ph/0301093) (arXiv:quant-ph/0301093, 2003; Int. J. Quantum Inf. 2004). Azmat's Binary Verse AI exposition names their exact algorithms with computed gate parameters as background to the paper's fixed-finite-gate claim; the work is also cited in the paper as [MZ].

## Possibly relevant literature (found by the agent, not checked)
- [M. Imran, *Exact quantum splitting and the structure of finite algebras*](https://arxiv.org/abs/2608.30340) (arXiv:2608.30340, v1 31 Aug 2026, v2 16 Oct 2026). Exact quantum polynomial splitting over finite fields using one exact Grover iteration with an input-dependent rotation after a test with known success probability; compare with the paper's exact amplification from success probability exactly 1/4 using fixed gates only.
- [M. Imran and G. Ivanyos, *An exact quantum hidden subgroup algorithm and applications to solvable groups*](https://arxiv.org/abs/2202.04047) (arXiv:2202.04047, 2022). Exact HSP algorithm using the Mosca–Zalka exact QFT, an example of exact algorithms in parameterized-gate models, which the paper's introduction (Section 1.1) contrasts with its fixed finite gate set.
- [J.-Y. Cai, *Shor's Algorithm Does Not Factor Large Integers in the Presence of Noise*](https://arxiv.org/abs/2306.10072) (arXiv:2306.10072, 2023; Sci. China Inf. Sci. 2024). Shows that Shor's factoring fails under vanishing random noise in controlled-rotation gates; relevant to the paper's statement that approximating arbitrary-angle rotations does not yield probability-one correctness.
- [J.-Y. Cai and B. Young, *Quantum Algorithms for Discrete Log Require Precise Rotations*](https://arxiv.org/abs/2412.17269) (arXiv:2412.17269, 2024; ACM Trans. Quantum Comput. 2025). Extends Cai's noise result to Shor's discrete-log algorithm; concerns the precision of the rotations that the paper's construction avoids.

## Digests and expositions
- [Azmat, *Exact Quantum Factoring: How OpenAI’s Fixed-Gate Proof Turns 25% Into Certainty*](https://binaryverseai.com/exact-quantum-factoring-openai-proof/) (Binary Verse AI, 2026-10-17). Paper-specific exposition of the four-phase order trial, dyadic probability corrections, auxiliary factorizations, deferred filters and final amplitude-amplification step, distinguishing the claimed circuit bounds from practical hardware estimates.

## News and blogs
- None found.
