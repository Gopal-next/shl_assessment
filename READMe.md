# SHL Assessment Recommendation Agent

An AI-powered recommendation system that assists recruiters in selecting the most suitable assessments through natural language conversations.

## Overview

This project provides intelligent assessment recommendations by combining Large Language Models, semantic retrieval, and conversational memory.

Recruiters can describe hiring requirements incrementally, and the system refines recommendations through a consultative dialogue.

Example:

* User: *I need an assessment for a Java Developer.*
* Agent: *Which experience level are you targeting?*
* User: *Mid-level.*
* Agent: *Are you interested in technical skills, behavioral traits, or both?*
* User: *Both.*
* Agent returns the most relevant SHL assessments.

---

## Features

* Conversational recommendation workflow
* Multi-turn context awareness
* Clarification-based interaction
* Semantic retrieval using embeddings
* Top-K assessment recommendations
* Grounded responses from SHL catalog
* FAISS local vector database
* FastAPI backend APIs
* Swagger documentation
* Deployment-ready architecture

---

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic

### LLM & Orchestration

* LangChain
* Gemini API
* Gemini Embeddings

### Retrieval

* FAISS
* Semantic Search

### Deployment

* Render

---

## Architecture

User Query

↓

Conversation Memory

↓

LangChain Agent

↓

Clarification Loop

↓

Gemini Embedding

↓

FAISS Similarity Search

↓

Top-K Retrieval

↓

Gemini Response Generation

↓

Assessment Recommendations


---

## Deployment

Application deployed using Render.

Considerations:

* Free-tier storage limitations
* Precomputed embeddings
* Local FAISS persistence
* Reduced inference latency
* No embedding generation during runtime

---

## Challenges Solved

### Irrelevant Retrieval

Improved document representation by incorporating:

* Assessment names
* Skills
* Job levels
* Duration
* Descriptions

---

### Context Loss

Maintained conversation history across turns.

---

### Hallucinations

Restricted recommendations strictly to assessments available within the SHL catalog.

---

## Future Improvements

* Redis session memory
* Metadata filtering
* Hybrid Search (BM25 + FAISS)
* Reranking models
* Multi-user support
* Persistent chat sessions
* Evaluation metrics (Precision@K, Recall@K)

---

## Author

Gopal Kumar

AI Engineer | Generative AI | RAG | LangChain | FastAPI
