---
title: "Interviews: Synthesis"
type: synthesis
created: 2026-06-14
updated: 2026-06-14
tags: [interviews, synthesis]
---

# Interviews: Synthesis

The rolling synthesis of every interview in this section. Each interview is filed once on its own page, built from [[interview-template]]. This page accumulates the themes that show up across them, so you do not have to re-read transcripts to remember what was found. It is updated whenever a new interview is ingested.

## Interviews

- [[interviewee-1]] (about 72 min): a design and innovation professional on what makes teams click or stall, where her real thinking happens (out loud, with a sounding board), and where AI helps or hurts in innovation work.
- [[interviewee-2]]: a designer on a CMU innovation capstone, on a team that worked through aligned (low) expectations, stuckness caused by process rigidity and destabilizing authority feedback, and AI as a refiner to keep out of early problem-framing.
- [[interviewee-3]]: an engineer-minded student on conflict and ownership as the engine of teamwork, who rejects the Collaboration Agent as a threat to team spirit, wants AI to never give verdicts, and names a research-scoping mechanism for the fuzzy front-end as the tool he would actually build.

## Themes across interviews

Drawn from three interviews. Still hypotheses to confirm or revise as more are added, not established patterns. Where they converge is noted as such; where they diverge is at least as useful.

All three converge on:

- Teams work on shared alignment, not skill. Interviewee 1 named a unifying goal (sometimes an external "common villain"); Interviewee 2 named aligned expectations, where even a shared lack of interest synced the team once it was said out loud; Interviewee 3 named knowing where everyone stands as the precondition for contributing at all. The common factor is everyone knowing the others' position.
- Real thinking is social and verbal, through opposition. Interviewee 1 does her best thinking out loud with a sounding board; Interviewee 2 located all real thinking in in-person meetings; Interviewee 3 makes the mechanism explicit, that an opposing view is the stress-test an idea cannot get on its own. Conflict, for him, is the engine, not a failure.
- AI aggregates and lacks your context, so it does not invent. Interviewee 1's Spotify-Wrapped test, Interviewee 2's hand-redone surface-level synthesis, and Interviewee 3's "it proposes what is already on the internet" are the same observation from three angles. See [[genai-on-the-adaption-innovation-spectrum]] and [[what-genai-is-good-and-bad-at]].
- AI is trusted for grounded and laborious work (finding sources, drafting, formatting) and distrusted for the generative core. All three keep AI away from the part that has to be theirs, and all three name sycophancy as a problem; Interviewee 3 has built a brutal-critique prompt to fight it.

They diverge on what makes an AI tool trustworthy, now a three-way split that is the most useful tension in the set:

- Interviewee 1: epistemic integrity. Transparency and traceability, correct version and context handling, no hallucination, no flattery. The fear is a tool that praises.
- Interviewee 2: authority validation. The tool is trusted when a faculty member or manager later approves the direction it suggested; it earns trust as pre-review preparation aligned with the authority.
- Interviewee 3: no verdicts plus scoping competence. The tool is trusted when it hands over plain pros and cons and never recommends ("even if it's the wrong choice, I'd know why I made it"), and when it can demonstrably scope a domain to "enough." His trust is about the tool not deciding and proving it can bound the work.

New from Interviewee 3:

- Conflict-as-engine and anti-mediation. The most pro-conflict participant: respectful argument is necessary, and a peace-making mediator who says "let it go" is the threat, not the conflict. Any facilitation move that reduces friction risks being read as sabotage.
- Ownership is the point of a team, and it grounds a direct objection to the design. Routing a complaint through the Collaboration Agent "takes the team spirit away" and lets you "run away from the accountability" of the face-to-face conversation where ownership is forged. The confidentiality feature that Interviewee-1-style trust would praise is exactly what he distrusts, because privacy lets people dodge the accountable conversation. This is the sharpest challenge to [[innovation-team-agent-architecture]] in the set.
- A constructive refinement: rather than fire one question, the system should report the commonalities and the differences across members (what the team agrees on and why, and what it disagrees on), to frame a human discussion instead of substituting for it. This preserves accountability and is a candidate Collaboration or Orchestrator output.
- Audience simulation: a scoped questioner is welcome partly because it rehearses the questions the real audience will ask.
- Scoping the fuzzy front-end is the tool he would build: a non-generative aid that bounds how much domain research is "enough." This is the inverse of Interviewee 2's "keep AI out of early framing," and the two reconcile if AI's early-phase role is calibrating how much to read rather than generating content.

## Open questions

- Does a well-timed question actually unblock teams, and can AI deliver it, or only a human? (The core hypothesis.)
- Can one tool hold three trust models at once (non-flattering integrity, authority validation, and no-verdicts plus scoping), or are these different users?
- Is the ownership objection real: does AI-surfaced conflict let people dodge accountability, or lower the barrier to a conversation that then happens for real? Test whether "the team answers with its own reasoning" is enough.
- Should the Collaboration or Orchestrator layer output an agree/disagree map, not just a single question?
- Is a research-scoping aid the way to give AI an accepted early-phase role, reconciling Interviewee 2 (keep AI out) and Interviewee 3 (scope the front-end)?
- Should question type, not question presence, vary by phase? See [[innovation-team-agent-architecture]].
- Run more interviews before treating any theme above as a pattern.

The themes above connect to established research in [[team-dynamics]] (psychological safety, shared purpose, collective intelligence, transactive memory, conflict types). For a synthesis of how GenAI can act on these dynamics as a Socratic questioner in innovation work, see [[genai-as-socratic-facilitator]].

## Protocols

- [[faculty-interview-protocol]] (full, 50 to 60 min) and [[faculty-interview-protocol-short]] (25-min core): the guide for the next population, III capstone faculty. Faculty see many teams rather than one, are the authority behind the binding-feedback dynamic, and own the individual-contribution assessment problem, so their interviews should be compared against the student view rather than pooled with it.

## How to add one

Give me a transcript: paste it in, or drop the text into `raw/interviews/`. I will clean it, label the speakers, fill in a copy of [[interview-template]], add it to the list above, update the themes, and append a line to `log.md`. Interviewees are anonymized by default unless you tell me otherwise.
