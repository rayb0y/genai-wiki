# GenAI Knowledge Base — Wiki Schema

This repo is an LLM-maintained wiki about generative AI (GenAI): how it works, what it is and is not good at, its alternatives, and how AI works when it is not generative. The LLM owns the `wiki/` layer entirely. The human (Amal) curates sources, asks questions, and reads. The LLM does the writing, cross-referencing, and bookkeeping.

## Domain and audience

- Topic: generative AI, covering mechanisms, capabilities, limits, alternatives, and the wider field of AI beyond GenAI (classical, symbolic, and discriminative ML).
- Depth: technical but accessible. Explain real mechanisms (transformers, gradient descent, diffusion, attention) with rigor, but keep it readable by a smart non-specialist, and define jargon on first use.
- Sourcing is mandatory. Every non-obvious factual or quantitative claim must carry a citation to a primary paper, official doc, or reputable article. No unsourced claims.
- Objective, not sycophantic. Report what the evidence says, including where GenAI fails, is overhyped, or where claims are contested. Avoid marketing language and cheerleading, and do not hedge away real criticism. Where experts disagree, present both sides with citations and say so plainly. Distinguish demonstrated results from vendor claims and speculation. The wiki should read like a skeptical literature review, not a brochure.

## Voice

Write in a plain, human voice. Avoid the common tells of machine-generated prose: heavy em-dash use, the "not just X but Y" construction, rule-of-three triads, punchy sentence-fragment conclusions ("The pattern:", "Bottom line:", "Net:"), bold-label bullets, and filler intensifiers (genuinely, crucial, robust, leverage, seamless, tellingly, importantly). Prefer commas, periods, and parentheses over em-dashes. Vary sentence length. Lists are fine where they aid clarity, but write the items as plain sentences rather than bolded labels.

## Directory layout

```
GenAI-Wiki/
  CLAUDE.md          # this file, the schema
  index.md           # catalog of every page (read first when answering)
  log.md             # append-only record of ingests, queries, and lints
  raw/               # immutable source documents the user drops in (LLM never edits)
  wiki/
    *.md             # core topic pages, kept deliberately few (lean over comprehensive)
    sources/         # one summary page per ingested source, with full citation
```

Keep the wiki lean. Prefer a few dense, well-linked pages over many thin ones. Consolidate before adding a new page, and only split a page out when it truly stands alone. The current core is `how-genai-works.md` (Storage, Retrieval, Interaction), `what-genai-is-good-and-bad-at.md`, and `reading-list.md`.

## Page conventions

Every wiki page starts with YAML frontmatter:

```yaml
---
title: Human-Readable Title
type: concept | comparison | source | overview | dashboard
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [genai, transformers, ...]
sources: [source-page-slug, ...]   # source pages this page draws on
---
```

- Links: use Obsidian-style `[[wikilink]]` to other pages by their filename slug (without `.md`). Link liberally; a link to a not-yet-written page is a valid TODO marker.
- Citations: inline, as `([Author Year](URL))` or `([Source Title](URL))`. Each page ends with a `## Sources` section listing full references with links.
- Tone: explanatory prose. Use lists or tables only where they aid clarity. No filler.
- Contradictions: when a new source contradicts an existing claim, do not silently overwrite. Note both, flag with `> [!conflict]`, and cite each side.

## Workflows

Ingest (the user drops a file in `raw/` or asks to research a topic):
1. Read the source, or do web research with citations.
2. Write or update a page in `wiki/sources/` summarizing it with a full citation.
3. Update the relevant `wiki/` pages, integrating the new information.
4. Add or refresh the entry in `index.md`.
5. Append a line to `log.md`: `## [YYYY-MM-DD] ingest | <title>`.

Query (the user asks a question):
1. Read `index.md` to locate relevant pages, then read those pages.
2. Synthesize an answer with citations.
3. If the answer is durable, file it back as a wiki page and index it.
4. Append to `log.md`: `## [YYYY-MM-DD] query | <question>`.

Lint (the user asks for a health check):
- Find contradictions, stale claims, orphan pages, missing pages, missing cross-references, and gaps a search could fill.
- Suggest new questions and sources. Append to `log.md`.

## Conventions for this wiki specifically

- Keep the distinction sharp between GenAI (models that produce new content such as text, images, audio, and code) and discriminative or classical AI (models that classify, predict, rank, or optimize). That distinction is the whole point of the wiki.
- Prefer primary sources: arXiv papers, official model or system cards, standards bodies, and peer-reviewed venues. Mark blogs and journalism as secondary.
- When citing benchmark numbers, name the benchmark, the model, and the date, since they go stale fast.
