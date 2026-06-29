---
title: "Innovation process methods (front-end toolkit)"
type: concept
created: 2026-06-14
updated: 2026-06-14
tags: [inpd, methods, pestle, design-research, experience-mapping, service-blueprint, pretotyping, double-diamond, capstone]
sources: []
---

# Innovation process methods (front-end toolkit)

The methods the CMU III IPD Capstone and the [[inpd]] process lean on, especially in the fuzzy front end. This is a working catalog that will keep growing as more resources come in and the faculty interviews happen; for now it covers environmental scanning (PESTLE), design research, experience mapping, service blueprints, pretotyping, and the Double Diamond. Each entry is a short, sourced summary, not a full how-to.

## How the methods map to the phases

Roughly, against the four [[inpd]] phases: PESTLE, design research, and experience mapping sit in Identify and Understand (finding and framing the opportunity); service blueprinting sits in Understand and Conceptualize (designing the service behind the product); pretotyping sits in Conceptualize and Realize (cheaply testing whether the right thing is worth building); and the Double Diamond frames the whole arc. The capstone names PESTLE its Phase 1 main method (IPD Capstone Phase 1 deck, CMU III, 2026).

## PESTLE: environmental scanning

PESTLE is a framework for reading the external forces acting on an organization or opportunity, used in strategic planning. The six factors are Political, Economic, Social, Technological, Legal, and Environmental, all outside the team's control ([CIPD PESTLE factsheet](https://www.cipd.co.uk/knowledge/strategy/organisational-development/pestle-analysis-factsheet/); [PESTLEanalysis.com](https://pestleanalysis.com/what-is-pestle-analysis/)). It began as PEST (Political, Economic, Social, Technological), attributed to Francis Aguilar, and grew the Legal and Environmental lenses; PESTEL is the same thing with the letters reordered, and STEEPLE and STEEPLED add Ethics and Demographics. It is usually paired with SWOT, which adds the internal view PESTLE lacks.

The connection to iNPD is direct: classic iNPD's SET factors (Social, Economic, Technology) are a subset of PESTLE, which is why the capstone treats SET as the minimum to cover and PESTLE as the fuller scan (see [[inpd]]). The honest limits, from the same sources, are that PESTLE can sprawl (it is data-hungry and goes stale), so the guidance is to keep it short, list only factors that actually affect the project, lead with the most impactful, and drive toward actionable implications rather than a long list.

## Design research: ask the right question first

Erika Hall's two essays are the program's framing for research in the front end, and both argue the same thing: the value is in the question, not the method or the pile of data.

