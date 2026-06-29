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
- [[complaints-and-conflict-in-teams]]: the research base for what the system should do when a member complains about a person or the project (voice, procedural fairness, the triangulation trap, task versus relationship conflict).
- [[inpd]]: the integrated New Product Development process (Cagan & Vogel), the four-phase framework the project studies, and where teams typically get stuck by phase.
- [[triz]]: the Theory of Inventive Problem Solving (contradiction-based), used as one questioning mode in the facilitation design.
- [[innovation-process-methods]]: the front-end toolkit the CMU III capstone uses (PESTLE, design research, experience mapping, service blueprints, pretotyping, Double Diamond, VOA, business methods). A growing catalog.
- [[capstone-process]]: the IPD Capstone as actually run, phase by phase, with the recurring patterns in the teaching team's feedback (a corpus of real facilitation moves).
- [[genai-as-socratic-facilitator]]: the research case for why an AI questioner can work in innovation teams. Covers the Socratic questioning model, phase-specific facilitation, the groupthink amplification risk, and key design limitations.
- [[innovation-team-agent-architecture]]: the full system design record. Each agent's role, inputs, outputs, and the reasoning behind every design decision: the LLM-Wiki shared state (4 tiers), 6 core agents plus 2 milestone agents, and the feedback loop.
- [[agent-prompts]]: the draft system prompt for each agent, bound to its read/write tiers and the design's rules.
- [[proof-of-work-attribution]]: the research on whether transcripts and artifacts can reveal who did what and who sourced an idea, what is and is not attributable, and how to do it without surveillance.
- [[architecture-diagram]]: a Mermaid flow view of the whole system (tiers, agents, the single intervention path).

## Interviews (`wiki/interviews/`)

- [[interviews-synthesis]]: rolling synthesis of project interviews, with the themes that recur across them.
- [[interviewee-1]]: the first interview, a structured summary with key takeaways, quotes, and themes.
- [[interviewee-1-analysis]]: a deeper people-researcher analysis of that interview.
- [[interviewee-1-transcript]]: the full cleaned, speaker-labeled transcript.
- [[interviewee-2]]: the second interview, a designer on a CMU capstone, on aligned expectations, authority-versus-peer feedback, and AI as a refiner.
- [[interviewee-2-analysis]]: a deeper people-researcher analysis of that interview.
- [[interviewee-2-transcript]]: the full cleaned, speaker-labeled transcript.
- [[interviewee-3]]: the third interview, an engineer-minded student on conflict and ownership, who challenges the Collaboration Agent and wants a scoping mechanism.
- [[interviewee-3-analysis]]: a deeper people-researcher analysis of that interview.
- [[interviewee-3-transcript]]: the full cleaned, speaker-labeled transcript.
- [[interview-template]]: the structure each interview page follows.
- [[faculty-interview-protocol]]: the full semi-structured guide for interviewing III capstone faculty (a distinct population from the students), about 50 to 60 minutes.
- [[faculty-interview-protocol-short]]: the 25-minute core version for faculty who are short on time, must-ask questions first.

Drop a transcript into `raw/interviews/` (or paste it to me) and I will clean it, file it here, and update the synthesis.

## Sources (`wiki/sources/`)

- [[lee-trott-2023-llm-explained]]: a popular explainer (Understanding AI, 2023), with its cited bibliography and a note on where it has dated since 2023.

_(See `log.md` for history and `CLAUDE.md` for the wiki's conventions.)_
