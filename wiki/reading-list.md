---
title: "Reading List: The Key Papers"
type: concept
created: 2026-06-04
updated: 2026-06-08
tags: [genai, papers, reading-list]
sources: []
---

# Reading List

The papers worth reading, grouped by what they tell you, each with a link and a one-line note. Cross-referenced from [[how-genai-works]] and [[what-genai-is-good-and-bad-at]].

## How it works

- Vaswani et al. (2017), *Attention Is All You Need*, https://arxiv.org/abs/1706.03762. The transformer, the architecture everything else sits on.
- Mikolov et al. (2013), *word2vec*, https://arxiv.org/abs/1301.3781. Meaning as vector geometry, the basis of embeddings (storage) and retrieval.
- Brown et al. (2020), *GPT-3 / Few-Shot Learners*, https://arxiv.org/abs/2005.14165. In-context learning, and why prompting works.
- Lewis et al. (2020), *Retrieval-Augmented Generation*, https://arxiv.org/abs/2005.11401. Combine frozen weights with a searchable external index to ground outputs in real facts.
- Ho et al. (2020), *Denoising Diffusion Probabilistic Models*, https://arxiv.org/abs/2006.11239. How image generation works, by denoising from noise.

## How it's trained, and the frontier

- Ouyang et al. (2022), *InstructGPT / RLHF*, https://arxiv.org/abs/2203.02155. How a raw predictor becomes a helpful assistant; a 1.3B aligned model was preferred over 175B GPT-3.
- Kaplan et al. (2020), *Scaling Laws*, https://arxiv.org/abs/2001.08361. Performance improves predictably with scale, later corrected by Chinchilla ([Hoffmann 2022](https://arxiv.org/abs/2203.15556)).
- DeepSeek-AI (2025), *DeepSeek-R1*, https://arxiv.org/abs/2501.12948. Reasoning via RL on chain-of-thought, the post-2023 shift the next-word story misses.

## Strengths, limits, and the skeptical view

- Kambhampati (2024), *Can LLMs Reason and Plan?*, https://arxiv.org/abs/2403.04121. The evidence that LLMs cannot reliably plan or self-verify and need external verifiers.
- Ji et al. (2023), *Survey of Hallucination*, https://arxiv.org/abs/2202.03629. Why models fabricate, and what reduces it.
- Schaeffer et al. (2023), *Are Emergent Abilities a Mirage?*, https://arxiv.org/abs/2304.15004. Apparent sudden abilities are largely an artifact of the metric.
- Bender et al. (2021), *Stochastic Parrots*, https://dl.acm.org/doi/10.1145/3442188.3445922. The form-without-meaning critique, plus bias, cost, and misinformation.

## AI that is not generative

- Sutton (2019), *The Bitter Lesson*, http://www.incompleteideas.net/IncIdeas/BitterLesson.html. One page: general compute-leveraging methods tend to beat hand-coded knowledge.
- Silver et al. (2016), *AlphaGo*, https://www.nature.com/articles/nature16961. Superhuman performance from RL and search, not generation.

## Getting the most out of LLMs (retrieval, memory, context)

- Lewis et al. (2020), *RAG*, https://arxiv.org/abs/2005.11401. The founding retrieval-augmented generation paper. See [[rag-explained]] and [[getting-the-most-out-of-llms]].
- Gao et al. (2023), *RAG for LLMs: A Survey*, https://arxiv.org/abs/2312.10997. The map of the RAG landscape; pair it with the [2024 survey](https://arxiv.org/abs/2410.12837).
- Asai et al. (2023), *Self-RAG*, https://arxiv.org/abs/2310.11511. Retrieve on demand, then self-critique.
- Liu et al. (2023), *Lost in the Middle*, https://arxiv.org/abs/2307.03172. Why bigger context windows do not automatically help.
- Packer et al. (2023), *MemGPT*, https://arxiv.org/abs/2310.08560. OS-style memory for persistent, stateful agents.
- GraphRAG, https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ (paper: [Edge et al. 2024](https://arxiv.org/abs/2404.16130)). Knowledge-graph retrieval for global, multi-hop questions.

For the full annotated list (DPR, ColBERT, HyDE, RAPTOR, FLARE, CRAG; REALM, RETRO, Atlas, Memorizing Transformers, LongMem, Generative Agents; Position Interpolation, StreamingLLM, Infini-attention, RULER), see [[getting-the-most-out-of-llms]] §Deep-dive reading by area.

## Cognitive style (Kirton A-I)

- Kirton (1976), *Adaptors and Innovators: A Description and Measure*, https://eric.ed.gov/?id=EJ148010. The founding paper on adaptive versus innovative cognitive style.
- Im & Hu (2005), *Revisiting the Factor Structure of the KAI*, https://journals.sagepub.com/doi/10.2466/pr0.96.2.408-410. The three-factor versus four-factor debate.
- KAI Foundation overview, https://kai.foundation/adaption-innovation-measure-cognitive-style/. The style-versus-level distinction in plain terms. See [[kirton-adaption-innovation]] and [[genai-on-the-adaption-innovation-spectrum]].

## If you only read five

Read Vaswani 2017 for how it works, Brown 2020 for in-context learning, Ouyang 2022 for RLHF, Kambhampati 2024 for the limits, and Sutton 2019 for the bigger picture.
