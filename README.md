# simple-llm-rag-demo

This project demonstrates a simple Retrieval-Augmented Generation (RAG) workflow using Large Language Models (LLMs). It provides example notebooks and configuration files to ingest documents, perform retrieval from a vector database, and generate responses using LLMs.

## Features

- Document ingestion and embedding
- Vector database integration (see [vectorDB/README.md](vectorDB/README.md))
- Example Jupyter notebooks for RAG workflows
- Sample documentation and deployment manifests

## Directory Structure

- `Ingest-client-doc.ipynb` – Notebook for ingesting documents
- `RAG_pdf.ipynb` – Notebook demonstrating RAG with PDF documents
- `vectorDB/` – Vector database configs and deployment files
- `vLLM/` – LLM-related resources
- `docs/` – Sample documentation and reference PDFs


## Getting Started
1. Demo environment - https://catalog.demo.redhat.com/catalog?item=babylon-catalog-prod/sandboxes-gpte.ocp4-demo-rhods-nvidia-gpu-aws.prod&utm_source=webapp&utm_medium=share-link
2. Deploy Vector DB
3. Deploy LLM
4. Run Ingest Client to upload docs to vector DB
5. Run RAG Notebook 



