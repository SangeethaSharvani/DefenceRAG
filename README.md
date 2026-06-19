# DefenceRAG
# DefenceRAG

## Overview

A Retrieval-Augmented Generation (RAG) system for answering defence procurement and policy questions using the provided corpus.

## Architecture

Corpus (metaData.csv)
→ SentenceTransformer Embeddings (all-MiniLM-L6-v2)
→ FAISS Vector Store
→ Top-K Retrieval
→ Gemini 2.5 Flash
→ Grounded Answer Generation

## Tech Stack

* Python
* Sentence Transformers
* FAISS
* Google Gemini
* Pandas
* NumPy

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Build vector index

```bash
python build_index.py
```

3. Generate answers

```bash
python generate_answers.py
```

Output:

```text
submission.csv
```

## Design Choices

* Semantic retrieval using all-MiniLM-L6-v2
* FAISS for efficient similarity search
* Grounded answer generation from retrieved context
* Source-aware retrieval pipeline
