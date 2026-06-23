---
title: "Multi-Agent Architecture for AI-Facilitated Innovation Teams"
type: concept
created: 2026-06-22
updated: 2026-06-22
tags: [architecture, multi-agent, orchestrator, socratic, inpd, triz, decision-logger, proof-of-work, collaboration, shared-state, facilitation]
sources: [kambhampati-2024, kambhampati-llm-modulo-2024, park-2023, packer-2023, liu-2023, wegner-1986, lewis-2003, collins-stevens-1982, vanlehn-2011, woolley-2010, janis-1982, altshuller-1984, cagan-vogel-2002, sharma-2023, du-2023, liang-2023, wang-2022, zheng-2023, flipflop-2023, devils-advocate-2024, inducing-disagreement-2024, meeting-action-items-2023, wizard-of-oz-2022]
---

# Multi-Agent Architecture for AI-Facilitated Innovation Teams

This page documents the design of the multi-agent system built for the innovation-teams research project: what each component does, what information it reads and writes, and why it was designed that way. It is a design record, not a tutorial. For the research case supporting the Socratic approach, see [[genai-as-socratic-facilitator]]. For the iNPD process the system facilitates, see [[inpd]]. For the TRIZ contradiction method used by one of the agent's modes, see [[triz]].

## What this system is not

