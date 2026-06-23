---
title: "Interviewee 1: Analysis"
type: analysis
created: 2026-06-14
updated: 2026-06-14
tags: [interviews, analysis, innovation-teams, ai-in-teams, thematic-analysis]
---

# Interviewee 1: Analysis

A detailed qualitative analysis of the first interview. The structured record is [[interviewee-1]], the full transcript is [[interviewee-1-transcript]], and the supporting literature is [[team-dynamics]]. This is one case, so everything here is a hypothesis to test against later interviews, not a finding.

## Method and approach

This is a single semi-structured interview of about 72 minutes, recorded as a voice memo and machine-transcribed (Whisper, `small` model), then cleaned into intelligent verbatim. The analysis uses a reflexive thematic approach: read the transcript closely, attach short codes to meaningful segments, group codes into candidate themes, and check each theme back against the transcript and against the [[team-dynamics]] literature. Quotes are drawn from [[interviewee-1-transcript]].

Two caveats shape the reading. First, the interviewer is also the project lead, so the questions steer toward AI, teams, and stuckness; the participant's framing is partly a response to that steering. Second, the participant is currently interning on an AI voice product, which may make her more fluent and more critical about AI than a typical designer.

## Participant context

A design and UX professional from an innovation agency, with experience spanning visual design, UX, and turning research into insights, in roles from junior designer up to a managerial position that gave direction and dealt with clients. She has worked on a spectrum from open-ended projects (client has a goal, not a path) to rigid ones (technology fixed, design must conform). At the time of the interview she was interning on an AI voice product. She is articulate about process and unusually candid about interpersonal friction.

## Coding map

The codes that recurred, grouped into the themes developed below:

- Purpose and goals: "no common goal," "common villain," personal vs shared objectives, interest in the topic.
- Trust and relationships: trauma-bonding, give and take, respect for contribution, intimidating-but-effective leads, hierarchy vs peer-to-peer.
- Cognition and getting unstuck: sounding board, thinking out loud, going in circles, overthinking vs "just start somewhere."
- Persuasion and decisions: anticipating each stakeholder's questions, asymmetric effort on the preferred concept, evidence-tied arguments, deferring to stake.
- Knowledge and coordination: the truth document, knowledge-sharing workshops, access asymmetries, messy research files, rotation in and out.
- AI in practice: fast document absorption, unverified "shaky foundations," grounded confirmation, sycophancy, validation, idea generation as aggregation.
- Trust in AI: transparency, version and context integrity, non-flattery.

## Themes

### 1. Shared purpose is the load-bearing variable

Across every team story, the presence or absence of a common goal is what separates good from bad, more than skill, seniority, or process. The clearest bad team is defined by its absence: "there was just no common goal or common thing to work toward, because everyone had different objectives," with the rot visible before work began, when two members announced they would not invest. Asked what she would change, she does not reach for process; she says "the people."

What is distinctive is her account of how purpose gets manufactured when the project itself does not supply it: an external adversary. "For the hackathon it was winning the hackathon; for the client it was winning over that one unreasonable guy; for me versus the other junior designers it was winning against the manager." This is a lay version of a superordinate goal, and it maps onto the shared-purpose discipline in [[team-dynamics]] (Katzenbach & Smith). The practical implication for the project is that a facilitation tool that helps a team name a shared goal, even a temporary external one, may matter more than any ideation feature.

### 2. Trust forms through shared adversity and reciprocity, not time

Trust in her stories is forged fast and through events, not accumulated slowly. She bonds with an intimidating, unfriendly lead within one project because they faced a hostile client gatekeeper together: seeing the normally unflappable lead "holding her head" created the opening, and "we had this common villain, almost." The mechanism she names for ongoing trust is reciprocity: "there just needs to be some sort of give and take... you have to respect their contribution and they need to respect yours. If you feel like one of you is doing too much, that's not going to click." The trust-through-safety mechanism is psychological safety ([[team-dynamics]], Edmondson), and the reciprocity she emphasizes lines up with the collective-intelligence finding that social sensitivity and balanced turn-taking predict group performance more than individual ability ([[team-dynamics]], Woolley).

### 3. Thinking is dialogic, and the sounding board is the core mechanism

This is the theme most central to the project, and she states it unprompted. "I do my best thinking talking to somebody, when I have a sounding board... hearing myself talk, or hearing somebody else's different opinion, restructures how I'm thinking. I tend to go in a circle with things, so hearing someone else talk about it pulls me out of that." Two features matter for designing an AI questioner. First, the value is restructuring, not answering: the other party changes how she thinks, not what she concludes. Second, she names the opposite failure mode too, overthinking, which she breaks by acting: "I have to just start somewhere, and as I'm doing that I eliminate and figure out where to go." A useful intervention therefore has two jobs depending on the stuck state: when she is looping, reframe; when she is frozen, prompt a concrete first move.

### 4. Persuasion is anticipatory design

She treats getting a concept accepted as a design problem in its own right. She does not argue harder; she pre-empts. She models each decision-maker's question set by level ("my lead, very granular... the manager, slightly broader... the client, even broader, why this over something they've seen elsewhere") and structures the same concept differently for each. She also deliberately invests unequally: "I would not put equal effort into three concepts; I'd put more effort into the one I thought was better," because a better-fleshed option "answers more questions in their head." This is sophisticated and slightly manipulative, and she is self-aware about it ("ways we've strong-armed clients"). For the project it suggests that practitioners already run a private model of their stakeholders' questions; an AI that surfaces or pressure-tests that model could be valuable.

### 5. Knowledge is a transactive system, held together by hand

