---
title: "Interviewee 3: Analysis"
type: analysis
created: 2026-06-14
updated: 2026-06-14
tags: [interviews, analysis, innovation-teams, ai-in-teams, ownership, conflict, scoping, thematic-analysis]
---

# Interviewee 3: Analysis

A detailed qualitative analysis of the third interview. The structured record is [[interviewee-3]], the full transcript is [[interviewee-3-transcript]], and the supporting literature is [[team-dynamics]]. This is one case, so everything here is a hypothesis to test against the other interviews, not a finding. The contrasts with [[interviewee-1-analysis]] and [[interviewee-2-analysis]] are called out, and this interview is unusual because the participant reacted directly to the project's own design.

## Method and approach

A single semi-structured interview, recorded, transcribed, cleaned into intelligent verbatim, and anonymized. Reflexive thematic approach: code meaningful segments, group into themes, check each theme against the transcript and the [[team-dynamics]] literature. Quotes are drawn from [[interviewee-3-transcript]].

Three caveats shape the reading, one of them sharper than usual. The interviewer is the project lead, so the questions steer toward AI, teams, and stuckness. The participant has an engineering and autonomous-systems leaning, so his AI examples are technical and his bar for "does this actually work" is quantitative. And, most importantly, the interviewer was a former teammate of the participant and described the project's own design to him mid-interview, so part of this transcript is a participant critiquing the interviewer's artifact to the interviewer's face. That invites both candor and a wish to be constructive, and both are visible.

## Participant context

A CMU master's student with an engineering orientation. He spoke about three projects: an early invisible-technology concept (a small team that included the interviewer), a sponsored innovation capstone that proposed an invisible city transportation system, and a current solo project on diabetes management for non-clinical families. He works comfortably with technical material (an autonomous-racing path-planning project recurs as his AI example) and has built tooling for his own AI use, including a critique prompt and an attempt at a Claude skill file to scope research. He is articulate and strongly normative about how teams should behave, which is the spine of the interview.

## Coding map

The codes that recurred, grouped into the themes below:

- Conflict and discussion: conflict of opinion as the start of discussion, stress-testing, heated-but-respectful, stepping back, supporting points.
- Ownership and accountability: contributing meaningfully, knowing where everyone stands, becoming invisible, the empty claim, taking emotion out and talking it through.
- Anti-mediation: "let it go" as harmful, confronting the mediator, mediation that hinders progress.
- The design reaction: Collaboration Agent takes team spirit away, running from accountability, short-term help versus long-term harm, the agree/disagree synthesis.
- AI sycophancy and control: brutal-critique prompt, numbers and edge cases, no verdicts, plain pros and cons, unbiased interview analogy.
- AI limits: lacks your context, pushes the already-done, fails at novelty, reason-from-logic workaround.
- AI uses: laborious work, drafting, diagrams, the pawned-off design section, design thinking as inputs-not-outputs.
- Scoping: the fuzzy front-end, too much or too little detail, enough-to-work-around, stop-loss, the desired scoping mechanism.
- Knowledge and coordination: per-phase docs with tabs, the whiteboard, different understandings of the same word, phasing deliverables to resolve.

## Themes

### 1. Conflict is the engine of the team, and mediation is the threat

This is his organizing belief, and it is the strongest pro-conflict stance across the three interviews. "The discussion always starts at the conflict of opinion. If there is no conflict of opinion, you would never be able to explore different elements," and "conflicts get more results out of a discussion than having everybody agree." He frames opposition as the only reliable way to stress-test an idea, because you will not stress-test something you are attached to. This is, in the language of [[team-dynamics]], a strong endorsement of constructive task conflict (Jehn; De Dreu and Weingart), and his one management rule, step back when it gets heated and resume, is precisely the move that keeps task conflict from curdling into relationship conflict.

The corollary, which is distinctive, is that he treats mediation as the danger rather than conflict. A teammate who said "let it go, let it go" during a heated discussion was, to him, doing harm, because smoothing the conflict let a weakly-supported idea survive and hid how people actually thought. He confronted that person directly. Where most facilitation instincts try to reduce friction, he wants friction protected, and only the heat managed. Any facilitation design has to reckon with a user who would read a peace-making intervention as sabotage.

### 2. Ownership is the point of a team, and it is earned through the hard conversation

His second pillar is ownership, and he ties it tightly to the first. You build ownership by contributing meaningfully and, crucially, by knowing where everyone stands: "I should know whether you're on the same page as me, because then I know what to discuss and how." A disengaged member becomes "invisible," and their claim on the project is "an empty claim... it's not really yours because you didn't do anything." The mechanism that produces ownership is the same uncomfortable discussion from theme 1: taking the emotion out yourself and talking it through is how you both resolve the issue and learn how your teammate reasons. This sets up his objection to the design, because the design offers to do that uncomfortable thing for him.

