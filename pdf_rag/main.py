from pdf_rag.document_processor import DocumentProcessor
from pdf_rag.vector_store import VectorStore
from pdf_rag.llm_interface import LLMInterface

class PDFRAGApplication:
    def __init__(self, model_name: str = "llama2"):
        self.document_processor = DocumentProcessor()
        self.vector_store = VectorStore()
        self.llm = LLMInterface(model_name)

    def load_pdf(self, pdf_path: str):
        """Load and process a PDF file."""
        chunks = self.document_processor.process_pdf(pdf_path)
        self.vector_store.add_documents(chunks)
        return len(chunks)

    def query(self, question: str, n_results: int = 3) -> str:
        """Query the RAG system."""
        results = self.vector_store.query(question, n_results)
        context = results["documents"][0]
        response = self.llm.generate_response(question, context)
        return response