Her "truth document" is a near-textbook transactive memory system ([[team-dynamics]], Wegner; Lewis): a single indexed record of confirmed decisions, timeline, objective, hierarchy, and links to concept files, used to onboard members who rotate in and out. It works because it carries specialization, credibility, and coordination. The friction points are also classic: technical content too dense for juniors, access and permission asymmetries ("some artifacts are business plans I don't have access to"), and research files where the "final clarified" version is buried among raw data points. Notably, she is the one sent "to hunt through the research files," which is where she sees the strongest case for AI.

### 6. Disagreement is settled by evidence and stake, not authority

Her conflict repertoire is structured: find a halfway point, split the work by conviction, merge concepts, or pre-build rebuttals. The throughline is moving disagreement off personalities and onto evidence. With a singular-direction lead, "if you have direct proof to tie back to your argument, then fine, I'm defeated; you have a source point... I have a user quote." Where evidence runs out, she defers by stake: "whoever has the bigger stake in that decision, you defer to them." This sits on top of the contested conflict literature in [[team-dynamics]] (Jehn vs De Dreu & Weingart): her practice is essentially to convert relationship-tinged disagreement into checkable task disagreement, which is the move the research suggests is safest.

### 7. A lay theory of AI that mirrors the wiki's adaptor thesis

Without the vocabulary, she draws the same line this wiki draws. AI is excellent as a grounded retrieval tool ("reference only this doc and give me the answer, a lot faster") and as a confirmer of facts from your own documents ("it's not sourcing the internet and making something up"). It is untrustworthy for two generative jobs. For validation, because "AI is always going to shift toward praising you, and that's not the point of validation." For ideation, because "innovation is trying to come up with something new, and AI is very good at aggregating the most successful, most popular information," so compiling popular existing material will not produce the genuinely new. Her test case is Spotify Wrapped, a cross-domain leap from year-in-review stats into music: "would AI come up with an idea as innovative as Spotify Wrapped? I don't know. I think so." This is, in plain language, the claim that GenAI is a high-level adaptor that interpolates within its paradigm rather than shifting it (see [[genai-on-the-adaption-innovation-spectrum]] and [[what-genai-is-good-and-bad-at]]). The "shaky foundation" she describes, building on unverified output that later crumbles, is the verification weakness in lived form.

### 8. Trust in an AI tool has three concrete requirements

She is specific about what would make her trust a tool: transparency ("I should be able to track down where the info is coming from or why it's telling me something"), version and context integrity ("are you pulling from something that has now been scoped out, or answering with a merged context instead of just what I need right now?"), and no sycophancy. The sycophancy point is sharp: the burden of catching flattery currently falls on the user's self-awareness, and "people less familiar with AI won't have that awareness... you might start to doubt yourself." This maps to the RLHF caveat in [[how-genai-works]] and is, in effect, a design spec.

## Cross-cutting tensions

Three internal tensions are worth holding rather than resolving, because they are likely to recur:

- Equality versus hierarchy. She prizes give-and-take and equal respect, yet she also says flat peer-to-peer teams are harder precisely because no one has the authority to be blunt and move things along. Coordination, for her, sometimes needs a hierarchy that contradicts the equality she values.
- Distrust of AI ideation versus a hedged yes. She argues AI cannot make a Spotify Wrapped leap, then immediately closes with "I don't know, I think so." Her stated position is more skeptical than her intuition.
- Teamwork and outcomes can decouple. Her most-repeated structural observation is that a great team can produce a bad outcome ("teamwork great, outcome shite") when an external blocker dominates. Team health is not a proxy for results, which complicates any single success metric.

## Salience

The points she returned to without prompting, and which therefore carry weight, are: the need for a common goal, the sounding board as where thinking happens, verification and the shaky foundation, and the praise response. These four are the strongest candidates to look for in the next interviews.

## Design implications for the AI questioner

Read as requirements for the project's tool, her account suggests:

- Be a sounding board that restructures thinking, not an answer engine. Diagnose the stuck state: reframe when the person is looping, prompt a first concrete move when they are frozen.
- Help a team name a shared goal, including a temporary external one, before doing anything else.
- Ground everything in the team's own record (the truth document and research files), with traceable sources, which is the [[rag-explained]] pattern she independently asked for.
- Get version and context right: answer from current, scoped-in material, not merged or stale context.
- Do not flatter, and do not validate. Stay on the questioning side; leave validation to users and the market.
- Surface, rather than replace, the practitioner's private model of stakeholder questions.

## Tentative mapping to iNPD phases

Provisional, to refine across interviews; the four phases are defined in [[inpd]]. Her knowledge-and-research-hunting pain sits in understanding users and identifying opportunities (finding and trusting the right inputs). Her persuasion and concept-selection work sits in conceptualizing and realizing (getting a direction accepted). Her stuck-team and trust stories cut across all phases, suggesting that the deepest deadlocks are about purpose and trust rather than any single phase's task.

## Limitations and reflexivity

This is one retrospective, self-reported account from an agency context, filtered through a machine transcript that will contain errors and through an interviewer who is also a stakeholder in the conclusion. Social-desirability and recency effects are likely, and her current AI-product internship probably sharpens her AI views. Names and identifying details are removed; she is referred to only as Interviewee 1. None of the themes should be generalized until corroborated by further interviews.

## Open questions for the next interviews

- When a team was genuinely stuck, what specifically unblocked it, and could a well-timed question have done the same, or only a person?
- Does the "common villain" pattern recur, and is a manufactured external goal as effective as an intrinsic one?
- Where do practitioners draw the line between AI as grounded resource and AI as idea source, and does it match this account?
- What would a non-flattering, source-tied AI questioner have to do for them to trust it inside a live project?