### 3. He rejects the Collaboration Agent, on ownership grounds

Asked directly about the Collaboration Agent (complain to it, it strips the emotion and fires a neutral question to the team), he gives the sharpest critique of the project's design in any interview. His objection is not technical, it is moral and developmental: "that's what I should be doing... if you give that job to AI, you're basically killing that team spirit," and it "lets you take the accountability away and give it to the AI... you're running away from the accountability of owning up to your problem." His distinction is short-term versus long-term: in a brief capstone the agent can be helpful, but over time it prevents the team from building the mutual model of how each person thinks, leaving everyone "separated as well as connected," resolving issues without anyone learning anything.

This deserves to be taken at full strength rather than explained away. The design's defense is that the system only asks a question and the team answers with its own reasoning, so the humans still do the thinking. But his point cuts underneath that: even a neutral, de-identified question lets the complainer avoid the specific, attributed, face-to-face conversation that he believes is where ownership is forged. The agent removes the friction of confrontation, and for him that friction is the value. The honest implication is that the Collaboration Agent's confidentiality feature, which Interviewee-1-style trust concerns would praise, is exactly what this participant distrusts, because privacy is what lets people dodge the accountable conversation.

### 4. But he hands the design a real improvement

Having rejected the single-question mechanism, he constructs a better one, unprompted. The system should not just fire a question; once it has the peers' inputs it should "report two things, the commonalities between all the peer reviews and the differences," the points the team agrees on and why, and the points it disagrees on. His reasoning is that a complaint contains noise ("I would be speaking everything out, whether it's important or not"), and the value the AI can add without stealing the conversation is distillation: showing the team the actual shape of its agreement and disagreement so it can "frame the problem properly and start discussing." This is a genuine extension to [[innovation-team-agent-architecture]]: an Orchestrator or Collaboration output that is a structured agreement/disagreement map across members, which frames a human discussion rather than substituting a question for it. It also answers his own objection, because a map that the team must then discuss preserves the accountable conversation instead of replacing it.

### 5. A scoped questioner is welcome, and the welcome is conditional on scope

He separates the Socratic questioner from the Collaboration Agent and is positive about the former, with a condition. An AI that asks questions is helpful "as long as it limits itself to the scope of the project," and he gives two reasons that are useful design rationale. First, audience rehearsal: "if AI is asking that question, some other time the audience would ask the same question," so the questioner is valuable as a stand-in for the eventual evaluators. Second, multi-lens coverage in unfamiliar domains: for his diabetes project he wants questions across clinical, product, customer, and regulation perspectives, because he is new to the domain and cannot generate those lenses himself. Both support the Socratic design in [[genai-as-socratic-facilitator]], and the first suggests an explicit "audience simulation" framing that the wiki does not currently name.

### 6. He engineers against sycophancy, and refuses verdicts entirely

He is the most operationally anti-sycophancy participant. He does not just dislike the praise reflex, he has built around it: a deliberately "brutal" critique prompt scoured from the internet, and a habit of demanding numbers, "what percentage deals with normal cases, what with edge cases, how reliable," and the gaps where the idea fails. This is a lay quantification of reliability that mirrors the wiki's own emphasis on verification ([[what-genai-is-good-and-bad-at]]).

He extends this into a hard line that maps onto the architecture's central invariant. AI "should not come up with any kind of proposals" or verdicts: "I don't want its opinion about which idea is better. I want to make that decision for myself. Even if it's the wrong choice, I'd at least know why I made it." His analogy is the unbiased interview that must not lead. This is the "the LLM never decides" rule of [[innovation-team-agent-architecture]] arrived at independently, and pushed further: not even a recommendation, only the pros and cons. That is stronger than the current Socratic design, which still selects which question to ask; he would want even that selection to avoid implying a verdict.

### 7. AI lacks your context and cannot invent, so it is for labor, not ideation

His technical examples ground the wiki's adaptor thesis in lived detail. "No matter how much context you give AI, it still lacks the context you have, because you are in the situation," illustrated by the racing project where Claude returned compute-heavy suggestions that ignored the on-ground reality of the track and car. And because it works from "the internet model," it "would try to propose an idea that is already available," so "if you're trying to do something that hasn't entirely been done, it will fail." His workaround is sharp: for novel problems, stop asking whether an idea exists and ask whether it could work from the mathematics or logic. This is the high-level-adaptor claim ([[genai-on-the-adaption-innovation-spectrum]]) with an engineer's escape hatch attached. The consequence for practice is his rule that AI is for laborious work (drafting, emails, diagrams, pulling references) and not for design thinking, where "you give inputs rather than take inputs." His bad-AI example, a teammate pawning the report's design section to AI and it returning em-dashes, fabricated points, and no grasp of the core idea, is the verification failure others named, with a tidy irony given this wiki's own ban on em-dashes.

