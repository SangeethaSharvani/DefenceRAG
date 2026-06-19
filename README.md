# DefenceRAG: Procurement & Policy Reasoning System

## Overview

DefenceRAG is a Retrieval-Augmented Generation (RAG) system designed to answer questions related to defence procurement policies, financial delegations, and naval regulations. The system retrieves relevant information from official policy documents and generates grounded, explainable responses with supporting references.

The solution combines semantic search, vector retrieval, and large language models to improve factual accuracy while reducing hallucinations in policy-focused question answering.

---

## Problem Statement

Defence procurement and regulatory documents are often lengthy, complex, and difficult to navigate manually. The objective of this project is to build an intelligent assistant capable of:

* Understanding natural language questions
* Retrieving relevant policy sections from official documents
* Generating concise and context-grounded answers
* Providing traceable references to supporting sources

---

## System Architecture

Source Documents (PDFs)

↓ Text Extraction & Chunking

↓ Embedding Generation (all-MiniLM-L6-v2)

↓ FAISS Vector Index

↓ Top-K Semantic Retrieval

↓ Gemini 2.5 Flash

↓ Grounded Answer Generation

---

## Data Sources

The system utilizes official defence policy and regulatory documents, including:

* Delegation of Financial Powers Rules (DFPR)
* Defence Procurement Manual (DPM)
* Navy Regulations
* Structured metadata corpus (metaData.csv)

To support raw document ingestion, PDF extraction and chunking pipelines were also implemented using pypdf.

---

## Key Features

* Semantic document retrieval
* Vector similarity search using FAISS
* Grounded response generation
* Source-aware retrieval pipeline
* PDF ingestion and chunking support
* Explainable policy question answering
* Modular and extensible architecture

---

## Technology Stack

### Programming Language

* Python

### Retrieval Layer

* Sentence Transformers
* FAISS

### LLM Layer

* Google Gemini 2.5 Flash

### Data Processing

* Pandas
* NumPy
* PyPDF

---

## Design Decisions

### Why Sentence Transformers?

The all-MiniLM-L6-v2 model provides efficient semantic embeddings while maintaining low computational overhead, making it suitable for rapid retrieval tasks.

### Why FAISS?

FAISS enables fast similarity search across thousands of document chunks and provides a lightweight local vector database solution.

### Why Retrieval-Augmented Generation?

Traditional LLMs may hallucinate information when answering policy questions. By grounding responses in retrieved document chunks, the system improves factual reliability and traceability.

### Why Use the Provided Metadata Corpus?

The competition dataset included a preprocessed metadata corpus containing structured chunks extracted from source PDFs. Using this corpus enabled efficient indexing while preserving grounding to the original documents.

---

## PDF Processing Pipeline

Source PDF

↓ Text Extraction (PyPDF)

↓ Chunking (500 characters with overlap)

↓ Embedding Generation

↓ Vector Indexing (FAISS)

↓ Retrieval

↓ Answer Generation

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Build Vector Index

```bash
python build_index.py
```

### Run Retrieval Pipeline

```bash
python generate_answers.py
```

### Output

```text
submission.csv
```

---

## Future Improvements

* Hybrid Retrieval (Keyword + Semantic Search)
* Reranking Models
* Streamlit-based Interactive Interface
* Citation-aware Answer Generation
* Advanced Chunking Strategies
* Multi-document Reasoning

---

## Outcome

The final system successfully demonstrates an end-to-end Defence RAG pipeline capable of retrieving relevant policy information and generating grounded responses from official procurement and regulatory documents.
