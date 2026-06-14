# Log — GenAI Knowledge Base

Append-only. Each entry: `## [YYYY-MM-DD] <op> | <title>`. Quick tail: `grep "^## \[" log.md | tail -5`.

## [2026-06-04] init | Wiki scaffolded
Created CLAUDE.md schema, index.md, log.md, and raw/ + wiki/{concepts,comparisons,sources} dirs. Principles set: technical-but-accessible depth, mandatory sourcing, objective (non-sycophantic) tone.

## [2026-06-04] ingest | First research pass — GenAI mechanisms, capabilities, limits, non-GenAI AI
Web-researched and wrote 10 wiki pages, all with inline citations + Sources sections: overview; concepts/{what-is-genai, how-llms-work, how-image-and-diffusion-models-work, training-and-scaling, hallucination-and-reliability, non-genai-ai, reading-list}; comparisons/{genai-vs-humans, genai-vs-classical-ai}. ~18 primary papers cited. Flagged 3 live conflicts: emergence vs mirage (Wei vs Schaeffer); GPT-4 bar-exam percentile (Katz vs Martinez); Bitter Lesson vs Sutton's 2025 LLM skepticism.

## [2026-06-04] lint | Cross-reference check
Verified all [[wikilinks]] resolve to existing page slugs; no broken links, no orphans. Gap noted: wiki/sources/ has no per-paper pages yet (bibliography is in reading-list.md). Next-session candidates: agents/tool-use deep dive; mixture-of-experts & modern architectures; multimodal models; AI safety/alignment; energy & cost; Chinchilla-era data scaling.

## [2026-06-04] update | Restructured how-llms-work into Storage / Retrieval / Interaction
Reorganized the page into 4 parts: Mechanism, Storage (parametric weights, embeddings, context window, KV cache, external store), Retrieval (attention-as-lookup, parametric recall, in-context, RAG), Interaction (prompting/ICL, chat+system prompts, decoding controls, tools/ agents). Added 2 sources: Mikolov 2013 (word2vec/embeddings), Lewis 2020 (RAG). Added both to reading-list. All wikilinks still resolve.

## [2026-06-04] note | Wiki purpose for now = GenAI "actually good at / actually bad at"
Per Amal: current goal is a sharp, evidence-based read on real GenAI strengths vs weaknesses; the strengths feed the **Arthur Sugden project**. Primary page for this: [[genai-vs-humans]] (plus [[genai-vs-classical-ai]] for tool-fit). TODO: confirm what the Arthur Sugden project is so the "good at" list can be tailored to it.

## [2026-06-04] ingest | Lee & Trott (2023) "LLMs Explained" + cited research
Created wiki/sources/lee-trott-2023-llm-explained.md: summary, full bibliography of the article's cited research (word2vec, Caliskan 2017 bias, Tenney 2019, Wang/Redwood 2022 IOI, Geva 2020 FFN-as-memory, Merullo 2023, Kosinski 2023 ToM, Ullman 2023, Bubeck 2023 Sparks-of- AGI), and a "where it has dated" analysis citing newer work: Anthropic Scaling Monosemanticity (2024), DeepSeek-R1 (2025), Strachan 2024 (Nature Hum Behav ToM), GPT-4 MoE, Chinchilla, Schaeffer mirage. Added a mechanistic-interpretability subsection to how-llms-work. Added Tier 3.5 to reading-list. Updated index.

## [2026-06-04] query | Where is the Lee & Trott article outdated?
Answered in chat + filed as the "where it has dated" section of the source page. 7 areas: interpretability progress, RL-trained reasoning models, ToM nuance, Sparks-of-AGI as conflicted source, emergence-as-mirage, GPT-3 no longer archetype (MoE), Kaplan superseded by Chinchilla.

## [2026-06-07] restructure | Collapsed to a tight core (de-bloat)
Per Amal ("current wiki is bloated"): reduced 14 pages -> 5. New core: how-genai-works.md (Storage/Retrieval/Interaction + brief training & image gen), what-genai-is-good-and-bad-at.md, reading-list.md (slimmed). Merged-in & deleted: overview, what-is-genai, how-llms-work, how-image-and-diffusion, training-and-scaling, hallucination-and-reliability, non-genai-ai, genai-vs-humans, genai-vs-classical-ai. Kept source page (lee-trott-2023). Updated index + CLAUDE.md (flat wiki/, "keep it lean" rule). Old content recoverable via file history if needed.