It is not a system that tells teams what to do. LLMs cannot reliably produce and self-verify multi-step plans ([Kambhampati 2024](https://arxiv.org/abs/2403.04121)). The LLM-Modulo framework argues that the right role for an LLM in a planning-adjacent task is inside a loop with a human verifier: the LLM generates candidates; the human (or a domain checker) approves them ([Kambhampati et al. 2024](https://arxiv.org/abs/2402.01817)). This architecture applies that pattern to facilitation: the agents generate questions; the team approves, rejects, or logs a reason for ignoring them. The LLM never makes a decision for the team.

## The shared state layer: LLM-Wiki

The precondition for any agent that can notice a reasoning gap is that the reasoning is written down somewhere the agent can read it. An LLM has no persistent memory by default ([[how-genai-works]] §Storage). The "lost in the middle" problem means that even a very large context window is unreliable for the volume of material a multi-week project generates: accuracy in a 20-document setting dropped below the model's closed-book baseline when the relevant document sat in the middle of a long context ([Liu et al. 2023](https://arxiv.org/abs/2307.03172)). The fix is external structured state rather than a longer window, which is the MemGPT insight: treat the window as working memory and an external store as long-term memory ([Packer et al. 2023](https://arxiv.org/abs/2310.08560)). For agents that need to maintain behavior across sessions, a persistent memory stream scored by recency, relevance, and importance enables coherence that no single window can ([Park et al. 2023](https://arxiv.org/abs/2304.03442)).

The project's shared state is called the LLM-Wiki: a curated, structured, agent-maintained markdown store that persists across sessions. It is the technical implementation of what Wegner called a transactive memory system, the team's external map of what is known, decided, and built ([Wegner 1986](https://link.springer.com/chapter/10.1007/978-1-4612-4634-3_9); [Lewis 2003](https://doi.org/10.1037/0021-9010.88.4.587)). See [[team-dynamics]] §Transactive memory and [[getting-the-most-out-of-llms]] §The compounding move for the broader treatment.

The LLM-Wiki is organized into four tiers with different access controls:

**Tier 1: Project State.** Readable and writable by all agents. Contains the decision log (what was decided, when, and why), the artifact log (what was built and in which phase), the current iNPD phase, and the phase transition history. This is the shared ground truth.

**Tier 2: Team Dynamics.** Writable by the Collaboration Agent; readable by the Collaboration Agent and the Orchestrator. Contains per-member participation patterns, flagged unresolved interpersonal conflicts, and emotional signal history. The Socratic Agent does not read this tier. The reason is important: if the Socratic Agent read Team Dynamics, it could craft questions that target a specific member's emotional state or interpersonal position, which would make it a manipulation tool rather than a facilitation one. Separating the tiers preserves the Socratic Agent's role as a process-level questioner, not a people-manager.

**Tier 3: Knowledge Base.** Read-only for all agents. Contains the iNPD phase definitions (from [[inpd]]) and the TRIZ contradiction matrix and inventive principles (from [[triz]]). No agent writes to this tier; it is the project's reference library.

**Tier 4: Agent Logs.** Written by each agent for its own records; readable only by the Orchestrator. Contains the history of questions asked, questions dismissed, calibration signals received, and inter-agent messages. The purpose is audit: the Orchestrator can see the system's history without that history polluting the team-facing state.

## Input channels

Three channels bring information into the system. Each has a different trust level and update cadence, which is why they are kept separate rather than merged into a single feed.

**Channel 1: Transcripts and session notes.** The primary source. After each work session, the team submits a text record of what happened. These can be typed notes, structured summaries, or text transcribed from audio by a tool the team uses externally. The system does not transcribe audio directly (see Collaboration Agent section for why). The Decision Logger reads these first.

**Channel 2: Artifact submissions.** The Proof of Work Agent receives these. An artifact is anything the team produces: a research summary, a concept sketch, a prototype specification, a slide deck, a user interview report. Submitting an artifact is a signal that a decision was made (to build this, not something else), even if the decision was never written down.

**Channel 3: Feedback signals.** The team's structured responses to Socratic Agent questions: thumbs up with rationale, thumbs down with explanation, or explicit "ignoring" with a reason. See the Feedback Loop section for the full mechanics. These are the calibration inputs for the Orchestrator and, when substantive, become Decision Logger entries.
## Agents

The system prompt for each agent is in [[agent-prompts]].

### Orchestrator

**Reads:** all four tiers of the LLM-Wiki.
**Writes:** nothing directly to state.
**Speaks to:** other agents only. It never addresses the team.

The Orchestrator is the system's nervous system. It monitors all incoming signals (iNPD Agent phase events, Collaboration Agent flags, Proof of Work events, feedback loop responses), decides when a Socratic Agent question is warranted, and chooses the mode. It does not answer questions for the team; the team's record of "why" is built from its answers to the Socratic Agent's questions (see the Decision Logger), not from the team querying the system.

Why it never speaks to the team: the single-agent failure mode is that the LLM enters the team's social dynamics. When a team gets answers and analysis directly from a central AI, authority confusion follows, and sycophancy pressure builds (the team asks, the AI validates, the feedback loop rewards agreement). The Orchestrator being an invisible coordinator means all team-facing outputs are structured through specialized agents with defined scopes. Any output the team sees comes from the Socratic Agent (a question) or from a status interface (a read from Project State). The Orchestrator never editorializes.

Why it reads all four tiers: deciding when not to fire a question is as important as deciding when to fire one. If the Collaboration Agent's Team Dynamics log shows that two members are in active conflict, firing a TRIZ contradiction question about a technical decision is the wrong intervention at that moment. The Orchestrator needs the full picture to make that judgment.

How detection is kept reliable: deciding that a pattern is a real gap, contradiction, or premature consensus is the system's hardest judgment, and it is the kind of classification GenAI is weakest at ([[what-genai-is-good-and-bad-at]]). The Orchestrator reduces that risk in three ways. Hard, checklist-style criteria (has a Product Opportunity Gap been articulated? has user research been synthesized?) are checked by deterministic or model-based rules rather than free judgment, which is the LLM-Modulo idea of pairing the model with a sound external check ([Kambhampati et al. 2024](https://arxiv.org/abs/2402.01817)). Soft judgments ("is this a gap?") are sampled several times and fire only when the samples agree, the self-consistency method ([Wang et al. 2022](https://arxiv.org/abs/2203.11171)). And because the trigger is effectively an LLM-as-judge call, its known biases (verbosity, position, self-preference) are controlled for ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)). Detection precision and recall on real project logs are still unmeasured, so they are something the validation stage has to test rather than assume (see the limitations in [[genai-as-socratic-facilitator]]).

### iNPD Agent

**Reads:** Tier 1 (Project State), Tier 3 (Knowledge Base: iNPD definitions).
**Writes:** Tier 1 (current phase, phase transition events, gate check results).
**Speaks to:** Orchestrator.

The iNPD Agent operates in two modes that were originally separate agents.

**Continuous monitoring mode:** tracks which iNPD phase the team is in by reading the decision log and artifact log and checking them against the criteria for each phase. It flags when the team's current work pattern diverges from what the current phase requires (for example, when a Phase 1 team has already converged on a specific solution concept, suggesting premature narrowing). These flags become candidates for the Socratic Agent's phase-based question mode.

**Gate mode:** activated when the team signals a phase transition. Before the transition is registered in Project State, the iNPD Agent runs a structured completion check: has the current phase produced the outputs it requires? For Phase 1 (Identify), the check is whether a Product Opportunity Gap has been articulated. For Phase 2 (Understand), whether user research and stakeholder analysis have been completed and synthesized. Unmet gate criteria become Socratic question candidates for Mode 1.

Why Phase Gate was merged into iNPD rather than kept as a separate agent: a separate Phase Gate Agent would need to read the same tiers, apply the same iNPD phase criteria, and produce the same type of output (a gap for the Socratic Agent to turn into a question). Two agents doing the same knowledge retrieval to produce the same output type is duplication, not modularity. The design rule applied here is that agents earn their separation when they bring a distinct knowledge base or produce a categorically different output. Gate checking brings neither; it is phase monitoring run at a transition boundary.

### Collaboration Agent

**One per team member.**
**Reads:** Tier 2 (Team Dynamics for its assigned member), Tier 1 (Project State).
**Writes:** Tier 2 (participation patterns, flagged issues, emotional signals for its member).
**Speaks to:** Orchestrator.

The Collaboration Agent tracks whether each member is being heard, whether their stated positions and objections are being addressed in subsequent sessions, and whether participation patterns are becoming unbalanced. It uses the session transcripts and the member's structured post-session notes as its primary inputs.

Why one agent per member rather than one shared agent: collaboration dynamics are member-specific. Whether Person A's Phase 2 objection was addressed in the next session is a distinct question from whether Person B's concept proposal was evaluated. A per-member agent maintains a continuous history for each person that a shared agent would aggregate and lose. When the Orchestrator needs to know whether a specific member's concern has been unaddressed for multiple sessions, the per-member agent has that record directly. This is a borderline case under the project's own rule that agents earn their separation: the per-member agents share a knowledge base and output type, so they could be read as one agent partitioned by person. They are kept separate because maintaining a continuous, uninterrupted history per member is the distinguishing function; if that proves unnecessary in practice, they should collapse into one agent with per-member records.

Why text-based and text-only: audio analysis would require speaker diarization (attributing speech to the correct person in a multi-speaker recording), which adds technical complexity and raises privacy questions at the research prototype stage. Audio attribution is scoped for a later phase. Text is the right scope for now: it can be typed notes, structured summaries, or externally transcribed audio, and it makes the attribution problem trivial because the team controls the format.

The peer review model: rather than attempting real-time intervention during a meeting (which would introduce social friction by commenting on who is dominating the conversation mid-session), the Collaboration Agent works asynchronously. After each session, each member submits a structured note covering what they contributed, what questions they still have, and what they feel went unaddressed. The Collaboration Agent reads these against the session transcript and flags discrepancies to the Orchestrator. This asymmetry, acting after rather than during, is intentional. Woolley and colleagues found that equal turn-taking predicts group outcomes, but correcting imbalance in real time is disruptive; the right moment is the retrospective between sessions ([Woolley et al. 2010](https://www.science.org/doi/10.1126/science.1193147)).

### Proof of Work Agent

**Reads:** Tier 1 (artifact log), artifact submissions via Channel 2.
**Writes:** Tier 1 (artifact log entries: artifact title, version, phase, submitter, date, description).
**Speaks to:** Orchestrator (artifact events), Decision Logger (artifact context when a new entry has no corresponding decision log entry).

The Proof of Work Agent is the "what was built" record. Every artifact the team produces is logged here with its phase context. Its Orchestrator-facing role is to fire an event whenever an artifact appears without a corresponding decision log entry: this signals a decision that was made implicitly, which is one of the Decision Logger's three failure modes to catch.

Why it is separate from the Decision Logger: PoW and the Decision Logger answer different questions. "What was built" and "why was it decided" are independent. A prototype can be submitted before the rationale has been articulated. The PoW artifact event is what prompts the Decision Logger to ask "is there a log entry explaining this?" Having them be the same agent would force that temporal coupling and lose the ability to detect the gap.

### Decision Logger

**Reads:** Tier 1 (decision log, artifact log), Channel 1 (transcripts), Channel 3 (feedback signals), PoW events, Socratic Agent history from Tier 4.
**Writes:** Tier 1 (decision log entries: what was decided, when, by whom, why, which artifacts it explains).
**Speaks to:** Orchestrator.

The Decision Logger is the "why" record. Its job is to make sure that every consequential decision in the project has a logged rationale, and it does this through three input sources that cover different failure modes.

**Source 1 (transcripts):** The Decision Logger reads session notes and extracts explicit decisions and their stated reasons. Doing this automatically is the point: extracting decisions and action items from a raw transcript is an established task with annotated benchmarks (the AMI meeting corpus labels decisions and actions) ([Meeting Action Item Detection 2023](https://arxiv.org/abs/2303.16763)), so the team submits a raw transcript and the Decision Logger proposes entries for one-tap confirmation rather than asking people to author structured notes. This keeps the logging burden off the team, which matters because teams under deadline do not log diligently ([[interviewee-1-analysis]]). This is the primary source. Its failure mode is implicit decisions, where the team reached consensus without articulating the reasoning. "Everyone agreed to go with concept B" without a recorded "because it better addresses the user need identified in Phase 2" is an incomplete decision log entry. The transcript can confirm the decision happened; it cannot supply the missing reasoning.

**Source 2 (PoW signals):** When the Proof of Work Agent logs a new artifact, the Decision Logger checks whether the artifact has a corresponding decision log entry. If not, it flags the gap to the Orchestrator. The underlying reasoning is that an artifact is evidence of a decision: the team built this concept sketch rather than another, which means something drove that choice, even if it was never stated. This source catches decisions that show up as outputs before they show up as reasoning.

**Source 3 (Socratic fallback):** If the Socratic Agent asked a rationale-probing question and the team answered it (through the feedback loop), that answer is a decision log entry whether or not the team ever wrote one formally. If the team logged "ignoring this question because we addressed it last session," that log entry is also recorded: it documents what the team considered and rejected, which is valuable historiographically. This source closes the loop between the questioning system and the documentation system, and is why the feedback loop's "ignoring" option requires a written reason rather than a silent dismiss.

The three-source structure exists because any single source will miss cases. Transcripts miss implicit decisions. PoW misses decisions that do not yet produce artifacts. Socratic fallback requires the system to have asked, which requires a trigger. Three overlapping coverage profiles reduce the chance of a consequential decision going unrecorded.

### Socratic Agent

**Reads:** Tier 1 (Project State), Tier 3 (Knowledge Base: iNPD definitions and TRIZ matrix), Orchestrator triggers.
**Writes:** nothing to state.
**Speaks to:** the team (the only agent that does so, through the Orchestrator's trigger).

The Socratic Agent asks one question per trigger cycle. It does not propose solutions, generate options, or evaluate concepts. It recognizes a reasoning pattern in the current project state and retrieves a question calibrated to that pattern. The research case for this role is in [[genai-as-socratic-facilitator]]; the core justification is that step-level elicitation of reasoning, not delivery of information, is where facilitation value is concentrated ([VanLehn 2011](https://www.tandfonline.com/doi/abs/10.1080/00461520.2011.611369); Collins & Stevens 1982).

Why the Socratic Agent writes nothing to state: a question that does not land is not a decision. If the Socratic Agent logged every question it fired as a state write, the decision log would accumulate questions the team found irrelevant and the signal-to-noise ratio for the Decision Logger would degrade. The team's response (from the feedback loop) is what gets written, either as a calibration signal or as a substantive entry that the Decision Logger harvests.

**Mode 1: Phase-based.** Triggered by the iNPD Agent. The question is drawn from the iNPD-phase question bank for the current phase and the specific gap the iNPD Agent flagged. Phase 1 questions address premature convergence (what other directions have not been explored?). Phase 2 questions challenge unexamined interpretation (what else could this observation mean?). Phase 3 questions force evaluation criteria (what criteria would you use to choose between these concepts?). Phase 4 questions force prioritization (what is the minimum that ships, and what is out of scope?).

**Mode 2: TRIZ contradiction.** Triggered by the Orchestrator when logged decisions contain a structural conflict: improving one parameter while the current approach degrades another. The Socratic Agent classifies the conflict against the 39 TRIZ engineering parameters, retrieves the matched inventive principles from the contradiction matrix, and converts each principle into a question for the team. The team does not need to know TRIZ is running; they receive a question about the contradiction they have created. Mode 2 is restricted to technical contradictions, because the TRIZ matrix is derived from engineering patents and does not map cleanly onto UX, service, or business-model problems (see [[triz]]); for those, the Orchestrator falls back to phase and synthesis modes.

Why TRIZ was merged into the Socratic Agent rather than kept as a separate agent: the original design had a separate TRIZ Agent. The same merging logic applies as for the Phase Gate: both TRIZ mode and Phase mode do the same thing. Recognize a pattern in the logged state; retrieve a matching structure from a knowledge base; convert it to a question. The only difference is which knowledge base is consulted. Two agents coordinating to produce the same output type (a question) adds handoff complexity without adding capability. One agent, two retrieval sources.

**Mode 3: Synthesis.** Triggered at phase transitions or when the Orchestrator detects that the decision log has grown significantly without an integrative review. The question is coherence-focused rather than gap-focused: given what has been decided, do the decisions hang together? Example: "Given what you found in Phase 2, which of these three observations most directly explains why you chose this direction in Phase 3?" Synthesis mode is not looking for gaps; it is checking whether the team's reasoning has internal consistency before they move on.

**Mode 4: Challenge.** Triggered when the Orchestrator detects consensus forming faster than the decision log can explain: multiple agents reporting alignment without much recorded debate, on a decision that has significant unresolved dependencies. The question asks for the strongest argument against the current direction. Its purpose is to make sure the team has actually thought the decision through, not to judge whether the team is right. The challenge can be overruled, and a silenced challenge is a fine outcome as long as the team answers it with its own human reasoning, which the feedback loop records. This mode exists because GenAI's RLHF training defaults toward validation and agreement ([[how-genai-works]] §Interaction), which at the team level amplifies groupthink dynamics ([Janis 1982](https://archive.org/details/groupthinkpsycho00jani)). Challenge mode is the system explicitly working against its own default. Because the same agreeable model cannot reliably challenge itself ([Sharma et al. 2023](https://arxiv.org/abs/2310.13548)), Challenge mode is run as a separate adversarial role rather than a self-critique. An explicit devil's-advocate persona reliably produces disagreement (about 99% versus about 48% at baseline) and has improved group decisions in a controlled study ([Inducing Disagreement in Multi-Agent LLM Teams](https://openreview.net/forum?id=mxBmj5LYU2); [Chiang et al. 2024, IUI](https://dl.acm.org/doi/10.1145/3640543.3645199)), and generating the challenge through a proposer-versus-challenger debate improves reasoning and reduces sycophantic convergence ([Du et al. 2023](https://arxiv.org/abs/2305.14325); [Liang et al. 2023](https://arxiv.org/abs/2305.19118)). Because the goal is to provoke the team's reasoning rather than to be correct, it does not matter that this disagreement is performed rather than genuinely held, and the team, not the model, adjudicates. The known tendency for a challenged model to cave under pushback ([Laban et al. 2023, FlipFlop](https://arxiv.org/abs/2311.08596)) is not a problem here, because the mode's job is to surface the counter-case, not to win the argument. The interview evidence for why this is necessary is in [[interviewee-1]]: the trust barrier named most directly was that AI "just says yes that's a great idea." Challenge mode is the design response to that.

## Feedback loop

Every Socratic Agent question requires a team response before the Orchestrator can escalate further on the same thread. There are three response types.

**Thumbs up.** The team found the question useful. Required: one sentence explaining why. The rationale requirement is not bureaucratic: a thumbs up without explanation tells the Orchestrator that the question landed, but not what made it land. That distinction determines whether the same mode should fire again in similar conditions. Without the rationale, the system has no calibration signal from positive outcomes, only from negative ones, which would bias it toward over-firing questions the team has never explicitly rejected.

**Thumbs down.** The team did not find the question useful. Two required fields: (a) what the team had already addressed that made the question redundant, and (b) why the timing was wrong. The "already addressed" field tells the Orchestrator whether the project state was stale (the reasoning had happened but not been logged) or whether the mode was wrong (the question type did not fit the moment). The "timing" field tells it whether to fire this mode less often or to check the state more carefully before firing.

**Ignoring (required documentation).** The team wishes to proceed without engaging with the question. Required: a written reason. This is the most important requirement in the feedback loop. Silent dismissal would make unanswered questions invisible to the Decision Logger's third source (Socratic fallback). A team that can dismiss questions without logging a reason will do so whenever the question inconveniences them, and the system will have no record of what was considered and rejected. The written reason, even a brief one, closes the gap between "the system asked" and "the team considered and moved on."

Why required responses at all: the standard failure mode for AI facilitation tools is that they become background noise. Questions accumulate unacknowledged; the team stops reading them; the system stops being useful. The required response structure prevents that failure mode and is also how the system generates the calibration data it needs to improve over time. A system that allows silent dismissal has no feedback signal except the absence of engagement, which is indistinguishable from the system failing.

## Milestone agents

Two agents are scoped for activation at milestones only, not continuous operation. They are not part of the core loop described above.

**Synthesis Agent.** Activated at phase transitions. It is distinct from the Socratic Agent's Mode 3: Mode 3 fires a single coherence-checking question in the moment, whereas the Synthesis Agent produces a full written synthesis document the team reviews at the boundary. Mode 3 probes; the Synthesis Agent compiles. It reads the full decision log and artifact log for the completed phase and generates a structured synthesis: what was decided, what was built, what the decision trail shows about the team's understanding, and where the synthesis has visible gaps. The team reviews this before the iNPD Agent's gate check runs. The purpose is to give the team a shared, written account of what they understood before moving to the next phase.

Why not continuous: synthesis mid-phase pulls the team into reflective work at a moment when they need to be in generative work. A synthesis question during active exploration is disruptive. At a phase boundary, it is the right intervention because a transition requires exactly this integration.

**Retrospective Agent.** Activated at project completion or a major milestone. Reads the full project history, including the feedback loop record, and generates a structured retrospective: which decisions turned out to be pivotal, which Socratic questions were initially dismissed but later revisited, and what patterns across the project are visible in hindsight. The purpose is transferable learning, not project management.

Why not continuous: retrospective work requires enough temporal distance from the decisions to be reflective. A mid-project retrospective is a status review, not a learning document, because the decisions are too recent and too live to evaluate dispassionately. Running it on a sparse log (early in the project) would produce low-value output.

Why both agents are milestone-only: both do synthesis over accumulated state rather than pattern recognition on current state. They need enough material to be useful, which is a time-threshold requirement the continuous agents do not have. Running them early produces noise; saving them for transitions and endings produces signal.

## Design principles that cut across the whole system

**Agents earn their separation.** An agent exists when it brings a distinct knowledge base or produces a categorically different output. When two agents apply the same knowledge to produce the same output type, they are merged. This is why TRIZ mode is inside the Socratic Agent, and why Gate Mode is inside the iNPD Agent.

**The LLM never makes a decision.** Every system output is either a question or a read from state. The team makes decisions; the agents document, check, and question them.

**Every intervention produces a record.** Whether a question lands or is rejected, the response goes into the log. The facilitation value of the system is partly in the questions asked; it is also in the documentation that the feedback loop generates as a side effect.

**Coverage over precision.** The Decision Logger uses three input sources because any one source will miss cases, and the monitoring agents overlap because no single agent sees the full picture. The goal is not to have one agent that is very precise; it is to have overlapping agents whose combined coverage is high.

## Sources

- Kambhampati, S. (2024). Can large language models reason and plan? *Annals of the New York Academy of Sciences*. https://arxiv.org/abs/2403.04121
- Kambhampati, S. et al. (2024). LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks. https://arxiv.org/abs/2402.01817
- Park, J. S. et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. https://arxiv.org/abs/2304.03442
- Packer, C. et al. (2023). MemGPT: Towards LLMs as Operating Systems. https://arxiv.org/abs/2310.08560
- Liu, N. et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. https://arxiv.org/abs/2307.03172
- Wegner, D. M. (1986). Transactive Memory: A Contemporary Analysis of the Group Mind. In Theories of Group Behavior. Springer. https://link.springer.com/chapter/10.1007/978-1-4612-4634-3_9
- Lewis, K. (2003). Measuring Transactive Memory Systems in the Field: Scale Development and Validation. *Journal of Applied Psychology*, 88(4), 587–604. https://doi.org/10.1037/0021-9010.88.4.587
- Collins, A. and Stevens, A. L. (1982). Goals and strategies of inquiry teachers. In R. Glaser (Ed.), *Advances in Instructional Psychology* (Vol. 2, pp. 65–119). Lawrence Erlbaum. (Book chapter; no open-access URL.)
- VanLehn, K. (2011). The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems. *Educational Psychologist*, 46(4), 197–221. https://www.tandfonline.com/doi/abs/10.1080/00461520.2011.611369
- Woolley, A. W. et al. (2010). Evidence for a Collective Intelligence Factor in the Performance of Human Groups. *Science*, 330(6004), 686–688. https://www.science.org/doi/10.1126/science.1193147
- Janis, I. L. (1982). *Groupthink: Psychological Studies of Policy Decisions and Fiascoes* (2nd ed.). Houghton Mifflin. https://archive.org/details/groupthinkpsycho00jani
- Altshuller, G. S. (1984). *Creativity as an Exact Science: The Theory of the Solution of Inventive Problems.* Gordon & Breach. https://books.google.com/books/about/Creativity_as_an_Exact_Science.html?id=8BBRAAAAMAAJ
- Cagan, J. and Vogel, C. M. (2002). *Creating Breakthrough Products: Innovation from Product Planning to Program Approval.* (2nd ed. 2013.) https://press.etc.cmu.edu/books/creating-breakthrough-products-special-second-edition
- Sharma, M., Tong, M., et al. (2023). *Towards Understanding Sycophancy in Language Models.* https://arxiv.org/abs/2310.13548
- Du, Y. et al. (2023). *Improving Factuality and Reasoning in Language Models through Multiagent Debate.* https://arxiv.org/abs/2305.14325
- Liang, T. et al. (2023). *Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate.* https://arxiv.org/abs/2305.19118
- Wang, X. et al. (2022). *Self-Consistency Improves Chain of Thought Reasoning in Language Models.* https://arxiv.org/abs/2203.11171
- Zheng, L. et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* https://arxiv.org/abs/2306.05685
- Laban, P. et al. (2023). *Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment.* https://arxiv.org/abs/2311.08596
- Chiang, C.-W. et al. (2024). *Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate.* IUI 2024. https://dl.acm.org/doi/10.1145/3640543.3645199
- *Inducing Disagreement in Multi-Agent LLM Executive Teams: Only the Devil's Advocate Works.* OpenReview. https://openreview.net/forum?id=mxBmj5LYU2
- *Meeting Action Item Detection with Regularized Context Modeling* (2023). https://arxiv.org/abs/2303.16763
- *A Wizard or a Fool? Initial Assessment of a Wizard of Oz Agent Supporting Collaborative Virtual Environments* (2022). HAI. https://dl.acm.org/doi/10.1145/3527188.3563930
