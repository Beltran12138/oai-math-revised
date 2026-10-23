# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Frederico Cançado, *AC-zoo-results* (notes and reports on weak forms of choice)](https://github.com/frederico-cancado/AC-zoo-results) (GitHub repository, notes dated 7 October 2026 and later). Preliminary notes that take this paper's model construction as their "external source" and derive a finite-basis property for the injection order on cardinalities in that model; the author states they were prepared with substantial OpenAI Codex assistance and have not been externally reviewed.

## Comments and discussion
- [Asaf Karagila, *OpenAI, the Partition Principle, and mathematics*](https://karagila.org/2026/openai-pp/) (blog post, 8 October 2026). After a brief look, a set theorist who has long worked on this problem criticizes the preprint's exposition, structure, terminology and references (including Lemmas 7.4 and 8.1) and calls it "unclear, muddled, and has a strange structure"; he does not assess whether the result is correct and reports no mathematical error.
- [Asaf Karagila, *Why I don't trust Lean code from AI*](https://karagila.org/2026/lean/) (blog post, 10 October 2026). A follow-up post explaining why he does not intend to read or run the AI-generated Lean proof accompanying this paper, while accepting that formalising the statement itself is "easy enough to do right".
- [Hacker News discussion of Karagila's post, *OpenAI, the Partition Principle, and Mathematics*](https://news.ycombinator.com/item?id=50013902) (Hacker News, 8 October 2026). A long thread that is mostly about AI in mathematics in general; a few comments discuss what the Lean proof attached to this result does and does not establish.
- [Elliot Glazer (@ElliotGlazer), post on X](https://x.com/ElliotGlazer/status/2107600021655032184) (6 October 2026). Says the result means his refutation of the (Weak) Partition Principle in New Foundations is "nonvacuous after all".
- [Hanul Jeon (@hanuljeon95), post on X](https://x.com/hanuljeon95/status/2107627039780151787) (7 October 2026). Remarks that the apparently fully AI-generated paper is "quite readable" and asks whether OpenAI selected readable papers or the model itself produces them.
- [Elliot Glazer (@ElliotGlazer), thread on X](https://x.com/ElliotGlazer/status/2108598549160349836) (9 October 2026). Says Lemma 7.4, flagged by Karagila, is trivial, being the converse of "if P(A)\{{}} has a choice function, then A is well-orderable", and notes the paper thereby reproves Zermelo's theorem.
- [Sridhar Ramesh (@RadishHarmers), post on X](https://x.com/RadishHarmers/status/2108607620244287775) (9 October 2026). Criticizes the paper for "invoking Foundation here just to be able to talk about a partial function into A".

## Formalization
- [OpenAI math release, *Lean scope notes for result 244*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/244.md) (lean/docs/244.md). The release's own Lean formalization proves Con(ZF) → Con(ZF + PP + ACwo + ¬AC); its transitive-model construction assumes a countable transitive ground model containing an internal strongly inaccessible cardinal and does not cover the paper's stronger transitive-model preservation assertions. [AI-generated per source]
- [google-deepmind/formal-conjectures issue #4581, *Does the Partition Principle imply the Axiom of Choice over ZF?*](https://github.com/google-deepmind/formal-conjectures/issues/4581) (GitHub issue, opened 23 July 2026). Proposes a Lean statement of the open question that this paper answers; when checked it had no comments or linked pull requests.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Adonai S. Sant'Anna, Otávio Bueno, Márcio P. P. de França, Renato Brodzinski, *Flow: the Axiom of Choice is independent from the Partition Principle*](https://arxiv.org/abs/2010.03664) (arXiv:2010.03664, October 2020). An earlier claimed PP + ¬AC result in a non-standard framework ("Flow"); not among the earlier approaches discussed in the paper's history section, which treats only Gilson's withdrawn preprints.
- [Andrzej Pelc, *On some weak forms of the axiom of choice in set theory*](https://pelc.uqo.ca/pelc/1978.html) (Bull. Acad. Polon. Sci. Sér. Sci. Math. Astronom. Phys. 26 (1978), 585–589). The paper cites the implication PP ⇒ ACwo only through Ryan-Smith's account of an argument "attributed to Pincus by Pelc"; this is the Pelc paper in question (the abstract on this page does not name PP).
- [Calliope Ryan-Smith, *Eccentricity, extendable choice and descending distributive forcing*](https://arxiv.org/abs/2506.11607) (arXiv:2506.11607, June 2025). Constructs symmetric extensions with control from distributivity; possibly relevant to the claim in Theorem 1.2 that the symmetric model adds no new countable sequences of ground-model elements.
- [Asaf Karagila, *On the Partition Principle*](https://karagila.org/2014/on-the-partition-principle/) (blog post, 20 December 2014). Surveys the history of PP from Burali-Forti and Russell onward and the known consequences PP ⇒ ACwo ⇒ DC; complements the paper's brief historical section.

## Digests and expositions
- [AI Proved What?, *No more pieces than points, yet no choice?*](https://aiprovedwhat.com/episodes/244-partition-principle-not-choice/) (episode 244, October 2026; status updated 2026-10-17). A short video and transcript explaining the distinction between reverse injections and choice functions and outlining the manuscript's reduction, symmetric model and coherent quotient bijections. [AI-generated per source]

## News and blogs
- [Remy, *OpenAI Math's Correction Week: What a Passing Lean Proof Actually Verifies*](https://redreamality.com/blog/ai-math-verification-lean-faithfulness/) (blog, 9 October 2026). Discusses Karagila's critique of this paper and the Comparator challenge for the Partition Principle result, including its 277-line statement file and its axiom allow-list (propext, Quot.sound, Classical.choice).
- [Equipo Ecosistema Startup, *Karagila a OpenAI: 'No enviaré whisky por ese paper'*](https://ecosistemastartup.com/karagila-a-openai-no-enviare-whisky-por-ese-paper/) (Spanish-language news site, 8 October 2026). Mainly a rewrite of Karagila's blog post criticising this paper, with no independent reporting.
- [Proofs and Prompts, *Essays by Asaf Karagila about the OpenAI announcement*](https://proofsandprompts.com/newsfeed/) (newsfeed entry, 2026-10-11). Identifies result 244 and links Karagila's two essays discussing its presentation and Lean proof.
