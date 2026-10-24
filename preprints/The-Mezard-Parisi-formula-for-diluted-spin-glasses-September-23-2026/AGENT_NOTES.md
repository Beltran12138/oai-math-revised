# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 221*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/221.md) (release documentation, 2026-10-06). States that the formalization proves convergence of the finite-system pressure to the infimum of the trial functional over all finite hierarchy depths and trial laws, for even arity at least two and positive density, and links the comparator statement `DilutedSpin.lean`.
- [OpenAI math release, *DilutedSpin.lean* (comparator statement)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/DilutedSpin.lean) (release Lean code, 2026-10-06). The formal statement of the Mézard–Parisi variational equality against which the release's Lean proof is checked.
- [OpenAI math release, *OAI/Probability/DilutedSpin/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/DilutedSpin/Main.lean) (openai/math at commit adc7f12). The solution module for the comparator challenge.

## Related prior literature mentioned by others
- [Dmitry Panchenko and Michel Talagrand, *Bounds for diluted mean-fields spin glass models*](https://arxiv.org/abs/math/0405357) (arXiv:math/0405357; Probability Theory and Related Fields 130, 2004). Identified as the source of the equality conjecture, stated after Theorem 4, that the release manuscript addresses.

## Possibly relevant literature (found by the agent, not checked)
- [D. Panchenko, *Hierarchical exchangeability of pure states in mean field spin glass models*](https://arxiv.org/abs/1307.2207) (arXiv:1307.2207; Probab. Theory Related Fields 161 (2015)). Identifies as the missing step toward the Mézard–Parisi ansatz that multi-overlaps of pure states depend only on their overlaps, which bears on the paper's stated main obstacle of controlling all finite multioverlaps.
- [D. Panchenko, *Structure of 1-RSB asymptotic Gibbs measures in the diluted p-spin models*](https://arxiv.org/abs/1308.1944) (arXiv:1308.1944; J. Stat. Phys. 155 (2014)). Earlier verification of the Mézard–Parisi ansatz for diluted p-spin models in the 1-RSB case, a precursor to the finite-RSB result [Pan16] that the paper cites.
- [S. Franz, M. Leone, F. L. Toninelli, *Replica bounds for diluted non-Poissonian spin systems*](https://arxiv.org/abs/cond-mat/0307367) (arXiv:cond-mat/0307367, 2003). Extends the Franz–Leone replica bounds beyond Poisson degree distributions and derives multi-overlap Ghirlanda–Guerra-type identities, relevant to the paper's restriction to Poisson dilution and to its multioverlap concentration step.

## Digests and expositions
- [OpenAI, *The Mézard–Parisi formula for diluted spin glasses — reasoning summary*](https://github.com/openai/math/blob/main/reasoning_traces/mezard-parisi-formula.tex) (OpenAI Math Release, 2026). The published summary describes the model's proposed route through marked Poisson perturbations, shifted branching depths, averaged multioverlap concentration, and truncation to first-moment disorder.

## News and blogs
- None found.
