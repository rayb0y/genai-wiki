---
title: "TRIZ: The Theory of Inventive Problem Solving"
type: concept
created: 2026-06-14
updated: 2026-06-14
tags: [triz, innovation, problem-solving, contradiction, design-theory]
sources: [altshuller-1984]
---

# TRIZ: The Theory of Inventive Problem Solving

TRIZ (a Russian acronym for the Theory of Inventive Problem Solving) is a method for solving hard design problems, developed by Genrich Altshuller from a systematic study of hundreds of thousands of patents. Its central claim is that invention is not random: the same structural problems and the same solution patterns recur across unrelated fields, so they can be catalogued and reused ([Altshuller 1984, *Creativity as an Exact Science*](https://books.google.com/books/about/Creativity_as_an_Exact_Science.html?id=8BBRAAAAMAAJ)). It is referenced here because the project treats one TRIZ idea, contradiction detection, as a mode for an AI questioner ([[genai-as-socratic-facilitator]]).

## Contradiction is the core of invention

Altshuller's key observation is that real inventions resolve a contradiction rather than trade one thing off against another. A technical contradiction exists when improving one property of a system degrades another (make the wing stronger and it gets heavier). A physical contradiction exists when one property must take two opposite values (the coffee should be hot to drink and cold to hold). Routine engineering accepts the trade-off; inventive solutions dissolve it so both sides win.

## The main tools

- 39 engineering parameters: a standard vocabulary for the properties that come into conflict (weight, speed, strength, energy use, and so on).
- 40 inventive principles: recurring solution patterns abstracted from the patent record (segmentation, "nested doll," "the other way round," and others).
- The contradiction matrix: a lookup table that maps a conflict between two of the 39 parameters to the inventive principles that have historically resolved that type of contradiction.
- Ideality and ARIZ: the broader idea that systems evolve toward an "ideal final result" (all benefit, no cost), and ARIZ, a step-by-step algorithm for working through tough problems.

The practical loop is: state the contradiction, classify it against the 39 parameters, look up the matched principles in the matrix, and translate each principle into a concrete idea for your problem.

## Strengths and limits

TRIZ is valuable because it is a structured, teachable way to get unstuck that pushes past the first obvious trade-off, and the contradiction frame is a sharp diagnostic. Its limits are also real: it was built from engineering patents, so it fits technical and product problems better than social or service ones; the matrix can feel mechanical; and applying it well still depends on framing the contradiction correctly, which is a skill. As a research method it is more practitioner heuristic than validated theory.

## Why it matters for this project

Contradiction detection is computable in a way that general facilitation is not. If a team's logged decisions contain a structural contradiction, a system can classify it, retrieve the relevant principles, and turn each into a question for the team. Because the output is a question rather than a proposed solution, a misclassified contradiction is low-risk: a question that does not land is simply dropped. That is the TRIZ mode of the Socratic questioner described in [[genai-as-socratic-facilitator]], and it sits alongside iNPD phase questions as a second source of questions over the same shared record.

## Sources

- Altshuller, G. S. (1984). *Creativity as an Exact Science: The Theory of the Solution of Inventive Problems.* Gordon & Breach. https://books.google.com/books/about/Creativity_as_an_Exact_Science.html?id=8BBRAAAAMAAJ
