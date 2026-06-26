---
title: "Interviewee 2: Analysis"
type: analysis
created: 2026-06-14
updated: 2026-06-14
tags: [interviews, analysis, innovation-teams, ai-in-teams, thematic-analysis, authority, feedback]
---

# Interviewee 2: Analysis

A detailed qualitative analysis of the second interview. The structured record is [[interviewee-2]], the full transcript is [[interviewee-2-transcript]], and the supporting literature is [[team-dynamics]]. This is one case, so everything here is a hypothesis to test against the other interviews, not a finding. Where it agrees or disagrees with [[interviewee-1-analysis]] is noted, because the contrast between the two is where most of the value sits.

## Method and approach

This is a single semi-structured interview, recorded and transcribed, then cleaned into intelligent verbatim and anonymized. The analysis uses a reflexive thematic approach: read the transcript closely, code meaningful segments, group codes into candidate themes, and check each theme back against the transcript and the [[team-dynamics]] literature. Quotes are drawn from [[interviewee-2-transcript]].

Two caveats shape the reading. First, the interviewer is also the project lead, so the questions steer toward AI, teams, and stuckness, and the participant's framing is partly a response to that steering. Second, the participant identifies strongly as a craft designer and is openly hostile to AI in the creative process, which sharpens her anti-AI-in-creative stance and should be read as a position, not a neutral measurement.

## Participant context

A designer with industry experience before CMU: product design at a manufacturing company, building internal tools and dashboards to cut manual work, then about eighteen months as a UX designer at a gaming company. The gaming role is worth noting because it trained a particular kind of constrained creativity: the game was in decline, the audience was fixed, and the brief was retention and monetization, so "the narrower it became, the more it made me think outside the box." She now studies in a CMU master's program and spoke mainly about an innovation capstone (referred to as the IPD or capstone team) and her UX role, and she is currently in a research-assistant position where her AI use is mostly source-finding. She is reflective about process and unusually direct about where AI has disappointed her.

## Coding map

The codes that recurred, grouped into the themes developed below:

- Purpose and alignment: shared disappointment, aligned low expectations, grades as the motivator, investment rising by phase three, personal versus shared goals at CMU.
- Roles and reciprocity: self-assigned "separate boxes," complementary strengths, rotating expectation-setter and expectation-manager, gratitude and affirmation, uniformly positive peer evaluations, the engineer teaching the group patiently.
- Stuckness: cannot see a path forward, process rigidity (phase four equals phase one), circular returns, stuck together, reliance on faculty, panic-driven fleshing out, reverting to the original solution.
- Authority and feedback: approved-then-rejected reversal, faculty feedback as "concrete" and a set direction, peer feedback as "constructive," compliance versus consideration, speaking for the group, "we're all deciding together."
- Knowledge and coordination: phase-structured docs plus Figma and WhatsApp, hard onboarding for the capstone, highly ordered handoff docs at work, role-based reading order.
- Cognition: real thinking in person, reading faces, drawing out introverts, online calls only for deciding what to sort.
- AI in practice: source-finding, surface-level synthesis redone by hand, presentation-review for story structure, running two models and comparing, transcription paraphrase failure, design homogenization, workload inflation.
- AI trust and boundaries: refiner not initiator, no AI in early framing or research, trust through authority validation, opt-in control, feedback "in the form of what the faculty would say."

## Themes

### 1. Alignment beats enthusiasm, even when the alignment is shared apathy

The capstone team worked not because anyone cared about the project but because everyone agreed, out loud, that they did not. "None of us were interested in the project, so in the first few days we quickly realized where we all stand," and that shared disappointment "established that we were all on the same page." This is a sharp variant of the shared-purpose finding in [[team-dynamics]] (Katzenbach & Smith). Interviewee 1 manufactured purpose through an external adversary, a "common villain"; Interviewee 2's team manufactured cohesion through a shared negative orientation toward the project itself. The common element across both is not the content of the goal but the synchronization: everyone knowing where the others stand. The load-bearing variable is alignment, and a low-investment alignment was enough to produce high-functioning teamwork.

