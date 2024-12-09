import chromadb
from chromadb.config import Settings
from typing import List, Dict

class VectorStore:
    def __init__(self, collection_name: str = "pdf_collection"):
        self.client = chromadb.Client(Settings(allow_reset=True))
        self.collection = self.client.get_or_create_collection(collection_name)

    def add_documents(self, documents: List[str], metadatas: List[Dict] = None):
        """Add documents to ChromaDB."""
        if metadatas is None:
            metadatas = [{"source": f"chunk_{i}"} for i in range(len(documents))]
            
        self.collection.add(
            documents=documents,
            ids=[f"id_{i}" for i in range(len(documents))],
            metadatas=metadatas
        )

    def query(self, query_text: str, n_results: int = 3) -> Dict:
        """Query the vector store."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results
