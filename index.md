# Index: GenAI Knowledge Base

A lean, sourced knowledge base on how generative AI works and what it is good and bad at. Read this first, then open a page. It aims to be objective and is cited throughout.

## Using this wiki

- [[SETUP]]: how to open this folder as an Obsidian vault, and the daily workflow.
- [[dashboard]]: auto-generated views of every page in Obsidian (needs the Dataview plugin).
- [[catalog]]: a static index of every page that also renders on GitHub (rebuilt automatically).

## Core pages (`wiki/`)

- [[how-genai-works]]: the mechanism, organized as Storage (where knowledge lives), Retrieval (how it is accessed), and Interaction (how you use it), plus short notes on training and image generation.
- [[what-genai-is-good-and-bad-at]]: what it does well, what it does not, and when to reach for a non-generative method. Feeds the Arthur Sugden project.
- [[getting-the-most-out-of-llms]]: practical levers, covering retrieval (RAG and beyond), storage and memory, long-context coherence, and the LLM-maintained-wiki pattern.
- [[rag-explained]]: what Retrieval-Augmented Generation is, in plain terms. Start here if RAG is new.
- [[reading-list]]: the key papers, grouped by what each tells you.

## Applied: Kirton's Adaption-Innovation

- [[kirton-adaption-innovation]]: a primer on Kirton's A-I cognitive-style theory (adaptive versus innovative, style versus level, the KAI inventory).
- [[genai-on-the-adaption-innovation-spectrum]]: the synthesis. GenAI as a high-level adaptor, how adaptive and innovative people should use it, and human-AI team composition.

## Team dynamics and facilitation (`wiki/`)

- [[team-dynamics]]: the research on what makes teams work (psychological safety, shared purpose, collective intelligence, transactive memory, conflict, development stages), mapped to the interview findings.
- [[inpd]]: the integrated New Product Development process (Cagan & Vogel), the four-phase framework the project studies, and where teams typically get stuck by phase.
- [[triz]]: the Theory of Inventive Problem Solving (contradiction-based), used as one questioning mode in the facilitation design.
- [[genai-as-socratic-facilitator]]: the research case for why an AI questioner can work in innovation teams. Covers the Socratic questioning model, phase-specific facilitation, the groupthink amplification risk, and key design limitations.
- [[innovation-team-agent-architecture]]: the full system design record. Each agent's role, inputs, outputs, and the reasoning behind every design decision: the LLM-Wiki shared state (4 tiers), 6 core agents plus 2 milestone agents, and the feedback loop.
- [[agent-prompts]]: the draft system prompt for each agent, bound to its read/write tiers and the design's rules.

## Interviews (`wiki/interviews/`)

- [[interviews-synthesis]]: rolling synthesis of project interviews, with the themes that recur across them.
- [[interview-template]]: the structure each interview page follows.

Drop a transcript into `raw/interviews/` (or paste it to me) and I will clean it, file it here, and update the synthesis.

## Sources (`wiki/sources/`)

- [[lee-trott-2023-llm-explained]]: a popular explainer (Understanding AI, 2023), with its cited bibliography and a note on where it has dated since 2023.

_(See `log.md` for history and `CLAUDE.md` for the wiki's conventions.)_