Two qualifications matter. Investment was not static: by the third phase the team "actually really got into the project," pulled in by the sheer volume of work rather than by interest. And the alignment had a ceiling, which surfaces in theme 3: a team aligned on not caring will tend to settle rather than push, and this one reverted to its earliest solution.

### 2. Roles self-organized, and gratitude did the maintenance

The division of labor required no negotiation. "We put ourselves into separate boxes almost immediately," each person claiming a strength (business, engineering, research and design) with "nobody fighting over it." This is a transactive memory system forming by self-selection ([[team-dynamics]], Wegner; Lewis): specialization assigned, credibility granted, coordination implicit. What kept it stable was an explicit regulatory pairing she describes, where "someone wanting to do more and someone else managing expectations" traded off, and those roles rotated. That expectation-management role is emotional and strategic regulation, not task work, and she names it as one of the most helpful dynamics.

The glue was active gratitude. Because no one was doing work they wanted, "every time someone pushed themselves to do a bit more, we were hyping each other up," and peer evaluations were uniformly positive. Read generously, this is psychological safety in practice ([[team-dynamics]], Edmondson). Read critically, uniformly positive evaluations and the claim that no disagreement ever went unresolved (theme 4) could also be harmony-seeking and conflict-avoidance, which is easier to sustain precisely because the stakes were low. Both readings should be held; the next interviews can test which travels to higher-stakes teams.

### 3. The real stuck-maker was the process, not ambiguity

Her most distinctive stuckness account is not about confusion. "It wasn't even that it was ambiguous, we just couldn't see a path forward," and the specific source of frustration was being made to keep cycling through the phases when "at the end of phase four the solution we had was basically the same as phase one." The structured process itself generated felt-pointless rework. This is an important counter to a naive reading of the project, which assumes structure helps stuck teams; here the iNPD phase discipline ([[inpd]]) was the irritant, because it demanded re-derivation of a decision the team had already settled.

There is a clean design opportunity in this. A facilitator that can recognize "the team has a settled answer and the remaining value is documenting and justifying it, not reopening it" would have helped, which routes directly to the Synthesis Agent and Decision Logger in [[innovation-team-agent-architecture]] rather than to another question. The deepest single frustration, though, came from authority, which is theme 4: faculty "approved something and then the feedback the next day was completely different," and that reversal, not the problem itself, triggered the worst all-nighter.

### 4. Authority changes how the same feedback is received

This is the interview's central new contribution. Identical content lands differently depending on who says it. Faculty feedback "feels very concrete," a set direction to comply with: "if they said you should consider this, we would only consider that." Peer or non-authority feedback "feels a lot more constructive," something to weigh and build on: "if you or another person said something, even three opinions, we'd think this makes sense, we can focus on the first part." The approved-then-rejected episode was destabilizing precisely because authority feedback carries binding force, so a reversal does not read as new information, it reads as the ground moving.

The implication for an AI questioner is double-edged and sets up the core tension of this interview. On one hand, it argues for a low-power, non-directive questioner, because a tool without positional authority gets engaged with more openly, as a prompt to consider rather than an order to obey. This is direct support for the Socratic, non-answering stance in [[genai-as-socratic-facilitator]]. On the other hand, theme 5 shows she only trusts such a tool when an authority later blesses it, which a low-power questioner by definition is not.

### 5. Trust is anchored to authority, which is the opposite of Interviewee 1

Asked what would make her trust an AI tool, she does not reach for transparency or non-flattery, which were Interviewee 1's answers. She reaches for external validation: "if I made the changes and the faculty visibly approved the direction, I'd trust it more, because I'd know it's the right direction," and at work "that onus would go to the manager." Trust is downstream of an authority confirming the tool was right. Interviewee 1's trust model was internal, epistemic integrity (traceable sources, correct context, no sycophancy); Interviewee 2's is external, authority validation. See [[interviewee-1-analysis]] theme 8 for the contrast.

