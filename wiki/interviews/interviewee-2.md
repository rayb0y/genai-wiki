---
title: "Interview: Interviewee 2"
type: interview
created: 2026-06-14
updated: 2026-06-14
tags: [interviews, innovation-teams, ai-in-teams, facilitation, knowledge-management, authority, feedback]
interviewee: Interviewee 2
---

# Interview: Interviewee 2

The record page for the second interview. The full speaker-labeled transcript is [[interviewee-2-transcript]], and the detailed qualitative analysis is [[interviewee-2-analysis]].

## Metadata

- Interviewee: Interviewee 2 (identity withheld; anonymized)
- Role and context: a designer (product design at a manufacturing company, then UX at a gaming company for about 18 months) now in a CMU master's program; spoke mainly about a CMU innovation capstone (referred to in the transcript as the IPD/capstone team) and a UX role; currently in a research-assistant position
- Date: interview date not recorded; filed 2026-06-14
- Interviewer: project lead (iNPD x AI innovation-teams study)
- Recording: anonymized raw transcript at `raw/interviews/interviewee-2.txt`
- Consent: [confirm and note]

## One-line summary

A designer's account of a capstone team that worked because everyone shared the same low expectations (a "shared disappointment" that aligned them), where stuckness came from process rigidity and destabilizing authority feedback, and a sharp read on AI in innovation work: keep it out of early problem-framing and research, use it later to refine and review, and note that feedback is received very differently depending on whether it comes from an authority (faculty) or a peer.

## Key takeaways

- The best team worked on aligned expectations, not shared enthusiasm. None of the members cared about the project, and naming that openly in the first meeting (a shared disappointment) is what synced them. Alignment of where everyone stood mattered more than excitement about the topic.
- Roles self-organized immediately. Members put themselves in "separate boxes" by taking initiative on their strengths (business, engineering, research and design), with no turf fights, and the expectation-setter and expectation-manager roles rotated as needed.
- A gratitude and affirmation culture held it together. Because no one was doing work they wanted, the team actively thanked and hyped each other, and peer evaluations were uniformly positive. This is psychological safety in practice (see [[team-dynamics]]).
- Stuckness came from process, not ambiguity. The team could not see a path forward and was forced to keep cycling through iNPD phases even though the phase-4 solution was essentially the phase-1 solution, which was demoralizing.
- Authority feedback destabilized more than it helped. Faculty approving something and then rejecting it the next day caused the worst stuck moment. Faculty feedback is read as "concrete," a set direction to comply with, whereas peer or non-authority feedback is read as "constructive" and engaged with more openly.
- AI should refine, not initiate. A hard no to AI in the early stages (understanding the problem, research, scoping), because it returns generic output misaligned with what the client or faculty wants. AI is useful later for ideation, analysis, review, and consolidating thoughts.
- Trust comes from authority validation. What would make Interviewee 2 trust an AI tool is that its suggestions are later approved by a faculty member or manager, positioning the tool as pre-review preparation that aligns with the authority, not a replacement for it.
- Lived AI failure modes: synthesis of multiple documents was surface-level with no nuance (so she did it by hand); it paraphrases text even when told to transcribe verbatim; and AI-forced design homogenized everything so "everything looked the same." Best uses were finding specific sources and reviewing a presentation's story structure, including triangulating across two tools (one teammate on one model, another on a different one).
- Where the real thinking happened: in-person, not on online calls. Sitting together let the team read faces and draw out quieter members; calls were only for deciding what to sort.
- Team memory was phase-structured docs (a shared doc, Figma, and WhatsApp), enough for the team but not for onboarding; a new joiner "would have a very difficult time." At her gaming job, by contrast, ordered handoff docs let a new person pick up almost immediately.

## Themes

