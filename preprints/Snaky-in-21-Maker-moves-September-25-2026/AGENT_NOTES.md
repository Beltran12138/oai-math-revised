# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Nándor Sieben, *Snaky: Proof sequence for Snaky*](https://github.com/nandorsieben/Snaky) (GitHub repository, 2026). Gives proof sequences (files `proof-sequence-18/19/20.html.gz`) in the sense of Sieben's proof-tree paper; the README says they are based on strategies described in this paper, and the 20-move sequence was later formalized in the gotrevor project.
- [Trevor Morris (gotrevor), *snaky-15x15: Snaky is a first-player win on 15x15*](https://github.com/gotrevor/snaky-15x15) (GitHub Lean development, October 2026). Reports kernel-checked theorems `Snaky.snaky_wins_15x15` and `Snaky.snaky_wins_17x17_in_20` and a Breaker win on 9×9, narrowing the smallest winning square-board size to between 10 and 15 after the paper's 17×17 bound. [AI-generated per source]

## Comments and discussion
- [edpegg, *Comment on “First look at mathematics manuscripts from an internal frontier model at OpenAI”*](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886/5) (OpenAI Developer Community, 2026-10-07). Briefly welcomes the Snaky solution and suggests making the strategy available as a playable game.

## Formalization
- [OpenAI math release, *Lean scope notes for result 187*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/187.md) (lean/docs/187.md, 2026). The release's own Lean development: a legal Maker strategy that wins within 21 Maker moves on the empty infinite board (excluding the finite-board restriction), plus reconstructions of the 35-move certificate and four conditional templates.
- [Trevor Morris (gotrevor), *Snaky: Maker wins on 17×17 within 20 moves*](https://github.com/gotrevor/snaky-15x15/blob/main/docs/notes/snaky-17x17.md) (GitHub formalization notes, 2026). Explains the conversion of Sieben's 1,510 situations into 1,738 cards and the kernel check of `snaky_wins_17x17_in_20` (no `native_decide`), describing it as a refinement of this paper's strategy rather than an optimality result. [AI-generated per source]

## Related prior literature mentioned by others
- [Nándor Sieben, *Proof trees for weak achievement games*](https://math.colgate.edu/~integers/ig7/ig7.pdf) (Integers 8, G07, 2008). Sieben's follow-up repository points to this paper for the definition of its proof sequences, connecting the new strategies with the earlier proof-tree method and handicap-one Snaky construction.
- [Immanuel Halupczok and Jan-Christoph Schlage-Puchta, *Achieving Snaky*](https://math.colgate.edu/~integers/hg2/hg2.pdf) (Integers 7, G02, 2007). The gotrevor notes and Binary Verse AI exposition cite its 8×8 loss, three-dimensional win and planar handicap-one win as predecessors to the unhandicapped planar result.

## Possibly relevant literature (found by the agent, not checked)
- [Ian Norris and Nándor Sieben, *Biased Weak Polyform Achievement Games*](https://arxiv.org/abs/1107.1878) (arXiv:1107.1878, 2011). Shows that winning Maker strategies can be built from games with fewer marks, which may relate to the paper's composition rule for conditional winning positions.

## Digests and expositions
- [ian52n, *snaky-21-move-cards*](https://github.com/ian52n/snaky-21-move-cards) (GitHub repository, 2026). An interactive viewer for the 728 cards of this paper's 21-move certificate, with a Breaker-reply simulator; it rechecks all cards on each load.
- [KaiaSage, *snaky-demo*](https://github.com/KaiaSage/snaky-demo) (GitHub repository, 2026). An interactive game that implements this paper's Maker strategy from its Appendix D certificate; it also includes a "Snaky in 20" variant, which the README calls an unreviewed draft. [AI-generated per source]
- [heyprof, *Snaky in 21 moves*](https://www.heyprof.app/en/demo/snaky-maker-strategie) (interactive exposition, undated). Presents a playable Maker–Breaker demonstration described as following the paper's embedded proof certificate, with displays for threats, protected regions and the remaining move allowance.
- [OpenAI Math Digest, *Snaky in 21 Maker moves*](https://masataka123.github.io/OpenAI-Math-Digest/ja/papers/snaky-in-21-maker-moves/) (Japanese exposition, 2026-10-15 reference edition). Explains the combination lemma, finite certificate, legal policy and finite-board corollary, and reports rerunning two author-supplied Python reconstruction programs while excluding Lean compilation from its checks. [AI-generated per source]

## News and blogs
- [Azmat, *Snaky in 21 Maker Moves: How OpenAI's Proof Ended a 47-Year Tic-Tac-Toe Mystery*](https://binaryverseai.com/snaky-in-21-maker-moves/) (Binary Verse AI, 2026-10-15). Discusses the paper's conditional winning positions, 728-card certificate and 17×17 corollary, and distinguishes the reported infinite-board Lean scope from finite-board claims.
- [kaiasky (reblogged on Centrally Unplanned), *Recently I have heard a bunch of people discussing...*](https://centrally-unplanned.tumblr.com/post/777761085255303168/recently-i-have-heard-a-bunch-of-people-discussing) (Tumblr post, undated on page). An informal post on the 21-move result: it notes that optimality is not established and links to a playable demo.
- [Wikipedia, *Harary's generalized tic-tac-toe*](https://en.wikipedia.org/wiki/Harary%27s_generalized_tic-tac-toe) (encyclopedia article, accessed 2026-10-21). States that in October 2026 OpenAI claimed to have proven Snaky a winner in 21 moves, and cites this preprint.