In "Dig in the Right Spot," a research question is what you need to know to make a better decision, and it is not the same as an interview question; a good research question is specific, actionable, and practical, goals come before questions, and the highest-priority question is the unknown that carries the most risk (your customers do not value it, it will not create business value, it creates larger problems, you cannot build it, someone already does it better). Questions come before methods, because there is no single best method, only the one that fits the question ([Hall, Dig in the Right Spot](https://medium.com/mule-design/dig-in-the-right-spot-6dc7af5a75e8)).

Her "9 Rules of Design Research" expand this: get comfortable being uncomfortable (a good question beats a right answer); ask first, prototype later; know your goal in advance, and not "to be proven right"; agree on the big questions (research questions are not interview questions); there is always enough time and money; do not expect data to change minds; embrace messy imperfection; commit to collaboration so the decision-makers are the best-informed; and find your bias buddies, checking each other's biases in a team with psychological safety and mutual respect ([Hall, 9 Rules of Design Research](https://medium.com/mule-design/the-9-rules-of-design-research-1a273fdd1d3b); expanded in her book *Just Enough Research*).

This matters to the project twice over. "Research questions are not interview questions" is a direct caution for the [[faculty-interview-protocol]]. And the emphasis on framing the riskiest question first is the same scoping need Interviewee 3 named as the AI tool he would actually build ([[interviewee-3-analysis]]).

## Experience mapping

An experience map is a strategic artifact that captures the holistic customer experience across touchpoints and channels, built around a customer journey model, an archetypal journey from A to B as a person tries to meet a need, annotated with the highs and lows they feel along the way (Adaptive Path's Guide to Experience Mapping, 2013). The point is that experiences break down where they span channels, and organizations own touchpoints but not the journeys that cut across them, so the map builds a shared frame of reference and surfaces the moments that, once improved, unlock more value. The activity of mapping, done collaboratively, builds consensus across the team as much as the artifact informs design. The guide is by Brandon Schauer's Adaptive Path (the capstone draws on Adaptive Path's materials).

## Service blueprint

A service blueprint visualizes the organizational processes behind a service, showing what the customer sees and what happens behind the scenes to support it. It is read in horizontal layers separated by lines: physical evidence and the customer (or attendee) actions above the line of interaction; frontstage actions the customer sees; the line of visibility; backstage actions the customer does not see; the line of internal interaction; and the support processes underneath ([NN/g, Service Blueprints](https://www.nngroup.com/articles/service-blueprints-definition/); Adaptive Path / Brandon Schauer service blueprint example). Where an experience map takes the customer's point of view, a service blueprint takes the organization's and exposes the operational machinery, which makes it the tool for designing the delivery of a service, not just its front. Two worked examples informed this entry: the Adaptive Path "Seeing Tomorrow's Services Panel" blueprint (Brandon Schauer, CC BY-SA) and the NN/g definition diagram.

## Pretotyping

Pretotyping, coined by Alberto Savoia, is about making sure you are building the right "it" before you build "it" right. A pretotype tests demand and use, not feasibility: where a prototype answers "can we build it, will it work," a pretotype answers "would I use it, would people buy it, and would they use it more than once." The canonical story is Jeff Hawkins carrying a wooden block sized for his shirt pocket and pretending it was a Palm Pilot for weeks before committing to build one, to find out whether he would actually use it. Pretending is the core move, and it is far cheaper and faster than prototyping ([Savoia, My Favorite Pretotype Story, 2010](https://pretotyping.blogspot.com/2010/08/one-of-my-favorite-pretotype-stories.html)). For an innovation team it is the discipline of validating the right thing with almost no investment, which guards against the failure mode Interviewee 1 described as building on a shaky foundation and the front-end "ask first" rule above.

## Value and business methods (Phases 2 to 4)

The later phases add a set of analysis and business tools, used in the capstone and catalogued here briefly.

Value Opportunity Analysis (VOA) and the Lean VOA canvas. iNPD names seven categories in which a product can add value (emotion, aesthetics, identity, ergonomics, impact, core technology, quality); the VOA scores an offering against them, and the program's Lean VOA canvas captures the values and needs of key users and compares them to the current state ([Cagan & Vogel 2002](https://books.google.com/books/about/Creating_Breakthrough_Products.html?id=hlSRf61_nnkC)). The faculty's recurring note is to write values as the emotion or value behind a criterion, not as a design requirement (see [[capstone-process]]).

Early product criteria. A short, prioritized set of need-to-haves derived from the value work, deliberately stated as benefits and outcomes rather than features, so the team does not bias itself toward a solution before conceptualizing.

Experience blueprints. A team variant of the service blueprint and journey, used to map the process, ecosystem, and stakeholder relationships around the offering and make shared understanding tangible.

Prototyping and the Build-A-Thon. Hands-on making of 2D and 3D prototypes to think ideas through and surface new ones, paired with the cheaper-first discipline of [pretotyping](#pretotyping), and a validation plan that lines up the people who will give feedback before there are concepts to test.

Market sizing with TAM, SAM, SOM. A nested estimate of the Total Available, Serviceable Available, and Serviceable Obtainable Market, built from a beachhead segment outward to frame a go-to-market strategy.

Lean Business Model Canvas. A one-page model of the business (customer segment, problem, unique value proposition, solution, channels, revenue, cost, key metrics, unfair advantage), Ash Maurya's lean adaptation of Osterwalder's Business Model Canvas, used to design how the offering delivers and captures value, not just creates it.

Archetypes. Behavior-based user models (extended in Phase 4 with demographics and psychographics) that shift the team from describing content or features to describing the people, which the capstone feedback repeatedly rewards.

## The Double Diamond

The Double Diamond, the Design Council's model the capstone uses to frame the front end, is two diamonds of divergence then convergence: Discover and Define (explore the problem widely, then frame it), followed by Develop and Deliver (explore solutions widely, then narrow to one). The capstone presents it less as a recipe than as a stance, quoting IDEO that it is "an invitation to get involved" rather than an instruction manual, and pairs it with writing a sharp design problem statement at the first convergence (IPD Capstone Phase 1 deck, CMU III, 2026). It maps cleanly onto iNPD: Discover and Define are Identify and Understand, Develop and Deliver are Conceptualize and Realize.

## Sources

- IPD Capstone course materials, 2026 (L1 welcome and structure; L2 Phase 1, Identifying opportunities in context). Integrated Innovation Institute, Carnegie Mellon University. (Course decks; raw uploads.)
- PESTLE analysis factsheet. CIPD. https://www.cipd.co.uk/knowledge/strategy/organisational-development/pestle-analysis-factsheet/
- Makos, J. What is PESTLE Analysis? PESTLEanalysis.com. https://pestleanalysis.com/what-is-pestle-analysis/
- PESTLE macro-environmental analysis. Oxford Learning Lab. https://www.oxfordlearninglab.com/p/pestle-macro-environmental-analysis
- Hall, E. (2018). Dig in the Right Spot. Mule Design. https://medium.com/mule-design/dig-in-the-right-spot-6dc7af5a75e8
- Hall, E. (2018). The 9 Rules of Design Research. Mule Design. https://medium.com/mule-design/the-9-rules-of-design-research-1a273fdd1d3b
- Schauer, B., et al. (2013). Adaptive Path's Guide to Experience Mapping. Adaptive Path. (CC BY-NC.)
- Nielsen Norman Group. Service Blueprints: Definition. https://www.nngroup.com/articles/service-blueprints-definition/
- Schauer, B. Service Blueprint for "Seeing Tomorrow's Services Panel." Adaptive Path. (CC BY-SA.)
- Savoia, A. (2010). My Favorite Pretotype Story. Pretotyping. https://pretotyping.blogspot.com/2010/08/one-of-my-favorite-pretotype-stories.html
- Design Council. The Double Diamond (framework referenced by the IPD Capstone).
