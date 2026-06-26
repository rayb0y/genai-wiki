# GenAI Knowledge Base

A lean, sourced wiki on how generative AI works and what it is good and bad at, plus an applied research project that builds on it: whether an AI Socratic questioner can help stuck innovation teams. It is an LLM-maintained knowledge base. A human curates sources and asks questions, and an LLM writes and maintains the pages, with a citation for every non-obvious claim.

## Start here

Open [index.md](index.md) for the hand-written guide, or [wiki/catalog.md](wiki/catalog.md) for an auto-generated index of every page.

## Foundation: how GenAI works

- [How GenAI works](wiki/how-genai-works.md): the mechanism, organized as storage, retrieval, and interaction.
- [What GenAI is good and bad at](wiki/what-genai-is-good-and-bad-at.md): strengths, weaknesses, and when to use a non-generative method.
- [Getting the most out of LLMs](wiki/getting-the-most-out-of-llms.md): retrieval (RAG and beyond), storage and memory, and long-context coherence.
- [RAG, explained simply](wiki/rag-explained.md): a beginner explainer.
- [Reading list](wiki/reading-list.md): the key papers, grouped by topic.

## Applied: cognitive style

- [Kirton's Adaption-Innovation](wiki/kirton-adaption-innovation.md): a primer on the adaptive-versus-innovative cognitive-style theory.
- [GenAI on the A-I spectrum](wiki/genai-on-the-adaption-innovation-spectrum.md): GenAI as a high-level adaptor, and what that means for human-AI teams.

## Applied: an AI Socratic facilitator for innovation teams

- [GenAI as a Socratic facilitator](wiki/genai-as-socratic-facilitator.md): the research case for an AI questioner, with its limitations.
- [Innovation-team agent architecture](wiki/innovation-team-agent-architecture.md): the full multi-agent system design (four-tier shared state, six core agents plus two milestone agents, the feedback loop).
- [Agent prompts](wiki/agent-prompts.md): a draft system prompt for each agent.
- [Architecture diagram](wiki/architecture-diagram.md): a Mermaid flow view of the whole system.
- [Team dynamics](wiki/team-dynamics.md): the research on what makes teams work.
- [iNPD](wiki/inpd.md) and [TRIZ](wiki/triz.md): the innovation frameworks the design draws on.
- Interviews: [synthesis](wiki/interviews/interviews-synthesis.md), the [first interview](wiki/interviews/interviewee-1.md) with its [analysis](wiki/interviews/interviewee-1-analysis.md) and [transcript](wiki/interviews/interviewee-1-transcript.md).

## How it's organized

- `index.md` is the catalog, `log.md` is the change history, and `CLAUDE.md` is the schema the LLM follows (conventions, sourcing rules, and voice).
- `wiki/` holds the topic pages, with `wiki/sources/` for per-source summaries and `wiki/interviews/` for interview write-ups.
- `raw/` is for source documents and transcripts you drop in for the LLM to ingest.
- `scripts/build_catalog.py` regenerates `wiki/catalog.md`, and a GitHub Action keeps it current on each push.

## Using it with Obsidian

This repo is an Obsidian vault. See [SETUP.md](SETUP.md) for how to open it and which plugins help. Pages link to each other with Obsidian-style `[[wikilinks]]`, which are clickable in Obsidian but render as plain text on the GitHub web view, where the standard markdown links above work instead.
