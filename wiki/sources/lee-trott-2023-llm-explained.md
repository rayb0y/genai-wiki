---
title: "Source: Lee & Trott (2023), Large Language Models, Explained with a Minimum of Math and Jargon"
type: source
created: 2026-06-04
updated: 2026-06-08
tags: [genai, llm, explainer, interpretability, source]
sources: []
---

# Source: Lee & Trott (2023), *Large Language Models, Explained with a Minimum of Math and Jargon*

Authors: Timothy B. Lee (journalist with a CS master's) and Sean Trott (cognitive scientist, UC San Diego). Published: July 27, 2023 on *Understanding AI* (Substack); page metadata shows a later edit on April 16, 2024. URL: https://www.understandingai.org/p/large-language-models-explained-with Type: long-form popular explainer (a secondary source), notable for being unusually accurate and for citing primary interpretability research.

## What it covers

A jargon-light walkthrough of how decoder LLMs (built around GPT-3) work:

1. Word vectors and embeddings: words as points in high-dimensional space, word2vec, vector arithmetic for analogies, and the way embeddings inherit human biases. Maps to [[how-genai-works]] §Storage.
2. Context-dependent meaning: the same word gets different vectors in different contexts (homonyms versus polysemy).
3. The transformer: stacked layers, each refining "hidden state" vectors. It uses GPT-3's real numbers: 96 layers, 12,288-dimensional vectors, and 96 attention heads per layer, which is 9,216 attention operations per token.
4. Attention: query, key, and value "matchmaking" that moves information between tokens, with a worked example from the Redwood Research IOI circuit in GPT-2.
5. Feed-forward layers: a pattern-matching "memory" of facts learned in training, illustrated by the Poland-to-Warsaw vector-arithmetic example. The division of labor is that attention retrieves from the prompt while feed-forward recalls from training. Maps to [[how-genai-works]] §Retrieval.
6. Training: self-supervised next-word prediction, backprop (the "squirrels and valves" analogy), and scale.
7. Why it works: scaling laws, theory-of-mind results, "Sparks of AGI," the stochastic-parrots debate, and prediction as foundational to intelligence.

The article's framing, that LLMs are next-token predictors whose abilities come from scale and whose inner workings remain uncertain, is consistent with this wiki's [[how-genai-works]]. It is a good lay companion to that page.

## Research cited in this article (now in the wiki's bibliography)

The primary and secondary works the article links, with what each shows:

- Mikolov et al. (2013), word2vec, https://arxiv.org/abs/1301.3781. Embeddings and vector arithmetic for analogies. Already in the wiki; see [[how-genai-works]] and [[reading-list]].
- Caliskan, Bryson, Narayanan (2017), human-like biases in word embeddings, https://www.science.org/doi/10.1126/science.aal4230. Embeddings encode social biases (for example doctor − man + woman → nurse). Relevant to fairness and limits.
- Contextual embeddings and polysemy (2020), https://arxiv.org/abs/2010.13057. Models use more similar vectors for polysemous senses than for homonyms.
- Vaswani et al. (2017), the transformer, https://arxiv.org/abs/1706.03762. Already in the wiki.
- Tenney, Das, Pavlick (2019), *BERT Rediscovers the Classical NLP Pipeline*, https://arxiv.org/abs/1905.05950. Early layers handle syntax, later layers handle semantics.
- Wang et al. / Redwood Research (2022), *Interpretability in the Wild* (IOI circuit in GPT-2), https://arxiv.org/abs/2211.00593. A reverse-engineered set of nine attention heads (Name Mover, Subject Inhibition, Duplicate Token) for one prediction, showing how hard full interpretability is.
- Geva et al. (2020), *Transformer Feed-Forward Layers Are Key-Value Memories*, https://arxiv.org/abs/2012.14913. FFN neurons act as pattern detectors and key-value stores.
- Merullo, Eickhoff, Pavlick (2023), *Language Models Implement Simple word2vec-style Vector Arithmetic*, https://arxiv.org/abs/2305.16130. FFN layers do analogy-style vector math (Poland to Warsaw).
- Kaplan et al. (2020), scaling laws, https://arxiv.org/abs/2001.08361. Already in the wiki.
- Kosinski (2023), *Theory of Mind May Have Spontaneously Emerged in LLMs*, https://arxiv.org/abs/2302.02083. GPT-4 around 95% on false-belief tasks.
- Ullman (2023), *LLMs Fail on Trivial Alterations to Theory-of-Mind Tasks*, https://arxiv.org/abs/2302.08399. Trivial rewordings break the ToM result (a "clever Hans" effect).
- Bubeck et al. (2023), *Sparks of Artificial General Intelligence*, https://arxiv.org/abs/2303.12712. The GPT-4 "sparks of AGI" claim (for example the TikZ unicorn). Contested.
- Bender et al. (2021), *Stochastic Parrots*, https://dl.acm.org/doi/10.1145/3442188.3445922. Already in the wiki; see [[what-genai-is-good-and-bad-at]].

## Where this article has likely dated (newer research)

The mechanics it explains (embeddings, attention, feed-forward, next-token prediction, trained by backprop at scale) remain correct and current. What has moved since mid-2023 is the surrounding picture.

Interpretability is less hopeless than the article implies. It says understanding even a single prediction could take months or years and that a full account is unlikely any time soon. That is now partly dated: Anthropic's sparse-autoencoder and dictionary-learning work scaled to a production model, extracting about 34 million interpretable, often multilingual and multimodal features from Claude 3 Sonnet ([Scaling Monosemanticity, 2024](https://transformer-circuits.pub/2024/scaling-monosemanticity/)). Real, steerable features can now be read out, which is a different trajectory from "decades away."

"Predict the next word" is no longer the whole training story. The article treats LLMs as pure next-word predictors, with RLHF in a footnote. Since late 2024, reasoning models are trained with large-scale reinforcement learning on chain-of-thought and spend more compute at inference time. One example is DeepSeek-R1, which reached o1-level math and reasoning, partly through RL with no supervised warm-up in its R1-Zero variant ([DeepSeek-AI 2025](https://arxiv.org/abs/2501.12948)). The next-token substrate is the same, but capability now comes substantially from post-training rather than pretraining alone ([[how-genai-works]]).

The theory-of-mind claim has become more rigorous and more mixed. Kosinski's "spontaneously emerged ToM," which the article cites approvingly, was challenged the same year by Ullman's trivial-alteration failures ([2302.08399](https://arxiv.org/abs/2302.08399)). The article notes this, but the current reference is the 2024 systematic study: GPT-4 matched or beat humans on false belief, irony, hints, and misdirection, yet failed at detecting faux pas, so its ToM is uneven rather than uniform ([Strachan et al. 2024, Nature Human Behaviour](https://www.nature.com/articles/s41562-024-01882-z)).

"Sparks of AGI" has aged into a contested, conflicted source. Bubeck et al. tested a non-public, pre-release GPT-4 (Microsoft is an OpenAI investor) with hand-picked examples and no reproducible protocol, and it now reads more as suggestive marketing than as evidence. See the [[what-genai-is-good-and-bad-at]] note on benchmark and contamination caveats.

The emergence the article leans on is itself disputed. Apparent sudden capability jumps are largely an artifact of the metric ([Schaeffer et al. 2023](https://arxiv.org/abs/2304.15004), see [[how-genai-works]]), a counterpoint the piece does not incorporate.

GPT-3 is no longer the architectural archetype. The article's dense 175B, 96-layer picture is now a generation behind. Frontier models are widely reported to use Mixture-of-Experts, where only a subset of expert sub-networks fire per token, along with far longer context windows and natively multimodal training. GPT-4's specifics remain undisclosed but are widely described as MoE ([IBM, What is mixture of experts?](https://www.ibm.com/think/topics/mixture-of-experts)).

Scaling guidance has moved past Kaplan (2020). The article cites Kaplan's scaling laws; the compute-optimal correction is Chinchilla, which says to scale data and parameters together ([Hoffmann et al. 2022](https://arxiv.org/abs/2203.15556)), alongside the 2024–2025 debate about a pretraining "data wall." See [[how-genai-works]].

In short, this is still an excellent mechanics explainer, but its capability and frontier claims (the interpretability timeline, theory of mind, "sparks of AGI," and GPT-3 as the archetype) should be read as a 2023 snapshot, superseded by the points above.

## Sources

- Lee, T. & Trott, S. (2023). *Large Language Models, Explained with a Minimum of Math and Jargon.* https://www.understandingai.org/p/large-language-models-explained-with
- Anthropic (2024). *Scaling Monosemanticity.* https://transformer-circuits.pub/2024/scaling-monosemanticity/
- DeepSeek-AI (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL.* https://arxiv.org/abs/2501.12948
- Strachan, J. et al. (2024). *Testing theory of mind in large language models and humans.* Nature Human Behaviour. https://www.nature.com/articles/s41562-024-01882-z
- Ullman, T. (2023). *Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks.* https://arxiv.org/abs/2302.08399
- Kosinski, M. (2023). *Theory of Mind May Have Spontaneously Emerged in Large Language Models.* https://arxiv.org/abs/2302.02083
- Bubeck, S. et al. (2023). *Sparks of Artificial General Intelligence.* https://arxiv.org/abs/2303.12712
- Geva, M. et al. (2020). *Transformer Feed-Forward Layers Are Key-Value Memories.* https://arxiv.org/abs/2012.14913
- Tenney, I. et al. (2019). *BERT Rediscovers the Classical NLP Pipeline.* https://arxiv.org/abs/1905.05950
- Wang, K. et al. (2022). *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small.* https://arxiv.org/abs/2211.00593
- Merullo, J. et al. (2023). *Language Models Implement Simple word2vec-style Vector Arithmetic.* https://arxiv.org/abs/2305.16130
- Caliskan, A., Bryson, J., Narayanan, A. (2017). *Semantics derived automatically from language corpora contain human-like biases.* Science. https://www.science.org/doi/10.1126/science.aal4230
- Hoffmann, J. et al. (2022). *Training Compute-Optimal LLMs (Chinchilla).* https://arxiv.org/abs/2203.15556
- Schaeffer, R. et al. (2023). *Are Emergent Abilities of LLMs a Mirage?* https://arxiv.org/abs/2304.15004
