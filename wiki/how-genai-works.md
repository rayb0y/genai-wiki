---
title: "How GenAI Works: Storage, Retrieval, Interaction"
type: concept
created: 2026-06-04
updated: 2026-06-14
tags: [genai, llm, storage, retrieval, interaction, diffusion]
sources: [vaswani-2017, brown-2020, lewis-2020, mikolov-2013, ho-2020, ouyang-2022, deepseek-2025, kaplan-2020, hoffmann-2022, rombach-2022]
---

# How GenAI Works

Generative AI learns the statistical structure of a large dataset and then samples from it to produce new content. For text the engine is the transformer, trained to predict the next token (a sub-word unit). For images it is diffusion, trained to turn noise into a picture. Everything below describes the text case unless noted, with the image case at the end. Three lenses organize how it works: how it stores knowledge, how it retrieves it, and how you interact with it.

Mechanically, an LLM takes the text so far, runs it up through stacked transformer layers, produces a probability distribution over the next token, samples one, appends it, and repeats ([Vaswani et al. 2017](https://arxiv.org/abs/1706.03762)). It is a next-token predictor, and its usefulness comes from scale.

In more detail, each attention step computes Attention(Q, K, V) = softmax(QK^T / √d_k) V, a scaled dot product between each token's query and every token's key that is normalized into weights over the values ([Vaswani et al. 2017](https://arxiv.org/abs/1706.03762)). The original transformer used 8 parallel attention heads, a model width of 512, and 6 encoder plus 6 decoder layers, and reached 28.4 BLEU on the WMT-2014 English-to-German translation task. GPT-3, the model that made in-context learning famous, scaled the same decoder-only design to 175 billion parameters across 96 layers, a width of 12,288, 96 attention heads, and a 2,048-token context window, trained on roughly 300 billion tokens of filtered web text, books, and Wikipedia ([Brown et al. 2020](https://arxiv.org/abs/2005.14165)).

## Storage: where knowledge lives

A model holds information in a few distinct places, and it helps to keep them separate.

- Parametric memory (the weights). Most of what a model knows is spread across its billions of parameters during training. This memory is durable but frozen at the training cutoff, and it has no index, so the model reconstructs facts rather than looking them up. That is one reason it fabricates ([[what-genai-is-good-and-bad-at]]). RAG calls this its parametric memory ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)).
- Embeddings (the representation). Every token is a vector in a space where nearby points mean similar things, so semantic and analogical relationships show up as geometry. The idea comes from word2vec ([Mikolov et al. 2013](https://arxiv.org/abs/1301.3781)). Attention operates on these vectors, and the same idea powers external search.
- Context window (working memory). The tokens in the current prompt are short-term memory. The model can use them precisely, but they are volatile: once they scroll out of the window they are gone, and there is no memory across sessions by default.
- External store. Documents and vector databases hold knowledge the weights do not have, ready to be pulled into the context on demand. This is the non-parametric memory in RAG ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)).

One way to hold all this: the weights are long-term memory (durable, frozen, fuzzy), the context window is working memory (precise but volatile), and an external store is a library you can fetch from.

## Retrieval: how knowledge is accessed

- Attention as lookup, inside the model. Self-attention is a content-based search. Each token forms a query, matches it against every other token's key, and reads out the best-matching values ([Vaswani et al. 2017](https://arxiv.org/abs/1706.03762)). Every layer runs a weighted search over the current context.
- Parametric recall, from the weights. A bare factual question is answered by reconstructing patterns spread across the weights. The result is fluent but can be wrong or out of date.
- In-context retrieval, from the prompt. If the facts are already in the context window, attention pulls them out accurately. That is why pasting a document in and asking about it works better than relying on memory.
- External retrieval, or RAG. Embed the query, fetch the most similar documents from a corpus, and put them in the context so the answer is grounded in real, updatable text ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)). This improves accuracy but does not remove error. In the original system a dense retriever (DPR) pulls from about 21 million hundred-word Wikipedia passages and a BART generator conditions on the top five retrieved passages, which set new state-of-the-art results on open-domain question answering ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)).

Reliability rises as you move from parametric recall to in-context to retrieved facts.

## Interaction: how you use it

