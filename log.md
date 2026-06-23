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

## [2026-06-14] enrich | Added source-grounded specifics (verified)
Per Amal ("add direct detail from the sources; only use the sources, don't make things up"), added
concrete figures, each verified against the primary source this session:
- how-genai-works: attention formula softmax(QK^T/sqrt(d_k))V; transformer base config (6+6 layers,
  d_model 512, 8 heads, 28.4/41.8 BLEU); GPT-3 (175B, 96 layers, 12288, 96 heads, 2048 ctx, ~300B
  tokens); RAG (DPR+BART, 21M Wikipedia passages, top-5); InstructGPT (13k SFT, 33k RM, 1.3B>175B);
  Kaplan (200+ models, 7 orders); Chinchilla (20 tok/param, 70B/1.4T beat Gopher 280B); DDPM (IS 9.46,
  FID 3.17 CIFAR-10). Added kaplan/hoffmann/rombach sources. Dropped an unverified "1000 steps" figure.
- what-genai: USMLE ~86.7% vs ~53% GPT-3.5 and ~60% pass; UBE ~297/400; Martinez breakdown (~68th
  overall vs 90th, ~48th/~15th vs passers); Blocksworld ~1/3 -> near zero on Mystery, GPT-3.5 ~0.7%;
  Schaeffer >92%; Ji intrinsic/extrinsic. Added LLM-Modulo (2402.01817) source.
- getting-most: Lost-in-the-middle 75/72/55% + <56% closed-book; RETRO 2T-token datastore.
- kirton: KAI scoring (range 32-160, midpoint 96, mean ~95, SD ~16, alpha 0.84-0.89). Added Bobic 1999.
Bumped updated dates; regenerated catalog; all links resolve; no em-dashes introduced.

## [2026-06-14] setup | Added Interviews section
Created wiki/interviews/ with interviews-synthesis.md (rolling cross-interview synthesis hub) and
interview-template.md (per-interview structure: metadata, summary, takeaways, quotes, themes,
follow-ups, transcript). Added raw/interviews/ as the transcript drop folder. Linked from index
under "Interviews". Added an interview-ingest workflow to CLAUDE.md (clean transcript -> fill
template -> update synthesis -> log; anonymize by default; cannot transcribe audio, user supplies
text). Regenerated catalog; all links resolve.

## [2026-06-14] ingest | Interview — Interviewee 1 (first interview)
Transcribed via Whisper (small) from a .qta voice memo, converted to .m4a with ffmpeg. Saved raw
transcript to raw/interviews/interviewee-1.txt (~72 min, ~10k words). Created
wiki/interviews/interviewee-1.md: separated interviewer questions from answers, wrote summary, 9
key takeaways, themes, 14 notable quotes, the 20-question interview guide as run, follow-ups, and
cross-links to existing pages. Interview corroborates wiki theses (AI as aggregator not innovator;
verify-or-shaky-foundation; ground in your own docs = RAG; sycophancy from RLHF). Updated
interviews-synthesis with the entry, preliminary themes, and open questions. Regenerated catalog;
all links resolve. Kept first name "Interviewee 1" (can anonymize on request). TODO: confirm interview date
and consent.

## [2026-06-14] ingest | Team dynamics research
Added wiki/team-dynamics.md: the core team-dynamics literature, each finding mapped to a interviewee-1
theme. Verified citations: Edmondson 1999 (psychological safety) + Project Aristotle; Katzenbach &
Smith 1993 (shared purpose/mutual accountability); Woolley 2010 Science (collective intelligence / c
factor, social sensitivity, turn-taking); Wegner 1986 + Lewis 2003 (transactive memory = the "truth
document"); Jehn 1995 vs De Dreu & Weingart 2003 (task/relationship conflict, flagged as a [!conflict]
tension); Tuckman 1965 (forming-storming-norming-performing); Salas 2005 (Big Five of teamwork).
Cross-linked to interviewee-1, interviews-synthesis, genai-spectrum, rag-explained. Added to index;
regenerated catalog; all links resolve.

## [2026-06-14] ingest | Interviewee 1: full transcript + deep analysis + anonymization
Per Amal: removed the interviewee's name; everything is now "Interviewee 1" (files, slugs, content,
log). Renamed raw transcript to raw/interviews/interviewee-1.txt and record page to
wiki/interviews/interviewee-1.md. Added two pages: interviewee-1-transcript.md (full cleaned,
speaker-labeled intelligent-verbatim transcript) and interviewee-1-analysis.md (reflexive thematic
analysis: method, coding map, 8 themes with evidence + literature links, cross-cutting tensions,
salience, design implications for the AI questioner, tentative iNPD phase mapping, limitations and
reflexivity). Updated slug links in interviews-synthesis and team-dynamics. Verified: zero remaining
name mentions, all links resolve, catalog rebuilt.

