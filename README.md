# GenAI Knowledge Base

A lean, sourced wiki on how generative AI works and what it is good and bad at. It is an
LLM-maintained knowledge base: a human curates sources and asks questions, and an LLM writes and
maintains the pages, with a citation for every non-obvious claim.

## Start here

Open [index.md](index.md) for the hand-written guide, or [wiki/catalog.md](wiki/catalog.md) for an
auto-generated index of every page. The core pages:

- [How GenAI works](wiki/how-genai-works.md): the mechanism, organized as storage, retrieval, and
  interaction.
- [What GenAI is good and bad at](wiki/what-genai-is-good-and-bad-at.md): strengths, weaknesses, and
  when to use a non-generative method.
- [Getting the most out of LLMs](wiki/getting-the-most-out-of-llms.md): retrieval (RAG and beyond),
  storage and memory, and long-context coherence.
- [RAG, explained simply](wiki/rag-explained.md): a beginner explainer.
- [Reading list](wiki/reading-list.md): the key papers, grouped by topic.
- Applied: [Kirton's Adaption-Innovation](wiki/kirton-adaption-innovation.md) and
  [GenAI on the A-I spectrum](wiki/genai-on-the-adaption-innovation-spectrum.md).

## How it's organized

- `index.md` is the catalog, `log.md` is the change history, and `CLAUDE.md` is the schema the LLM
  follows (conventions, sourcing rules, and voice).
- `wiki/` holds the topic pages, with `wiki/sources/` for per-source summaries.
- `raw/` is for source documents you drop in for the LLM to ingest.

## Using it with Obsidian

This repo is an Obsidian vault. See [SETUP.md](SETUP.md) for how to open it and which plugins help.
Note that pages link to each other with Obsidian-style `[[wikilinks]]`. Those are clickable in
Obsidian but render as plain text on the GitHub web view, where the standard markdown links above
work instead.
