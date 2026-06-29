---
title: "iNPD: Integrated New Product Development"
type: concept
created: 2026-06-14
updated: 2026-06-14
tags: [inpd, innovation, design-process, product-development, cagan-vogel, capstone, pestle, methods]
sources: [cagan-vogel-2002]
---

# iNPD: Integrated New Product Development

iNPD (integrated New Product Development) is a user-centered process for creating products, developed by Jonathan Cagan and Craig Vogel at Carnegie Mellon and set out in their book *Creating Breakthrough Products* ([Cagan & Vogel 2002](https://books.google.com/books/about/Creating_Breakthrough_Products.html?id=hlSRf61_nnkC)). It integrates design, engineering, marketing, and user research, and it organizes the work into four phases. It is the structured process the innovation-teams project studies, specifically as taught in the CMU Integrated Innovation Institute (III) IPD Capstone, and the AI questioner is designed to be aware of which phase a team is in ([[genai-as-socratic-facilitator]]). The front-end and design methods the program uses are collected in [[innovation-process-methods]].

## The four phases

1. Identify. Spot a product opportunity. Scan trends and unmet needs to find a gap worth pursuing, before committing to any solution.
2. Understand. Investigate the opportunity. Study users, stakeholders, and context to learn what the opportunity really is and what would make a solution valuable.
3. Conceptualize. Turn the understood opportunity into candidate concepts: functional, usable product or service ideas that deliver the value identified.
4. Realize. Develop the chosen concept into a producible product, resolving the engineering, business, and detail decisions needed to ship it.

The phases are a sequence with feedback, not a strict one-way gate. Teams loop back as they learn.

## The front-end tools

Two tools structure the early, fuzzy phases:

- Environmental scanning and Product Opportunity Gaps. Opportunities are found by reading shifts in the external environment. Classic iNPD scans SET factors, Social trends, Economic forces, and Technology advances, which combine to create a Product Opportunity Gap where current products do not yet serve an emerging need ([Cagan & Vogel 2002](https://books.google.com/books/about/Creating_Breakthrough_Products.html?id=hlSRf61_nnkC)). The CMU III capstone widens this scan to PESTLE, Political, Economic, Social, Technological, Legal, Environmental, naming PESTLE the Phase 1 main method and treating SET as the minimum to cover (IPD Capstone Phase 1 deck, CMU III, 2026; [PESTLE analysis, CIPD](https://www.cipd.co.uk/knowledge/strategy/organisational-development/pestle-analysis-factsheet/)). PESTLE adds the Political, Legal, and Environmental lenses on top of SET. The fuller treatment is in [[innovation-process-methods]].
- Value Opportunities. iNPD names seven categories in which a product can add value: emotion, aesthetics, identity, ergonomics, impact, core technology, and quality. They give a team a shared vocabulary for what "better" means, beyond features and price.

## The capstone in practice (CMU III)

The process the project studies is the IPD Capstone at Carnegie Mellon's Integrated Innovation Institute, a semester-long sponsored team project run by the institute's teaching team. Teams work a real sponsor brief across the four phases, with bi-weekly sponsor meetings, a named point of contact, and a per-team materials budget (IPD Capstone L1 and L2 decks, CMU III, 2026). The full phase-by-phase process as it is actually run, including the recurring patterns in the teaching team's feedback, is in [[capstone-process]].

Phase 1, Identifying opportunities in context, makes the front end concrete. A team identifies its stakeholders and their goals in context, scans the world today with PESTLE (SET at a minimum), sets priorities, runs expert interviews, consolidates what it knows and needs to find out, and records early product criteria to set aside. The gate test the faculty pose is whether the opportunity is clearly supported by the insights, can be presented meaningfully, and, above all, whether the team knows the why behind it. The program frames the front end with the Double Diamond and pushes teams to write a sharp design problem statement before converging.

Two threads connect this to the project's design. The faculty themselves encourage an AI research aid (NotebookLM) for the Phase 1 information scan, with an explicit source-validation step and the caveat that AI output still needs design and storytelling, which is the same scoping-and-verification tension the interviews raised ([[interviewee-3-analysis]], [[what-genai-is-good-and-bad-at]]). And the recurring gate question, does the team know the why, is exactly what the architecture's decision-rationale logging is built to capture ([[innovation-team-agent-architecture]]).

## Where teams typically get stuck, by phase

These are common failure modes per phase, useful as a map of where a facilitator's question can help (developed in [[genai-as-socratic-facilitator]]):

- Identify. Premature convergence: the team latches onto a solution before finishing the opportunity scan, narrowing the horizon too early.
- Understand. Unexamined interpretation: observations get turned into conclusions without stress-testing what they actually mean.
- Conceptualize. Option overload: the team has many concepts and no shared criteria to choose among them, so it needs evaluation, not more ideas.
- Realize. Scope creep and late redesign: decisions reopen too late, and the team needs to prioritize rather than expand.

## Why it matters for this project

A facilitator who knows the current phase can ask the question that fits what should be happening and flags what the team is skipping. That phase-awareness is one of the two question sources in the project's design, the other being TRIZ-style contradiction detection ([[triz]]); both are developed in [[genai-as-socratic-facilitator]]. The interview evidence that teams stall on purpose and trust more than on any single phase task is in [[interviewee-1-analysis]] and [[team-dynamics]].

## Sources

- Cagan, J., & Vogel, C. M. (2002). *Creating Breakthrough Products: Innovation from Product Planning to Program Approval.* (2nd ed. 2013.) https://books.google.com/books/about/Creating_Breakthrough_Products.html?id=hlSRf61_nnkC
- IPD Capstone course materials, 2026: L1 (welcome and structure) and L2 (Phase 1, Identifying opportunities in context). Integrated Innovation Institute, Carnegie Mellon University. (Course decks; raw uploads.)
- PESTLE analysis factsheet. CIPD. https://www.cipd.co.uk/knowledge/strategy/organisational-development/pestle-analysis-factsheet/
- What is PESTLE Analysis? PESTLEanalysis.com. https://pestleanalysis.com/what-is-pestle-analysis/