The tension is real and should not be smoothed over. She wants the tool to be low-power so its feedback is received openly (theme 4), yet she trusts it only when high-power authority confirms it. The resolution candidate, worth testing rather than asserting, is to position the tool as pre-review preparation: a non-binding questioner during the work that helps the team arrive where the authority would have pointed, so it earns trust through downstream validation while never itself issuing a directive. That reframes the contradiction as a sequence, questioner first, validation later, rather than a single role.

There is also a quieter risk here. A participant this oriented toward "what the faculty wanted" is exactly the kind of user for whom a validating AI is most dangerous, because she is primed to defer. Interviewee 1 named the burden of catching flattery; Interviewee 2 embodies the user who would not catch it. That makes the non-sycophancy requirement from [[how-genai-works]] more pressing in her case, not less.

### 6. AI belongs to the late phases: a refiner, not an initiator

She draws a precise phase line. AI is "a big no" in the early work of "understanding what we actually want the problem to be" and in research and scoping, because "it gave us everything generic that wasn't working with what the faculty wanted." It becomes useful once the direction is set, "to ideate, analyze, or give more suggestions," and "the work before that should still happen from us, it should be a more refining thing." Mapped to [[inpd]], she wants AI kept out of Identify and Understand and allowed into Conceptualize and Realize.

This sits in productive tension with [[innovation-team-agent-architecture]], which proposes phase-based questioning in every phase. The reconciliation is that question type, not question presence, is what should vary. In the early phases the right move may be to protect and probe the team's own framing (a question that widens the search or stress-tests an interpretation) rather than to inject AI-generated content, which is the thing she objects to. Her objection is to AI supplying the substance early, not to being asked a good question early, and the architecture's questioner is the latter.

### 7. A lived catalog of AI's limits that matches the wiki

Her concrete AI experiences independently reproduce several of the wiki's claims. Synthesis of three documents "was just the most surface-level thing, everything that matched," with "no nuance," so she redid it by hand and only then got the insights she wanted. That is Interviewee 1's aggregation point from a different direction: AI returns the overlap, not the synthesis, which is the high-level-adaptor thesis in lived form ([[genai-on-the-adaption-innovation-spectrum]], [[what-genai-is-good-and-bad-at]]). The transcription episode, where she told it to transcribe an image verbatim and "it paraphrased everything from its own understanding," is a failure to respect an explicit constraint and, in her framing, a failure of self-knowledge: "there should be some awareness of AI's limitations." Her dislike of AI in visual communication, where "everything just looked the same," is interpolation within a paradigm experienced as homogenization.

One coping strategy is notable as design evidence. For the presentation review, the team ran the same material through two different models and compared, "I was running one and someone else was running another, and the responses were very different, we took that into account." That is a lay version of self-consistency and ensembling, the same reliability move the architecture proposes for its own detection ([[innovation-team-agent-architecture]]). Users already triangulate across models by hand; the system formalizing that is consistent with how she already works.

### 8. Knowledge held by hand: fine for the team, not for a newcomer

The capstone's memory was phase-structured documents, a shared doc, a Figma, and a WhatsApp chat, organized by phase. It worked for the team but failed the onboarding test outright: asked how a new joiner would catch up, she said flatly, "they would have a very difficult time." Her gaming job is the contrast, where ordered handoff docs (product spec, design spec, design document, art, dev tools) were "intended so that if someone new is coming in they know where to pick up almost immediately," with a role-based reading order. The difference is exactly the externalized-shared-state argument behind the [[getting-the-most-out-of-llms]] LLM-Wiki pattern and the Tier-1 Project State in [[innovation-team-agent-architecture]]: a record that works because the team already holds the context versus a record structured so a newcomer, or an agent, can reconstruct it. For a system that depends on reading the team's logged state, this is the difference between a usable substrate and an unusable one, and it is a cultural and process problem as much as a technical one (the coverage limitation in [[genai-as-socratic-facilitator]]).

## Cross-cutting tensions

Several internal tensions are worth holding rather than resolving:

