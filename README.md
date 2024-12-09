# PDF RAG

A Python package for building RAG (Retrieval-Augmented Generation) applications using PDFs, ChromaDB, and Ollama.

## Installation

```bash
pip install -e .
```

## Usage

```python
from pdf_rag import PDFRAGApplication

# Initialize the application
rag = PDFRAGApplication()

# Load a PDF
rag.load_pdf("your_document.pdf")

# Query the system
response = rag.query("What is this document about?")
print(response)
```
