# 🚀 Generative AI – Complete Simple Notes

---

# 📌 Prerequisites (Before Starting)

You should know:

* Python Programming
* Machine Learning basics
* Deep Learning concepts
* Transformers
* Basic NLP

  * Tokenization
  * Embeddings

---

# 🧠 Learning Phases (Big Picture)

## Phase 1: Research Layer

* New ideas and models are developed

---

## Phase 2: Bedrock Models

* Core foundation models (LLMs) are built

---

## Phase 3: Providers

* Companies provide access to models
  (APIs, SDKs)

---

## Phase 4: You (Developer Role)

* Use these models
* Build real-world AI applications

---

# 🗺️ Plan of Action

You will learn:

1. LLM Foundations
2. RAG Systems
3. Agentic AI
4. Projects + Deployment

---

# ❓ What is an LLM?

## LLM = Large Language Model

### 1. Large

* Trained on huge data:

  * Books
  * Websites
  * Wikipedia
  * Code
  * Conversations

---

### 2. Language

* Works with:

  * English, Hindi, etc.
  * Programming languages

---

### 3. Model

* Deep learning system
* Neural network
* Learns patterns from data

---

## ⚠️ How LLM Actually Works

When you ask:

> “What is Python?”

LLM does NOT:

* Search Google
* Think like a human
* Truly understand meaning

LLM actually:

* Uses learned patterns
* Predicts next word
* Generates output word-by-word

---

# 🌍 Popular LLMs

* GPT models
* Gemini
* LLaMA
* Claude
* Grok
* Mistral

---

# ⚠️ Important Concept

👉 In Generative AI:

* We **don’t build LLMs from scratch**
* We **use pre-built models effectively**

---

# 💻 Using LLMs (Examples)

## OpenAI Example

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain LLM simply."}
    ],
)

print(response.choices[0].message.content)
```

---

## Gemini Example

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Explain LLM simply."
)

print(response.text)
```

---

## Claude Example

```python
import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

response = client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Explain LLM simply."}
    ],
)

print(response.content[0].text)
```

---

# 🚨 Problem

Each provider has:

* Different SDK
* Different syntax
* Different response format

👉 Hard to build scalable apps

---

# ✅ Solution: LangChain

LangChain standardizes everything

---

# 🧩 LangChain Components

* Models
* Prompts
* Chains
* Memory
* Indexes
* Agents

---

# 🧠 Models (Core Layer)

Models generate:

* Text
* Embeddings
* Outputs

They connect to providers like:

* OpenAI
* Google
* Anthropic

---

## Types of Models

### 1. Chat / Language Models

* Text generation
* Q&A
* Code writing
* Summarization

---

### 2. Embedding Models

* Convert text → vectors
* Used in search & RAG
* Find similarity

---

### 3. Multimodal Models

* Handle:

  * Images
  * Audio
  * Files

---

# 📝 Prompts

## What is a Prompt?

Instruction given to LLM

👉 Tells:

* What to do
* How to respond
* Output format

---

## Important Idea

👉 Better prompt = Better output

---

## Types of Prompts

### 1. Simple Prompt

```
Explain Machine Learning
```

---

### 2. System + User Prompt

* System → behavior
* User → question

Example:

```
System: You are a teacher
User: Explain LLM
```

---

### 3. Prompt Templates

Reusable prompts

Example:

```
Explain {topic}
```

---

### 4. Structured Output

* JSON
* Bullet points
* Fixed format

Example:

```
Return JSON with: definition, example
```

---

# 🔗 Chains

## What is Chain?

Sequence of steps

👉 Instead of:

* One input → one output

👉 We do:

* Step 1 → Step 2 → Step 3 → Final output

---

## Example

User asks:

> Summarize and translate

Steps:

1. Summarize
2. Translate
3. Return result

---

# 🧠 Memory

## What is Memory?

* Stores past interactions

---

## Without Memory

* Every query is independent

---

## With Memory

* AI remembers context

---

## Example

User:

> My name is Akarsh

Later:

> What is my name?

👉 With memory → correct answer

---

# 📚 Indexes (Very Important)

## Problem

LLMs:

* Don’t know private data
* Don’t know company data
* Don’t update in real-time

---

## Solution

👉 Connect external data

Sources:

* PDFs
* Databases
* Websites
* Documents

---

## This System is Called:

👉 **Retrieval**

---

# 🤖 Agents

## What are Agents?

AI systems that:
👉 Decide what to do next

---

## Difference

### Chains

* Fixed steps

### Agents

* Dynamic decision-making

---

## Why Agents Needed?

Some tasks need:

* Web search
* Calculations
* API calls
* Database queries

👉 LLM alone cannot do this
👉 Needs tools

---

# 🎯 Final Understanding

## Flow of Modern AI System

```
User → Prompt → LLM → Response
```

👉 Advanced systems:

```
User → Prompt → Chain / Agent → Tools / Data → LLM → Response
```

---

# 🚀 Final Line

👉 You are moving from:

* Just using AI

👉 To:

* Building real AI systems

---