- Prompting and in-context learning. This is the main interface. At sufficient scale a model performs new tasks from a few examples in the prompt, with no retraining ([Brown et al. 2020](https://arxiv.org/abs/2005.14165)). It is why prompting, few-shot examples, and "show your work" all work: you are configuring behavior through the context.
- Chat, system prompts, instruction following. Chat models are fine-tuned and aligned so they follow directions rather than only continuing text. That behavior comes from instruction tuning and reinforcement learning from human feedback (RLHF), not from pretraining alone ([Ouyang et al. 2022](https://arxiv.org/abs/2203.02155)). One caveat is worth keeping in mind: RLHF optimizes for what raters prefer, not for what is true, which is part of why models can be confidently wrong or sycophantic. InstructGPT built this behavior from about 13,000 labeler-written demonstrations for the supervised stage and roughly 33,000 ranked comparisons for the reward model, after which a 1.3-billion-parameter aligned model was preferred by human raters over the 175-billion-parameter GPT-3 ([Ouyang et al. 2022](https://arxiv.org/abs/2203.02155)).
- Decoding controls. Because generation samples, a few settings shape the output. Temperature controls how peaked the distribution is (low is more deterministic, high more varied), and top-k or top-p restrict sampling to likely tokens. Two things follow: the same prompt can give different answers, and the model has no built-in notion of one correct output, only likely continuations.
- Tool use and reasoning. The model can call external tools, such as a calculator, code, search, or a database, by emitting a structured call that an outside system runs and feeds back in. This is the basis of agents and the practical fix for tasks the model is bad at. When a model writes intermediate steps (chain-of-thought), it is using its own output as a scratchpad it can attend to. Reasoning models such as o1 and [DeepSeek-R1](https://arxiv.org/abs/2501.12948) are trained with RL to do a lot of this and to spend more compute at inference time. The substrate is still next-token prediction, but more of the capability now comes from this post-training than from pretraining alone.

## How it's trained (in brief)

Training runs in stages. Pretraining is self-supervised next-token prediction on a large corpus, and it is where broad knowledge comes from. Instruction tuning then fits the model to curated request-and-response examples. RLHF comes last: people rank outputs, a reward model is learned from those rankings, and the model is optimized toward it ([Ouyang et al. 2022](https://arxiv.org/abs/2203.02155)). Performance improves predictably with scale, which is why labs kept scaling, though the newest gains come more from RL on reasoning than from size alone. Kaplan and colleagues established the scaling picture by training more than 200 models and finding that test loss falls as a smooth power law in compute, data, and parameters across more than seven orders of magnitude ([Kaplan et al. 2020](https://arxiv.org/abs/2001.08361)). Chinchilla later corrected the recipe: for a fixed compute budget, data and parameters should grow together at roughly 20 training tokens per parameter, and a 70-billion-parameter Chinchilla trained on 1.4 trillion tokens outperformed the much larger 280-billion-parameter Gopher ([Hoffmann et al. 2022](https://arxiv.org/abs/2203.15556)).

## Image generation (in brief)

The principle is the same, learn a distribution and sample from it, but the mechanism differs. A diffusion model is trained to reverse a process that gradually adds noise to images. At generation time it starts from pure noise and removes it step by step until a picture appears, steered by a text prompt ([Ho et al. 2020](https://arxiv.org/abs/2006.11239)). It also shares the same failure mode as text GenAI: it samples plausible output, and plausible is not the same as correct, which is how you get a six-fingered hand or a fabricated citation. In the original method the forward process adds Gaussian noise over a long series of steps and the network is trained to predict the noise added at each step, an objective the authors connect to denoising score matching, which reached an Inception score of 9.46 and a state-of-the-art FID of 3.17 on unconditional CIFAR-10 ([Ho et al. 2020](https://arxiv.org/abs/2006.11239)). Latent diffusion later ran the same process in a compressed latent space rather than on raw pixels, which cut the cost enough to make systems like Stable Diffusion practical ([Rombach et al. 2022](https://arxiv.org/abs/2112.10752)).

## What this explains

Predicting the next token with attention, at scale, accounts for both sides of the ledger: the strengths (fluency, breadth, pattern completion, in-context learning) and the weaknesses (no guaranteed facts, no reliable planning, sensitivity to phrasing) covered in [[what-genai-is-good-and-bad-at]]. The same storage, retrieval, and interaction split names the levers you can actually pull. You can change what is stored (fine-tune, add memory), how it is retrieved (RAG, longer context), or how you interact with it (prompts, tools). The most reliable gains come from grounding the model in retrieved or tool-provided facts instead of trusting parametric recall.

## Sources

- Vaswani, A. et al. (2017). *Attention Is All You Need.* https://arxiv.org/abs/1706.03762
- Mikolov, T. et al. (2013). *Efficient Estimation of Word Representations in Vector Space (word2vec).* https://arxiv.org/abs/1301.3781
- Brown, T. et al. (2020). *Language Models are Few-Shot Learners.* https://arxiv.org/abs/2005.14165
- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* https://arxiv.org/abs/2005.11401
- Ouyang, L. et al. (2022). *Training Language Models to Follow Instructions with Human Feedback.* https://arxiv.org/abs/2203.02155
- Ho, J., Jain, A., Abbeel, P. (2020). *Denoising Diffusion Probabilistic Models.* https://arxiv.org/abs/2006.11239
- Rombach, R. et al. (2022). *High-Resolution Image Synthesis with Latent Diffusion Models.* https://arxiv.org/abs/2112.10752
- Kaplan, J. et al. (2020). *Scaling Laws for Neural Language Models.* https://arxiv.org/abs/2001.08361
- Hoffmann, J. et al. (2022). *Training Compute-Optimal Large Language Models (Chinchilla).* https://arxiv.org/abs/2203.15556
- DeepSeek-AI (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL.* https://arxiv.org/abs/2501.12948
