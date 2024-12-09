from pypdf import PdfReader
from typing import List, Dict
import re

class DocumentProcessor:
    def __init__(self):
        self.documents = []

    def process_pdf(self, pdf_path: str, chunk_size: int = 1000) -> List[str]:
        """Extract and chunk text from PDF."""
        reader = PdfReader(pdf_path)
        text = ""
        
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
        # Clean text
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        # Create chunks
        chunks = []
        words = text.split()
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_chunk.append(word)
            current_size += len(word) + 1
            
            if current_size >= chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_size = 0
                
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        self.documents.extend(chunks)
        return chunks
