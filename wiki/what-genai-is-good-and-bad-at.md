---
title: "What GenAI Is Good At, and What It Isn't"
type: comparison
created: 2026-06-04
updated: 2026-06-08
tags: [genai, capabilities, limitations, strengths, weaknesses]
sources: [brown-2020, kambhampati-2024, ji-2023, schaeffer-2023, martinez-2024, silver-2016]
---

# What GenAI Is Good At, and What It Isn't

GenAI is superhuman in breadth and speed and below human level in reliability and grounded reasoning. It wins where the task is to produce something plausible, fast, across any domain, and it trails a competent person where the task is to be reliably right, plan over many steps, or justify an answer. Benchmark numbers go stale and are often gamed, so treat specific figures as snapshots. Why these strengths and weaknesses follow from the mechanism is covered in [[how-genai-works]].

## What it's good at

It is strongest at breadth and speed. No person has read as much or can produce a competent first draft in seconds across as many domains, and that advantage comes straight from large-scale pretraining.

It is reliable at language production and transformation: drafting, summarizing, translating, rephrasing, format conversion, and boilerplate code, where fluent and plausible is close to correct.

It adapts to a new task on the fly. In-context learning lets it pick up a task from a few examples in the prompt, with no retraining ([Brown et al. 2020](https://arxiv.org/abs/2005.14165)).

It handles well-structured knowledge tasks. It scores above passing thresholds on text-based professional exams such as the bar and the USMLE, which is real competence on structured question answering ([Katz et al. 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10894685/); [Nori et al. 2023](https://arxiv.org/abs/2303.13375)). See the caveat under novel problems below.

It is good for ideation and breadth-first exploration: brainstorming, outlining, surfacing options, and explaining a concept at a chosen level, where variety and coverage matter more than guaranteed correctness.

It works well as a front-end to tools, turning a request into the right tool call (search, code, a database) and weaving the results into prose. Used this way it is an orchestrator, not the source of truth ([[how-genai-works]] §Interaction).

The common thread is that it is a breadth-and-fluency engine. It is at its best when a fast, broad, plausible draft that a person or tool will check is what you actually want.

## What it's bad at

Reliable factual accuracy is the main weakness. It fabricates fluently and with confidence, and that confidence does not track correctness ([Ji et al. 2023](https://arxiv.org/abs/2202.03629)). Anything load-bearing, such as facts, figures, citations, law, or medicine, needs verification.

It cannot reliably plan over many steps or check its own work. Self-critique often makes results worse, and sound output needs an external verifier rather than the model judging itself ([Kambhampati 2024](https://arxiv.org/abs/2403.04121)).

It cannot guarantee correctness on exact, formal tasks. Arithmetic, formal logic, and constraint satisfaction, anything with a checkable right answer, are better handed to a calculator, solver, or code than to the model's own generation.

It struggles with problems that are new rather than variations on what it has seen. Performance drops outside the training distribution and is sensitive to wording, and strong benchmark scores can reflect test questions seen in training rather than transferable skill. Even celebrated results get walked back: the widely repeated "90th-percentile bar exam" figure is closer to the 48th percentile against real test-takers ([Martínez 2024](https://link.springer.com/article/10.1007/s10506-024-09396-9)).

It is inconsistent. Sampling is stochastic, so the same prompt can give different answers and small rewordings can change the output, which is a problem for anything that needs to be repeatable.

It has no accountability or grounding. There are no stakes, no persistent memory by default, and no grounding in the physical or social world beyond text. It handles linguistic form well, but whether it understands is contested and should not be assumed in practice.

The common thread here is that it is a weak correctness-and-reasoning engine. It is at its worst where you need guaranteed accuracy, multi-step plans, repeatability, or someone accountable.

## When to use something else

If a task is mostly about being reliably right rather than producing a plausible draft, a non-generative method is often better, cheaper, and easier to audit. Gradient-boosted trees fit tabular prediction (fraud, credit, churn), solvers and planners fit scheduling and optimization, ranking models fit search and recommendation, and reinforcement-learning agents with search fit crisp-objective domains. The AI systems that are clearly superhuman, such as AlphaGo and AlphaFold, are not generative ([Silver et al. 2016](https://www.nature.com/articles/nature16961)). The strongest setups tend to be hybrids: let GenAI draft, explore, and orchestrate, and let a tool, a verifier, or a person be the source of truth.

## Using it well

Use GenAI for open-ended generation that a person or tool will check, and not as an unverified authority. Its output is a draft, not a fact. It is useful when kept human-in-the-loop or tool-grounded, and a liability when left to stand alone on anything that has to be correct.

In Kirton's terms the whole split reduces to one idea: GenAI is a high-level adaptor, good at doing things better within a frame and weak at doing things differently by changing the frame. See [[genai-on-the-adaption-innovation-spectrum]].

## Sources

- Brown, T. et al. (2020). *Language Models are Few-Shot Learners.* https://arxiv.org/abs/2005.14165
- Katz, D. et al. (2024). *GPT-4 passes the bar exam.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10894685/
- Nori, H. et al. (2023). *Capabilities of GPT-4 on Medical Challenge Problems.* https://arxiv.org/abs/2303.13375
- Ji, Z. et al. (2023). *Survey of Hallucination in Natural Language Generation.* https://arxiv.org/abs/2202.03629
- Kambhampati, S. (2024). *Can large language models reason and plan?* https://arxiv.org/abs/2403.04121
- Martínez, E. (2024). *Re-evaluating GPT-4's Bar Exam Performance.* https://link.springer.com/article/10.1007/s10506-024-09396-9
- Schaeffer, R. et al. (2023). *Are Emergent Abilities of LLMs a Mirage?* https://arxiv.org/abs/2304.15004
- Silver, D. et al. (2016). *Mastering the Game of Go.* Nature. https://www.nature.com/articles/nature16961