### 8. The real tool he wants is a scoping mechanism for the fuzzy front-end

When asked what AI tool he would actually build, he does not name the questioner. He names a research-scoping mechanism: given a problem statement, bound how much domain research is "enough," so a team gets oriented fast without "getting riled up in the details" or missing the critical thing. He is precise about the failure it solves, that AI "expands the scope too much," and that iNPD itself "doesn't have any mechanism to scope our research." He has even tried to build a Claude skill file for it. This is important because it is the inverse of Interviewee 2, who wanted AI kept out of the early Identify and Understand work; Interviewee 3 wants AI's primary job to be helping bound that exact work. The two are not as opposed as they look: both distrust AI generating early content, but Interviewee 3 sees a non-generative role, calibrating how much to read, that Interviewee 2 did not consider. A bounded research-scoping aid for the [[inpd]] front-end is a candidate reconciliation, and a distinct addition to the design's current question-only repertoire.

## Cross-cutting tensions

- He wants maximum conflict and minimum mediation, yet his own best practices (step back, cool down, give supporting points, apologize after) are themselves a kind of self-mediation. He protects conflict in principle while regulating it carefully in practice.
- He rejects the Collaboration Agent for removing accountability, then designs a Collaboration feature (the agree/disagree map). His objection is specifically to substituting for the conversation, not to AI touching team dynamics at all, which narrows the design problem usefully.
- He distrusts AI verdicts and context, yet relies on AI to stress-test his solo ideas. The reconciliation is his framing: AI is a sparring partner that tries to make an idea fail, never a judge that says which idea wins.
- His values are strongly normative ("that's what I should be doing," "if my idea is bad, just tell me why"), which makes him a clear thinker about how teams ought to work and a possibly unrepresentative guide to how mixed-engagement teams actually behave.

## Salience

The points he returned to unprompted, and which therefore carry weight: conflict as necessary and mediation as harmful, ownership as the thing AI must not erode, no verdicts from AI, and scoping the fuzzy front-end. The first two are his moral core and drive the design objection; the last is his concrete feature ask.

## Design implications for the AI questioner

- Treat the ownership objection as a first-class design constraint. The Collaboration Agent should be positioned as a nudge toward a human, attributed conversation, not a substitute for it. The feedback loop's requirement that the team supply its own reasoning is necessary but, per this participant, not obviously sufficient; consider explicitly handing the conflict back to the people to resolve face-to-face rather than resolving it through a de-identified question.
- Add the agree/disagree synthesis as a Collaboration or Orchestrator output: a structured map of where members agree (and why) and disagree, to frame a human discussion. This is his contribution and it preserves accountability.
- Name audience simulation as an explicit purpose of the Socratic questioner: questions that rehearse what evaluators will ask, scoped to the project.
- Hold the no-verdicts line hard, and extend it: not even a recommendation, only pros and cons, and be wary that even question selection can imply a verdict.
- Consider a research-scoping mode for the iNPD front-end: a non-generative aid that bounds how much domain reading is enough, which both this participant and Interviewee 2's concern point toward from opposite sides.
- Keep AI out of ideation content and on laborious drafting, with a verification step, consistent with all three interviews.

## Tentative mapping to iNPD phases

Provisional, to refine; phases are defined in [[inpd]]. His scoping need sits squarely in Identify and Understand (bounding the fuzzy front-end research). His conflict-and-detail stuckness (proposable versus doable, the effort/time/convenience debate) sits in Conceptualize and the transition into Realize, where the team chooses what to propose. His ownership and mediation concerns cut across all phases, since they are about how the team works rather than what phase it is in, echoing the cross-phase findings of the first two interviews.

## Limitations and reflexivity

This is one self-reported account from a participant with a strong, coherent ideology about teamwork, interviewed by a former teammate who also pitched him the design under discussion, which raises both candor and courtesy effects. His engineering background sharpens his AI critiques and may not generalize to less technical users. His normative confidence ("this is what I should be doing") makes him an excellent source on how good teamwork ought to feel and a weaker guide to teams where members do not share his standards. Names, project codenames, and identifying details are removed; he is referred to only as Interviewee 3. None of the themes should be generalized until corroborated.

## Open questions for the next interviews

- Does the ownership objection recur, and is there evidence that AI-surfaced conflict actually lets people dodge accountability, or does it lower the barrier to a conversation that then happens for real?
- Is the agree/disagree synthesis preferred over a single question by other participants?
- Do people split into the conflict-protecting and the harmony-seeking camps (this participant versus the smoother dynamics of Interviewee 2's team), and what predicts which?
- Is research-scoping of the fuzzy front-end a widely felt need, and is a non-generative scoping aid the way to give AI an early-phase role people will accept?
- Does the no-verdicts, pros-and-cons-only requirement hold across less technical participants?