## [2026-06-08] ingest | Expanded wiki into Kirton's Adaption-Innovation model
Researched Kirton A-I (1976/2003): continuum (adaptive "do better in-paradigm" vs innovative "do differently / paradigm shift"), style != level, KAI 3-factor (Sufficiency of Originality, Efficiency, Rule/Group conformity) + Im&Hu 4-factor debate. Added 2 pages: kirton-adaption-innovation.md (primer) and genai-on-the-adaption-innovation-spectrum.md (synthesis: GenAI = high-LEVEL, ADAPTIVE-style; how adaptors vs innovators use it; human-AI team composition). Thesis: GenAI is a "high-level adaptor" — explains the good/bad-at split in Kirton's terms. Counterpoint flagged: cross-domain recombination looks innovative but is in-paradigm interpolation; genuinely paradigm-shifting AI (AlphaGo move 37) is RL/non-genai, not generative. Cross-linked from what-genai-is-good-and-bad-at + index + reading-list.

## [2026-06-08] ingest | Added "Getting the Most Out of LLMs" + plain RAG explainer
New pages: getting-the-most-out-of-llms.md (retrieval: hybrid search, reranking, query rewriting, CRAG, Self-RAG, GraphRAG; storage: MemGPT/Mem0/A-Mem, vector DBs/KGs; coherence: lost-in-the-middle, RAG-vs-long-context; + the LLM-maintained-wiki as a do-all pattern) and rag-explained.md (beginner, open-book analogy). Added retrieval/memory papers to reading-list. Sources: Lewis 2020, Gao 2023 + 2024 surveys, Asai 2023 (Self-RAG), Liu 2023 (Lost in the Middle), Packer 2023 (MemGPT), Mem0/A-Mem, GraphRAG, Long-Context-vs-RAG (2025), In Defense of RAG (2024). Updated index + log.

## [2026-06-08] ingest | Deep-dive papers for retrieval / storage / coherence
Added "Deep-dive reading by area" to getting-the-most-out-of-llms.md (all arXiv IDs verified): Retrieval — DPR (2004.04906), ColBERT (2004.12832 / v2 2112.01488), HyDE (2212.10496), RAPTOR (2401.18059), FLARE (2305.06983), CRAG (2401.15884), GraphRAG paper (2404.16130). Storage/memory — REALM (2002.08909), RETRO (2112.04426), Atlas (2208.03299), Memorizing Transformers (2203.08913), LongMem (2306.07174), Generative Agents (2304.03442). Long context — Position Interpolation (2306.15595), StreamingLLM (2309.17453), Infini-attention (2404.07143), RULER (2404.06654). Cross-linked from reading-list.

## [2026-06-08] setup | Obsidian vault scaffolding
Added SETUP.md (open-as-vault steps, plugins, daily loop, git), .gitignore (OS + Obsidian workspace/cache), and wiki/dashboard.md (Dataview tables: all pages, concepts, comparisons, sources, tags). Verified frontmatter is consistent across all 8 content pages (type/updated/ tags present) so Dataview works. Linked SETUP + dashboard from index under "Using this wiki".

## [2026-06-08] edit | De-AI voice pass across the wiki
Rewrote all reader-facing pages in a plainer voice: removed em-dash overuse (titles/headers now use colons), the "not just X but Y" construction, fragment-conclusions (Bottom line / The pattern / Net), bold-label bullets, and filler words (genuinely, robust, leverage, crucial, tellingly). Added a Voice section to CLAUDE.md so future pages follow the same style. All citations, links, and facts preserved; all wikilinks still resolve. log.md left as the historical record.

## [2026-06-08] format | Reflowed hard-wrapped lines
Unwrapped the manual ~100-char line breaks across all markdown files so each paragraph, list item,
and callout body is a single line (no mid-sentence newlines in the raw files). Left frontmatter,
fenced code blocks, headings, list structure, and callout titles untouched. Verified: all wikilinks
resolve, code fences balanced, frontmatter pairs intact, both callouts preserved.

## [2026-06-08] setup | GitHub-visible static catalog + Action
Dataview dashboard.md does not run on GitHub (shows raw query code). Added a GitHub-friendly path:
scripts/build_catalog.py reads page frontmatter and writes wiki/catalog.md (a plain markdown table
that renders on github.com); .github/workflows/build-catalog.yml rebuilds and commits it on every
push (with [skip ci] to avoid loops). Kept dashboard.md for live use in Obsidian. Linked catalog
from index.md and README.md. All links verified.
