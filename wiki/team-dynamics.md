---
title: "Team Dynamics: What Makes Teams Work"
type: concept
created: 2026-06-14
updated: 2026-06-14
tags: [team-dynamics, innovation-teams, psychological-safety, collective-intelligence, conflict]
sources: [edmondson-1999, woolley-2010, tuckman-1965, wegner-1986, lewis-2003, katzenbach-smith-1993, jehn-1995, dedreu-weingart-2003, salas-2005]
---

# Team Dynamics: What Makes Teams Work

This page collects the main research on how teams function: what makes them effective, how they share knowledge, how they handle conflict, and how they develop over time. It is here because the innovation-teams project ([[interviews-synthesis]]) studies stuck teams, and most of what the first interview surfaced ([[interviewee-1]]) has decades of research behind it. Each section names the established finding and, where it fits, the matching point from the interview.

## Psychological safety

Amy Edmondson defined team psychological safety as a shared belief that the team is safe for interpersonal risk-taking: people can ask questions, admit mistakes, and disagree without fear of punishment or humiliation ([Edmondson 1999](https://journals.sagepub.com/doi/10.2307/2666999)). In her hospital study, higher-performing teams reported more errors, not because they made more, but because they felt safe enough to surface them. Google's Project Aristotle later studied hundreds of its own teams and found psychological safety the strongest predictor of team effectiveness ([NYT, Duhigg 2016](https://www.nytimes.com/2016/02/28/magazine/what-google-learned-from-its-quest-to-build-the-perfect-team.html)).

This maps to the interview's point that peer-to-peer teams are harder than hierarchical ones, because in a flat team there is no boss with the standing to be blunt and have it accepted, so people hold back unless they feel safe.

## Shared purpose and mutual accountability

Katzenbach and Smith distinguish a real team from a working group by a small set of disciplines: a common purpose the members shape together, specific performance goals, complementary skills, and mutual accountability ([Katzenbach & Smith, "The Discipline of Teams," HBR 1993](https://hbr.org/1993/03/the-discipline-of-teams-2)). Without a shared goal, a group of capable people does not become a team.

This is the interview's strongest theme. The worst team had "no common goal to work toward, because everyone had different objectives," and the best teams shared one, sometimes an external one ("a common villain") such as winning over a difficult client or winning a hackathon. See [[interviewee-1]].

## Collective intelligence

Woolley and colleagues found that groups have a measurable collective intelligence, a "c factor," that predicts performance across many tasks and is only weakly related to the members' average or peak individual IQ ([Woolley et al. 2010, Science](https://www.science.org/doi/10.1126/science.1193147)). What predicted it instead was the members' average social sensitivity, more equal turn-taking in conversation, and the proportion of women in the group.

Equal turn-taking and reading each other well is the research version of the interview's "give and take" and "respect their contribution." When one person dominates or contributions are not respected, the team does not click.

## Transactive memory: who knows what

A transactive memory system is a team's shared map of who knows what, first described by Wegner as an alternative to vague notions of a "group mind" ([Wegner 1986](https://link.springer.com/chapter/10.1007/978-1-4612-4634-3_9)). Lewis showed it has three measurable parts: specialization (members hold different expertise), credibility (they trust each other's knowledge), and coordination (they can combine it smoothly) ([Lewis 2003, J. Applied Psychology](https://doi.org/10.1037/0021-9010.88.4.587)).

This is the research behind the interview's "truth document" and the pain of onboarding people who rotate in and out of projects. A good transactive memory system is exactly what the team was building by hand, and it is also why an AI grounded in that shared record was an appealing idea ([[interviewee-1]]; the mechanism is [[rag-explained]]).

## Conflict: task versus relationship

Jehn separated two kinds of intragroup conflict: task conflict (disagreement about the work) and relationship conflict (interpersonal friction), and argued that whether conflict helps or hurts depends on its type and the group's context ([Jehn 1995](http://www.iot.ntnu.no/innovation/norsi-pims-courses/huber/Jehn%20(1995).pdf)).

> [!conflict] Is task conflict actually good?
> The common belief, drawn partly from Jehn, is that task conflict is productive while relationship conflict is harmful. A large meta-analysis complicated this: De Dreu and Weingart found that both relationship and task conflict were negatively related to team performance and member satisfaction, so even disagreement about the work is not reliably beneficial ([De Dreu & Weingart 2003](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Negotiation_and_Conflict_Management/De_Dreu_Weingart_Task-conflict_Meta-analysis.pdf)). The takeaway is that conflict is not free, and managing it (psychological safety, shared goals) is what lets a team get the benefit without the cost.

The interview's resolution tactics fit this: find a halfway point, defer to whoever has the bigger stake, and tie arguments to a source or user quote so a disagreement becomes about evidence rather than personalities.

## How teams develop over time

Tuckman's classic model describes a sequence groups tend to move through: forming (orientation), storming (conflict over roles), norming (cohesion), and performing (getting work done), with adjourning added later for the end of a team's life ([Tuckman 1965](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Dynamics/Tuckman_1965_Developmental_sequence_in_small_groups.pdf)). It is a rough description rather than a strict law, but it names why "beginnings are a little bumpy," as the interview put it, before a team settles.

## What teamwork is made of

Salas and colleagues distilled the teamwork literature into a "Big Five": team leadership, mutual performance monitoring, backup behavior, adaptability, and team orientation. These work through three coordinating mechanisms: shared mental models, closed-loop communication, and mutual trust ([Salas, Sims & Burke 2005](https://journals.sagepub.com/doi/10.1177/1046496405277134)). Backup behavior and mutual monitoring are the formal version of the interview's account of teammates covering for each other and of taking up the facilitator role when no one else does.

## How this connects to the project

The first interview was a single source, but nearly every theme it raised lines up with an established finding: shared purpose (Katzenbach & Smith), safety to speak up in flat teams (Edmondson), give-and-take and turn-taking (Woolley), the truth document as a transactive memory system (Wegner, Lewis), evidence-based disagreement (Jehn; De Dreu & Weingart), and bumpy beginnings (Tuckman). That gives the project a vocabulary and a set of measures to test its own hypotheses against, and a way to ask whether a well-timed AI question can support these dynamics rather than replace them. See [[interviews-synthesis]] for the interview findings, [[genai-on-the-adaption-innovation-spectrum]] for where AI fits cognitively, and [[genai-as-socratic-facilitator]] for the specific design theory.

## Sources

- Edmondson, A. (1999). *Psychological Safety and Learning Behavior in Work Teams.* Administrative Science Quarterly, 44(2), 350-383. https://journals.sagepub.com/doi/10.2307/2666999
- Duhigg, C. (2016). *What Google Learned From Its Quest to Build the Perfect Team* (Project Aristotle). New York Times. https://www.nytimes.com/2016/02/28/magazine/what-google-learned-from-its-quest-to-build-the-perfect-team.html
- Woolley, A. W., Chabris, C. F., Pentland, A., Hashmi, N., & Malone, T. W. (2010). *Evidence for a Collective Intelligence Factor in the Performance of Human Groups.* Science, 330(6004), 686-688. https://www.science.org/doi/10.1126/science.1193147
- Wegner, D. M. (1986). *Transactive Memory: A Contemporary Analysis of the Group Mind.* In Theories of Group Behavior. Springer. https://link.springer.com/chapter/10.1007/978-1-4612-4634-3_9
- Lewis, K. (2003). *Measuring Transactive Memory Systems in the Field: Scale Development and Validation.* Journal of Applied Psychology, 88(4), 587-604. https://doi.org/10.1037/0021-9010.88.4.587
- Katzenbach, J. R., & Smith, D. K. (1993). *The Discipline of Teams.* Harvard Business Review. https://hbr.org/1993/03/the-discipline-of-teams-2
- Jehn, K. A. (1995). *A Multimethod Examination of the Benefits and Detriments of Intragroup Conflict.* Administrative Science Quarterly, 40(2), 256-282. http://www.iot.ntnu.no/innovation/norsi-pims-courses/huber/Jehn%20(1995).pdf
- De Dreu, C. K. W., & Weingart, L. R. (2003). *Task versus Relationship Conflict, Team Performance, and Team Member Satisfaction: A Meta-Analysis.* Journal of Applied Psychology, 88(4), 741-749. https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Negotiation_and_Conflict_Management/De_Dreu_Weingart_Task-conflict_Meta-analysis.pdf
- Tuckman, B. W. (1965). *Developmental Sequence in Small Groups.* Psychological Bulletin, 63(6), 384-399. https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Dynamics/Tuckman_1965_Developmental_sequence_in_small_groups.pdf
- Salas, E., Sims, D. E., & Burke, C. S. (2005). *Is There a "Big Five" in Teamwork?* Small Group Research, 36(5), 555-599. https://journals.sagepub.com/doi/10.1177/1046496405277134
