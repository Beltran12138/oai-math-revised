# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Eric Winnington, *Unbounded Integrality Gaps and Additive Hardness for the Skiving Stock Problem*](https://github.com/ewinnington/math/tree/main/MIRDP) (GitHub manuscript, 7 October 2026). Transfers this paper's bin-packing construction to the skiving stock problem by complementing item sizes, claiming unbounded additive gaps for the ordinary and proper pattern LPs (refuting Zak's modified integer round-down conjecture) and NP-hardness of fixed additive approximation. The manuscript is conditional on the source result and states that it does not independently re-establish the source proof or its Lean development. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Bin packing and unbounded configuration-LP gaps* (Lean scope note)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/118.md) (lean/docs/118.md). Describes the scope of the release's Lean formalization: the gap family with $5B$ items and both LP values (individual-copy and size-type configuration LPs) equal to $B$, NP-hardness for each fixed $c$, and the equivalence of deterministic constant-additive approximation with $P=NP$.
- [OpenAI, *ComparatorChallenges/BinPackingGap.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BinPackingGap.lean) (openai/math, commit adc7f12). The comparator statement `main_results` (stated with `sorry`) is a conjunction of four parts: the LP-gap family, `PackingGapNPHard c` for all `c`, the additive-algorithm iff `PEqualsNP` equivalence, and an exact algorithm under `PEqualsNP`.
- [OpenAI, *OAI/Computability/BinPacking/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Computability/BinPacking/Main.lean) (openai/math, commit adc7f12). Contains the proof of `OAI.BinPackingGap.main_results`, which assembles lemmas from other modules of the development.

## Related prior literature mentioned by others
- [John Martinovic and Guntram Scheithauer, *New theoretical investigations on the gap of the skiving stock problem*](https://www.scielo.br/j/pope/a/gbJztFmGWqVRp89qXS3ncpD/?lang=en) (Pesquisa Operacional, 2019). The skiving-stock follow-up cites it as a source stating Zak's modified integer round-down conjecture as open, which is the conjecture the follow-up targets with this paper's construction.
- [Rebecca Hoberg and Thomas Rothvoss, *A Logarithmic Additive Integrality Gap for Bin Packing*](https://arxiv.org/abs/1503.08796) (arXiv:1503.08796, 2015-03-30). The AI Proved What? exposition cites this logarithmic additive upper bound to explain why the paper's unbounded-gap claim does not supply a matching logarithmic lower bound.

## Possibly relevant literature (found by the agent, not checked)
- [Christoph Nitsche, Guntram Scheithauer and Johannes Terno, *New cases of the cutting stock problem having MIRUP*](https://api.crossref.org/works/10.1007%2FS001860050015) (Mathematical Methods of Operations Research 48(1):105–115, 1998). An earlier paper on instance classes that do satisfy the modified round-up bound that Theorem 1.1 refutes in general.
- [Klaus Jansen and Roberto Solis-Oba, *An OPT + 1 Algorithm for the Cutting Stock Problem with Constant Number of Object Lengths*](https://www.springerprofessional.de/en/an-opt-1-algorithm-for-the-cutting-stock-problem-with-constant-n/3290638) (IPCO 2010). An additive-one algorithm for a fixed number of distinct sizes, relating to the paper's remark that its at-most-five-items restriction does not fix the number of distinct sizes, a regime it contrasts with Goemans–Rothvoss.
- [Ruixue Yuan, Da Teng and Zhenyu Sun, *Additive Rounding for LP-Tight Three-Item Bin Packing*](https://hexagonmath.org/2610.00395v1) (hexagon:2610.00395v1, October 2026). Studies the maximum additive configuration-LP gap for LP-tight instances with sizes in $(1/4,1/2)$ (three items per bin), compared with the five-item-per-bin regime of Theorem 1.1; it does not mention this paper.

## Digests and expositions
- [AI Proved What?, *One more bin?*](https://aiprovedwhat.com/episodes/118-bin-packing-configuration-gap/) (episode 118, October 2026). The video and transcript explain the two claims and the vertex-cover reduction, distinguish unbounded gaps from a matching logarithmic lower bound, and state that the producers have not run the Lean check. [AI-generated per source]
- [Open Mathematics Courses, *Configuration gaps in bin packing*](https://kokunoyumeto.github.io/open-math-courses-public/courses/configuration-gaps-in-bin-packing/) (online course, undated). Six lessons develop the configuration programs, competing trees, scalar encoding, fractional packing and cover extraction, with proofs and exercises described as written and self-checked by Claude Opus 5.5 and not yet independently reviewed. [AI-generated per source]

## News and blogs
- None found.
