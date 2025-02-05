# PDF RAG

A Python package for building RAG (Retrieval-Augmented Generation) applications using PDFs, ChromaDB, and Ollama.

## Project Structure

```
.
├── pdf_rag
│   ├── document_processor.py
│   ├── __init__.py
│   ├── llm_interface.py
│   ├── main.py
│   └── vector_store.py
├── README.md
├── requirements.txt
├── setup.py
├── test_package.py
└── test.py

2 directories, 10 files
```

## Installation

1. **Create and activate a virtual environment:**

    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows
    venv\Scripts\activate
    # On Unix or MacOS
    source venv/bin/activate
    ```

2. **Install the package:**

    ```bash
    pip install -e .
    ```

3. **Install Ollama on Linux:**

    Follow the steps below to install Ollama on a Linux system.

    ```bash
    # Download the Ollama installer
    curl -fsSL https://ollama.com/install.sh | sh

    # Verify the installation
    ollama --version
    ```

4. **Download models in Ollama:**

    To download specific models such as `llama3` and `deepseek-R1`, use the following commands:

    ```bash
    # Download the llama3 model
    ollama pull llama3

    # Download the deepseek-R1 model
    ollama pull deepseek-R1
    ```

## base Usage

```python
from pdf_rag import PDFRAGApplication

# Initialize the application
rag = PDFRAGApplication(model_name= "deepseek-r1")

# Load a PDF
rag.load_pdf("your_document.pdf")

# Query the system
response = rag.query("What is this document about?")
print(response)
```

## Testing

Run the `test.py` script to see how the module works with ChromaDB:

```python
import chromadb
chroma_client = chromadb.Client()

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print(results)
```
