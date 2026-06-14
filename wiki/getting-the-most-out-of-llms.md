---
title: "Getting the Most Out of LLMs: Retrieval, Storage, Coherence"
type: concept
created: 2026-06-08
updated: 2026-06-08
tags: [genai, rag, retrieval, memory, long-context, coherence, practical]
sources: [lewis-2020, gao-2023-survey, liu-2023-lost-middle, packer-2023-memgpt, asai-2023-selfrag]
---

# Getting the Most Out of LLMs

An LLM's weaknesses are structural ([[what-genai-is-good-and-bad-at]]), so the dependable gains come from the system you build around the model rather than from trusting the model more. The three levers that matter most line up with the three lenses in [[how-genai-works]]: improve what it can retrieve, give it storage beyond the context window, and design for long-term coherence. The through-line is to ground the model in real, curated, well-placed context instead of relying on its parametric recall.

## Retrieval: get the right facts into the window

[[rag-explained]] covers the basics. Plain RAG works ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)), but a naive version underperforms, and most 2023–24 research is about fixing its failure points. Two surveys map the field: [Gao et al. 2023](https://arxiv.org/abs/2312.10997) and the [2024 comprehensive survey](https://arxiv.org/abs/2410.12837). The techniques that help most:

- Hybrid search combines dense (embedding) retrieval with sparse keyword/BM25 search, so you catch both semantic and exact-term matches.
- Reranking reorders a noisy first-stage result with a cross-encoder, so the most relevant passages reach the prompt. The 2024 survey calls this one of the strongest steps for cutting hallucination ([survey](https://arxiv.org/abs/2410.12837)).
- Query rewriting and decomposition reshape the question into better retrieval queries before searching (for example, RQ-RAG).
- Corrective RAG (CRAG) grades fetched documents with an evaluator and discards or re-fetches the poor ones before they reach the model ([survey](https://arxiv.org/abs/2410.12837)).
- Self-RAG trains the model to decide when to retrieve, or to skip retrieval, and to check its own output against the evidence using reflection tokens, so retrieval is adaptive rather than always-on ([Asai et al. 2023](https://arxiv.org/abs/2310.11511)).
- GraphRAG builds an LLM-generated knowledge graph over the corpus and retrieves by traversing it, which supports corpus-wide, multi-hop questions that flat vector search misses ([Microsoft Research](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)).

## Storage: memory beyond the window

A model has only frozen weights (durable but fuzzy) and a volatile context window (precise but gone once it scrolls out), with no persistent memory by default ([[how-genai-works]] §Storage). You build that memory externally:

- MemGPT treats the window like RAM and an external store like disk, paging information in and out. This OS-style hierarchical memory turns a stateless model into a stateful agent ([Packer et al. 2023](https://arxiv.org/abs/2310.08560)).
- Later agent-memory work makes this production-ready, including [Mem0 (2025)](https://arxiv.org/abs/2504.19413) for scalable long-term memory and [A-Mem (2025)](https://arxiv.org/html/2502.12110v1) for self-organizing memory.
- Underneath, the store is usually a vector database for semantic recall, a knowledge graph for relational recall, or both. This is the persistent version of RAG's external memory.

## Long-term coherence: why a bigger context isn't the fix

Reaching for a huge context window is tempting, but it fails in documented ways:

- Models use information best at the beginning and end of the context and largely ignore the middle, and quality drops as the context grows, even for models built for long context ([Liu et al. 2023](https://arxiv.org/abs/2307.03172)). Stuffing everything in hurts; what you include and where you place it both matter.
- RAG and long context are not an either/or choice. Long-context models can win on raw quality when resources are unlimited, but RAG is cheaper and steadier, and curating the right slice often beats dumping everything in ([Li et al. 2025](https://arxiv.org/abs/2501.01880); [In Defense of RAG, 2024](https://arxiv.org/abs/2409.01666)).
- A working recipe: retrieve and curate the relevant slice, place the most important material at the edges, rerank to keep noise out, and hold continuity in external state (MemGPT-style) and running summaries instead of relying on the window to remember.

## The compounding move: an LLM-maintained wiki

A curated, LLM-maintained wiki, which is what this repo is, does all three at once and works better than plain RAG for building up knowledge over time:

- For storage, it puts knowledge into durable, structured markdown that persists across sessions, beyond the frozen weights and the volatile window. This is MemGPT's external context, but human-readable and curated ([Packer et al. 2023](https://arxiv.org/abs/2310.08560)).
- For retrieval, `index.md` and the topic pages act as a hand-curated layer: load the index, then open one already-synthesized page. You retrieve a compiled summary rather than raw chunks, which avoids the lost-in-the-middle problem ([Liu et al. 2023](https://arxiv.org/abs/2307.03172)). The `[[wikilinks]]` form a small knowledge graph, which is the GraphRAG idea ([Microsoft](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)).
- For coherence, the wiki is the persistent state. Contradictions are flagged once, cross-references stay maintained, and the synthesis accumulates. Each session re-grounds from the wiki, so the knowledge is compiled once and kept current rather than re-derived on every query.

The trade-off is that a wiki is curated memory, so it costs upkeep (which is the kind of bookkeeping an LLM is good at absorbing), and it is only as reliable as its sourcing and maintenance.

## Deep-dive reading by area

A fuller, annotated list for going deeper in each area.

### Retrieval

- Karpukhin et al. (2020), *Dense Passage Retrieval (DPR)*, https://arxiv.org/abs/2004.04906. The dual-encoder dense retriever that beat BM25, and the base most RAG retrievers build on.
- Khattab & Zaharia (2020), *ColBERT* (and *ColBERTv2*, 2021), https://arxiv.org/abs/2004.12832 and https://arxiv.org/abs/2112.01488. Late interaction: token-level matching, more precise than single-vector embeddings.
- Gao et al. (2022), *HyDE: Precise Zero-Shot Dense Retrieval*, https://arxiv.org/abs/2212.10496. Generate a hypothetical answer first and embed that to retrieve, closing the query-to-document gap with no labels.
- Sarthi et al. (2024), *RAPTOR*, https://arxiv.org/abs/2401.18059. Recursively cluster and summarize chunks into a tree, so retrieval can grab the right level of abstraction. Strong on multi-step QA.
- Jiang et al. (2023), *FLARE: Active Retrieval*, https://arxiv.org/abs/2305.06983. Retrieve during generation whenever the next sentence looks low-confidence, not only once at the start.
- Yan et al. (2024), *Corrective RAG (CRAG)*, https://arxiv.org/abs/2401.15884. Grade retrieved documents and fall back to web search when they are poor.
- Edge et al. (2024), *From Local to Global: GraphRAG*, https://arxiv.org/abs/2404.16130. The paper behind GraphRAG: a knowledge graph plus community summaries for corpus-wide questions.

### Storage & memory

- Guu et al. (2020), *REALM*, https://arxiv.org/abs/2002.08909. First to learn a retriever inside pretraining, treating retrieval as memory learned end-to-end.
- Borgeaud et al. (2022), *RETRO*, https://arxiv.org/abs/2112.04426. Chunked cross-attention to a large datastore matched GPT-3-class quality with about 25 times fewer parameters, letting external memory stand in for parameters.
- Izacard et al. (2022), *Atlas*, https://arxiv.org/abs/2208.03299. A retrieval-augmented model whose knowledge store can be updated independently of the generator.
- Wu et al. (2022), *Memorizing Transformers*, https://arxiv.org/abs/2203.08913. A kNN lookup into a memory of past key-value pairs, so the model can memorize new data at inference time.
- Wang et al. (2023), *LongMem*, https://arxiv.org/abs/2306.07174. A decoupled side-network that caches long history (to about 65k tokens) without memory staleness.
- Park et al. (2023), *Generative Agents*, https://arxiv.org/abs/2304.03442. The influential memory-stream design: score memories by recency, relevance, and importance, and periodically write higher-order reflections. See also [[how-genai-works]].

### Long context & coherence

- Liu et al. (2023), *Lost in the Middle*, https://arxiv.org/abs/2307.03172. Models use the start and end of context best and ignore the middle. The motivating result for everything above.
- Chen et al. (2023), *Position Interpolation*, https://arxiv.org/abs/2306.15595. Cleanly extend a RoPE model's context window (for example to 32k) with minimal fine-tuning.
- Xiao et al. (2023), *StreamingLLM*, https://arxiv.org/abs/2309.17453. Keep a few initial attention "sink" tokens to stream to millions of tokens stably, without retraining.
- Munkhdalai et al. (2024), *Infini-attention*, https://arxiv.org/abs/2404.07143. A compressive memory inside attention for bounded-memory long context, with passkey recall at 1M tokens.
- Hsieh et al. (2024), *RULER*, https://arxiv.org/abs/2404.06654. A benchmark showing the usable context is far shorter than the advertised window. Use it to sanity-check long-context claims.

## Putting it together

Rather than trusting the model's memory, engineer its context: retrieve the right facts and rerank them, give it persistent external storage, and curate what enters the window instead of maximizing window size. Over a long project, a maintained wiki folds all three into a single artifact that keeps improving.

## Sources

- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* https://arxiv.org/abs/2005.11401
- Gao, Y. et al. (2023). *Retrieval-Augmented Generation for Large Language Models: A Survey.* https://arxiv.org/abs/2312.10997
- (2024). *A Comprehensive Survey of Retrieval-Augmented Generation (RAG).* https://arxiv.org/abs/2410.12837
- Asai, A. et al. (2023). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection.* https://arxiv.org/abs/2310.11511
- GraphRAG, Microsoft Research. https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/
- Liu, N. et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* https://arxiv.org/abs/2307.03172
- Packer, C. et al. (2023). *MemGPT: Towards LLMs as Operating Systems.* https://arxiv.org/abs/2310.08560
- Mem0 (2025). *Building Production-Ready AI Agents with Scalable Long-Term Memory.* https://arxiv.org/abs/2504.19413
- A-Mem (2025). *Agentic Memory for LLM Agents.* https://arxiv.org/html/2502.12110v1
- Li, X. et al. (2025). *Long Context vs. RAG for LLMs: An Evaluation and Revisits.* https://arxiv.org/abs/2501.01880
- (2024). *In Defense of RAG in the Era of Long-Context Language Models.* https://arxiv.org/abs/2409.01666
