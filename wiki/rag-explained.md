---
title: "RAG, Explained Simply"
type: concept
created: 2026-06-08
updated: 2026-06-08
tags: [genai, rag, retrieval, beginner]
sources: [lewis-2020]
---

# RAG, Explained Simply

RAG stands for Retrieval-Augmented Generation. The plain version: instead of letting the model answer from memory alone, you first fetch the relevant documents and hand them to it, then ask it to answer using them.

## The open-book analogy

A plain LLM is like a knowledgeable person answering from memory. They are fluent, but they can misremember or invent things, because their knowledge is baked into frozen weights with no way to look a fact up ([[how-genai-works]] §Storage). That is why they hallucinate ([[what-genai-is-good-and-bad-at]]).

RAG hands that same person an open book before they answer. They still do the talking, but now they are reading from real source material instead of relying on recall.

## How it works, in three steps

1. Retrieve. Take the question and search a document collection (your files, a wiki, a database) for the passages most relevant to it.
2. Augment. Paste those passages into the prompt alongside the question, so they become the model's working memory for this one answer.
3. Generate. The model writes its answer from those passages rather than from memory alone.

The technique was named by [Lewis et al. 2020](https://arxiv.org/abs/2005.11401).

## Why it matters

It cuts hallucination, because the real facts sit in the context, so the model is more likely to be accurate and can cite where an answer came from. It also adds knowledge the model never learned, such as your private documents or anything newer than its training cutoff, without retraining it.

## One caveat

RAG reduces hallucination but does not remove it. If the retrieval step pulls the wrong documents, or the model misreads them, you still get a wrong answer. Improving that retrieval step is what the more advanced techniques (reranking, query rewriting, and the like) are for; see [[getting-the-most-out-of-llms]].

This wiki is itself a RAG-friendly source. `index.md` and the topic pages are the kind of curated, already-organized documents a RAG system retrieves from.

## Sources

- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* https://arxiv.org/abs/2005.11401