## [2026-06-22] ingest | Multi-agent architecture design record
Created wiki/innovation-team-agent-architecture.md: the full design record for the AI-facilitated innovation team system. Documents all agents (Orchestrator, iNPD Agent, Collaboration Agent x member, Proof of Work Agent, Decision Logger, Socratic Agent) plus two milestone agents (Synthesis, Retrospective). For each agent: role, read/write access to the 4-tier LLM-Wiki, who it speaks to, and explicit design rationale. Covered design decisions with sourced reasoning: why Phase Gate merged into iNPD (same knowledge type, same output); why TRIZ merged into Socratic Agent (same task, different knowledge base); why Collaboration Agent is text-only (diarization complexity, privacy; audio is Phase 2); why one Collaboration Agent per member (member-specific history); why Orchestrator never speaks to team (prevents sycophancy and authority confusion); why cascade priority is iNPD > Collaboration > PoW (structural error > dynamics corruption > documentation gap); why feedback loop requires written responses (no signal from silent dismissal; Decision Logger's Socratic fallback depends on it); why Decision Logger has 3 input sources (transcripts miss implicit decisions; PoW catches artifact-without-rationale; Socratic fallback closes the loop); why Synthesis and Retrospective agents are milestone-only (need accumulated material; mid-phase synthesis disrupts generative work). 13 primary sources cited. Updated index (cleaned duplicate genai-as-socratic-facilitator entry, added architecture page, reorganized facilitation section). Updated genai-as-socratic-facilitator.md architecture paragraph to link forward.

## [2026-06-22] lint | Citation verification pass on genai-as-socratic-facilitator.md
Four errors corrected: (1) Bloom 1984 JSTOR URL was wrong (3202427 -> correct Sage DOI journals.sagepub.com/doi/10.3102/0013189X013006004); (2) VanLehn 2011 had wrong DOI (10.1207/... -> 10.1080/00461520.2011.611369) and wrong issue number (46/3 -> 46/4); (3) Collins & Stevens title was "Goals and Methods" -> "Goals and Strategies", book was Winrock/Handbook -> R. Glaser (Ed.) Advances in Instructional Psychology Vol. 2 pp. 65-119 Erlbaum; PsycNET URL removed (matched 1983 Reigeluth version, not 1982 Glaser). (4) Fitzpatrick 2017 URL was www.jmir.org/2017/2/e19 -> mental.jmir.org/2017/2/e19/. Text also corrected: Bloom's mechanism is mastery learning + corrective feedback (not "targeted questions"); VanLehn's key finding is step-based ITS (g=0.76) vs answer-based (g=0.31) (not a generic "questions beat explanations" claim). Woolley 2010 DOI typo fixed in Sources (1193117 -> 1193147).

## [2026-06-22] ingest | GenAI as Socratic Facilitator — research architecture page
Gap analysis against existing wiki: team-dynamics, getting-the-most-out-of-llms, interviews-synthesis, and genai-on-the-adaption-innovation-spectrum all contained relevant pieces but no page synthesized the core research concept. Gaps identified: (1) no Socratic facilitation page, (2) TRIZ absent from the wiki, (3) team-level groupthink amplification from AI sycophancy not addressed, (4) multi-agent facilitation architecture not synthesized, (5) iNPD not connected to GenAI facilitation timing. Created wiki/genai-as-socratic-facilitator.md: covers the Socratic questioning model (Bloom 1984 2-sigma; VanLehn 2011 ITS; Collins & Stevens 1982 inquiry teaching), phase-specific iNPD facilitation, TRIZ contradiction detection as Mode 2 of the Socratic agent (with [[triz]] as TODO), groupthink amplification and the RLHF-sycophancy-at-team-level problem (Janis 1982; Woolley 2010), multi-agent shared-state architecture (Park 2023 Generative Agents; Packer 2023 MemGPT; Liu 2023 lost-in-the-middle), Woebot as adjacent-field evidence (Fitzpatrick 2017), and three key design limitations (coverage, feedback loop, over-questioning). Updated team-dynamics.md closing section and interviews-synthesis.md closing sentence to link forward. Added new page to index under "Team dynamics and facilitation." 12 primary sources cited; [[triz]] left as a valid TODO marker.

## [2026-06-14] lint/edit | QA pass on new additions
Reviewed the recent pages (genai-as-socratic-facilitator, team-dynamics, interviewee-1 set). Fixes:
created wiki/triz.md to resolve the broken [[triz]] link (Altshuller-sourced primer); removed 13
em-dashes from genai-as-socratic-facilitator to match house style; corrected the Woebot claim to the
RCT result (significant depression reduction vs control; anxiety fell in both groups) per Fitzpatrick
2017; added a Bloom 2-sigma replication caveat; added woolley-2010 + liu-2023 to that page's
frontmatter sources. In team-dynamics, replaced a gendered-slur quote with a paraphrase (consistent
with the cleaned transcript) and fixed a descriptor. Sharpened the analysis theme-2 literature anchor
(psychological safety for trust; Woolley for reciprocity). Noted light softening of strong language in
the transcript header. Added socratic + triz to index. Verified: no em-dashes, all links resolve.

## [2026-06-14] ingest | Folded iNPD into its own page
Created wiki/inpd.md (Cagan & Vogel four phases: Identify, Understand, Conceptualize, Realize; SET
factors -> Product Opportunity Gaps; the 7 Value Opportunities; per-phase deadlock patterns). Pointed
genai-as-socratic-facilitator and interviewee-1-analysis to [[inpd]] for the framework definition,
keeping the questioning application in the socratic page. Added inpd to index. Verified: no em-dashes,
all links resolve, catalog rebuilt.

## [2026-06-14] research+edit | Mitigations for the agent-architecture critique
Researched fixes for the design-review critiques and added an "Open design questions and mitigations"
section to innovation-team-agent-architecture.md, each critique mapped to sourced mitigations:
detection (LLM-Modulo external checks + self-consistency Wang 2022 + LLM-as-judge bias control Zheng
2023); genuine challenge (separate devil's-advocate persona ~99% vs ~48% disagreement; Du/Liang
multi-agent debate; Sharma 2023 sycophancy; FlipFlop caveat); logging burden (auto decision/action
extraction, AMI corpus / 2303.16763); MVP+evaluation (Wizard-of-Oz + Woebot-style controlled trial);
TRIZ domain-fit bound; timing flagged as still-open; plus two internal-consistency clarifications
(Synthesis duplication, per-member agent). Added 10 sources (all arXiv IDs verified). Honest about
residual unknowns. Verified: no em-dashes, all links resolve, catalog rebuilt.

## [2026-06-14] edit | Folded mitigations into original architecture sections
Per Amal (no separate section): removed the standalone "Open design questions and mitigations" block
and wove each researched fix into the section it belongs to. Detection reliability (self-consistency,
LLM-as-judge bias control, deterministic hard-gate checks) -> Orchestrator. Auto decision/action
extraction (AMI corpus) -> Decision Logger Source 1. TRIZ domain bound -> Mode 2. Genuine challenge
(separate devil's-advocate persona, proposer-vs-challenger debate, FlipFlop caveat) -> Mode 4.
Synthesis-mode-vs-agent distinction -> Synthesis Agent. Per-member separation caveat -> Collaboration
Agent. Coverage mitigation + validation/Wizard-of-Oz + timing-open -> the existing Key limitations
section on genai-as-socratic-facilitator (added WoZ source). Verified: no em-dashes, all links resolve.

## [2026-06-14] correct | Two design corrections from Amal (architecture page)
1) Challenge mode reframed: its purpose is to make sure the team has reasoned a decision through, not
to judge whether the team is right. An overruled ("silenced") challenge is a valid outcome as long as
the team supplies human reasoning (captured by the feedback loop). Dropped the "challenger must hold
its position" framing; FlipFlop now noted as not-a-problem since the mode surfaces the counter-case
rather than trying to win. Aligned the matching sentence on genai-as-socratic-facilitator.
2) Removed Channel 4 (Direct queries): the rationale source is the team's answers to Socratic
questions (Decision Logger Source 3), not the team querying the system, which also contradicted the
"system never gives answers" principle. Channels now three; Orchestrator no longer answers queries.
Verified: no em-dashes, all links resolve, no stray blank lines.

## [2026-06-14] ingest | Agent system prompts
Created wiki/agent-prompts.md: draft system prompts for all eight agents (Orchestrator, iNPD,
Collaboration, Proof of Work, Decision Logger, Socratic, Synthesis, Retrospective), each bound to its
read/write tiers and the architecture's rules (LLM never decides/answers; output is a question or a
structured write; Challenge mode provokes reasoning not correctness; rationale comes from Socratic
answers, no team-to-system queries). Added a "what prompts can't do alone" note (self-consistency,
separate devil's-advocate instance, tier access control, feedback/cascade are runtime, not prompt).
Linked from architecture (## Agents) and index. Verified: no em-dashes, code fences balanced, links
resolve, catalog rebuilt.

## [2026-06-14] edit | Removed cascade priority
Dropped the cascade-priority concept from the architecture per Amal (not needed for now). Deleted the
"## Cascade priority" section, removed the Orchestrator's cascade reference, reworded "Coverage over
precision" to drop the cascade mention, and removed cascade from the index summary and the agent-prompts
runtime note. The Orchestrator still collects flags from the three monitoring agents and fires one
question when warranted; it just no longer ranks them by a fixed priority order. Verified: links resolve,
catalog rebuilt.