- Low-power tool versus authority-validated trust. She wants the questioner to lack authority so its feedback is received openly, yet she only trusts it once an authority confirms it. This is the design knot of the whole interview.
- Stated anti-AI stance versus actual practice. She is emphatic that AI does not belong in design or research, then reports using it well for ideation expansion, presentation review, and source-finding. Her position is more anti-AI than her behavior.
- Smoothness as safety or as avoidance. Uniformly positive evaluations and no unresolved disagreements may reflect genuine psychological safety or low-stakes harmony-seeking. With a team aligned on not caring, smoothness is cheap.
- Real thinking is in person. She locates all real thinking in face-to-face meetings, where you can "see how they react" and draw out introverts, and none in online calls. This aligns with the equal-turn-taking finding in [[team-dynamics]] (Woolley) and is a constraint on any remote or asynchronous facilitation tool, which the Collaboration Agent in [[innovation-team-agent-architecture]] is, by design, async.

## Salience

The points she returned to without prompting, and which therefore carry weight, are the authority-versus-peer feedback distinction, AI as a refiner to be kept out of early framing, the destabilizing approved-then-rejected reversal, and AI's lack of nuance in synthesis. These four are the strongest candidates to look for in the next interviews, and the first of them is the most novel relative to Interviewee 1.

## Design implications for the AI questioner

Read as requirements for the project's tool, her account suggests:

- Operate as a low-power, non-binding questioner during the work, since non-authority feedback is engaged with more openly than authority feedback. This supports the Socratic, non-answering stance.
- Design for downstream authority validation to earn trust: position the tool as pre-review preparation that helps a team arrive where its faculty or manager would point, rather than as a source of verdicts.
- Vary question type by phase. In Identify and Understand, protect and probe the team's own framing rather than inject content; in Conceptualize and Realize, offer contradiction, criteria, and synthesis questions.
- Add a move for the settled-decision-and-rigid-process case: help the team document and justify a decision it has already made rather than force re-derivation, routing to the Decision Logger and Synthesis Agent.
- Make the shared state reconstructable by a newcomer, not just legible to the team that already holds the context, which is what makes the logged record usable by the agents at all.
- Respect explicit constraints and signal its own limits, the lesson of the transcription failure: do not paraphrase when asked to preserve, and be honest about what it cannot reliably do.
- Treat the non-sycophancy requirement as more urgent for authority-deferring users like her, who are least likely to catch flattery themselves.

## Tentative mapping to iNPD phases

Provisional, to refine across interviews; the four phases are defined in [[inpd]]. Her hard line against AI sits in Identify and Understand (problem framing, research, scoping). Her stuckness sits at the phase gates and in Realize, where the process forced re-derivation of a settled decision and scope kept reopening. The authority-feedback dynamic cuts across all phases, since faculty review punctuates every gate. Her account suggests the deepest deadlocks are about process rigidity and authority pressure rather than any single phase's task, which echoes Interviewee 1's finding that purpose and trust cut across phases.

## Limitations and reflexivity

This is one retrospective, self-reported account from a low-investment class capstone, cleaned from a transcript with some speech-to-text ambiguity (tool names were normalized, and a few teammate references were inferred from context before being anonymized to roles). The capstone's defining feature, that no one cared about it, makes its smooth dynamics a weak guide to high-stakes teams, where disagreement is costlier. The participant's strong craft-designer identity sharpens her hostility to AI in creative work, and the interviewer is a stakeholder in the conclusion, so social-desirability and steering effects are likely. Names and identifying details are removed; she is referred to only as Interviewee 2. None of the themes should be generalized until corroborated.

## Open questions for the next interviews

- Does the authority-versus-peer feedback asymmetry recur, and is a low-power AI questioner reliably engaged with more openly than an authoritative one?
- Do trust models split cleanly along an integrity axis (Interviewee 1) versus an authority axis (Interviewee 2), or is that a false binary that more interviews collapse?
- Does the "no AI in early framing, yes in late refinement" phase line hold across participants, and does it match the architecture's question-type-by-phase idea?
- Is "aligned apathy" a genuine team mode that produces real cohesion, or an artifact of low-stakes class projects that vanishes when the work matters?
- When the stuck-maker is the process itself rather than the problem, what facilitation move helps, and is it a question at all or a synthesis?
