---

# 🚀 CourseMate AI (RAG Project) – Simple Notes

## 📌 What are we building?

**CourseMate AI** = AI study assistant
👉 It lets students **chat with their PDFs / notes** instead of reading everything manually.

**Problem:**

* Too many study materials (PDFs, notes, books)
* Hard to find exact information

**Solution:**

* Ask questions → AI gives answers from your documents

---

# 🧠 What is RAG?

**RAG = Retrieval-Augmented Generation**

👉 Combines:

* Retrieval (search relevant data)
* LLM (generate answer)

👉 Output = **Accurate + Context-based answers**

---

# ⚙️ Complete RAG Pipeline (Step-by-Step)

## Step 1: Upload Documents

* PDFs
* Notes
* Research papers

---

## Step 2: Document Loading

* Convert files → readable format for system

---

## Step 3: Text Splitting (Chunking)

* Break large documents into small parts

👉 Why?

* LLM has token limits
* Improves accuracy

---

## Step 4: Embeddings

* Convert text → numbers (vectors)

Example:

```
"Gradient Descent"
→ [0.23, -0.81, 0.44, ...]
```

👉 Meaning:

* Similar text → similar vectors

---

## Step 5: Vector Database

* Store:

  * embeddings
  * text
  * metadata

👉 Tools:

* FAISS
* Chroma
* Annoy

---

## Step 6: User Query

User asks:

```
"What is NLP?"
```

---

## Step 7: Query Embedding

* Convert question → vector

---

## Step 8: Similarity Search

* Compare query vector with stored vectors

👉 Find most relevant chunks

---

## Step 9: Retriever

* Select **Top-K relevant chunks**
* These become context

---

## Step 10: LLM Response

* LLM generates answer using context

---

# 🔥 Text Splitting (Important Concept)

## Why chunking is important?

1. Better retrieval
2. Accurate embeddings
3. Faster processing

---

## Types of Text Splitting

### 1. Character-Based

* Split by character count
* Simple but not smart

---

### 2. Token-Based

* Split based on tokens (LLM units)
* More accurate

---

### 3. Semantic-Based

* Split based on meaning
* Best method ✅

---

# 🧩 Vector Database vs Normal Database

## Problem with normal DB:

* 1 lakh embeddings
* Each search = compare with all
* Time complexity = **O(n)** ❌

---

## Solution: Vector DB

Uses **ANN (Approximate Nearest Neighbor)**

Algorithms:

* HNSW
* IVF
* PQ

---

## Example (IVF Optimization)

Instead of searching 1 lakh embeddings:

* Divide into clusters (e.g., 5 clusters)
* Search only 1 cluster

👉 Faster search 🚀

---

# 🔍 Retrievers (Core of RAG)

## What is Retriever?

👉 Takes query → returns relevant chunks

---

## Types of Retrievers

### 1. By Data Source

* Wikipedia
* Arxiv
* APIs

---

### 2. By Strategy

---

## 🔹 1. Similarity Search

* Most common
* Finds closest vectors

👉 Problem:

* Returns similar/repeated info

---

## 🔹 2. MMR (Max Marginal Relevance)

👉 Goal:

* Balance:

  * relevance
  * diversity

👉 Avoids duplicate information

---

## 🔹 3. MultiQuery Retriever

👉 Problem:

* One query ≠ enough

Example:

```
"What is gradient descent?"
```

Other forms:

* Explain gradient descent
* How it works?
* Optimization algorithm

---

👉 Solution:

* Generate multiple queries
* Search all
* Combine results

---

# 🧠 Final Architecture (Simple View)

```
PDF → Loader → Split → Embedding → Vector DB
                                      ↓
User Query → Embedding → Retriever → LLM → Answer
```

---

# 🎯 Key Takeaways

* RAG = Search + Generate
* Chunking = very important
* Embeddings = core representation
* Vector DB = fast similarity search
* Retriever = brain of RAG
* LLM = final answer generator

---

If you want, I can next:

* Convert this into **exam notes / MCQs**
* Give **code implementation (LangChain + FAISS)**
* Or help you **build this project step-by-step**