- Aligned expectations over shared passion: a variant of Interviewee 1's "shared goal" finding, where even shared low investment worked because expectations were synced. See [[team-dynamics]] (shared purpose).
- Authority and feedback framing: the same content lands differently from a position of power versus a peer. Authority feedback compels compliance and can destabilize; peer or tool feedback invites consideration. This is the central new theme this interview adds.
- AI as refiner, not initiator, gated by phase: keep AI out of early Identify and Understand work, allow it in later Conceptualize and Realize work. Maps directly to [[inpd]] and to the phase-specific design in [[genai-as-socratic-facilitator]].
- Trust through authority validation: a second, different trust model from Interviewee 1's non-flattering, source-tied requirement. Here trust is anchored to an external authority confirming the direction.
- Process rigidity as a stuck-maker: being forced to revisit a settled decision because the phase structure demands it. A facilitation design question worth naming, see [[innovation-team-agent-architecture]].
- AI aggregates, does not add nuance: the hand-done synthesis story independently echoes the high-level-adaptor thesis ([[genai-on-the-adaption-innovation-spectrum]], [[what-genai-is-good-and-bad-at]]).
- Knowledge held in phase-structured docs, weak for onboarding: the transactive-memory and shared-state theme ([[team-dynamics]], [[getting-the-most-out-of-llms]]).
- Real thinking is in-person and social: reading faces to draw out introverts, which connects to equal turn-taking in [[team-dynamics]].

## Notable quotes

Verbatim text is in [[interviewee-2-transcript]].

- "None of us were interested in the project... so in the first few days we quickly realized where we all stand. That shared disappointment established that we were all on the same page."
- "We put ourselves into separate boxes almost immediately, because we each had established strengths, and nobody fought over it."
- "Every time someone pushed themselves to do a little bit more, we were all hyping each other up. Positive affirmation really helped."
- "At the end of phase 4 the solution we had was basically the same as phase 1, and it got frustrating to keep going back to the same thing over and over."
- "What threw us off was that something was approved and the feedback the next day was completely different."
- "It feels very concrete when it comes from faculty, and more constructive when it's from peers or any other platform assessing what I'm doing."
- "The work before that should still happen from us, it should be a more refining thing."
- "The initial stages of understanding what we actually want the problem to be, big no to AI, it gave us everything generic that wasn't working with what the faculty wanted."
- "If I made the changes and the faculty visibly approved the direction, I'd trust it more, because I'd know it's the right direction."
- "I told it do not change what's written, just transcribe, and it paraphrased everything from its own understanding."

## Connections to the wiki

This interview reinforces several existing claims and adds one new design tension. It echoes AI as an aggregator that lacks nuance ([[genai-on-the-adaption-innovation-spectrum]], [[what-genai-is-good-and-bad-at]]), the value of grounded retrieval over your own sources ([[rag-explained]], [[getting-the-most-out-of-llms]]), and team memory as a shared-state problem ([[team-dynamics]]). The new contribution is the authority-versus-peer feedback dynamic and the trust-through-validation model, which complicate the trust requirement found in [[interviewee-1]] and feed directly into the Socratic facilitator design ([[genai-as-socratic-facilitator]], [[innovation-team-agent-architecture]]). It feeds [[interviews-synthesis]].

## Open questions and follow-ups

- The two interviews give two different trust models: non-flattering and source-tied (Interviewee 1) versus authority-validated (Interviewee 2). A facilitation tool may need to serve both, for example by being a low-power constructive questioner during the work and a pre-review aligner before an authority checkpoint. Probe this directly.
- Interviewee 2 wants AI out of early Identify and Understand work but the architecture proposes phase-based questions in every phase. Reconcile: the question type, not the presence of questions, may be what differs by phase. Worth a design note in [[innovation-team-agent-architecture]].
- Process rigidity (being forced to revisit a settled decision) as a distinct stuck-maker. Is there a facilitation move for "the process is asking us to reopen a closed decision"?
- Confirm the interview date and consent for use.
- Still only two interviews; treat cross-interview themes as hypotheses, not patterns.

## Transcript and analysis

- Full transcript: [[interviewee-2-transcript]] (cleaned, speaker-labeled). Raw anonymized text: `raw/interviews/interviewee-2.txt`.
- Detailed analysis: [[interviewee-2-analysis]].
