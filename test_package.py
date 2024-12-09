## Usage
from pdf_rag import PDFRAGApplication

# Initialize the application
rag = PDFRAGApplication( model_name="llama3") 

# Load a PDF
rag.load_pdf("resume.pdf")

# Query the system
response = rag.query("What is this document about?")
print(response)
