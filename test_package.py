from pdf_rag import PDFRAGApplication

def test_pdf_rag():
    # Initialize the application
    rag = PDFRAGApplication(model_name= "deepseek-r1")

    # Load a PDF
    rag.load_pdf("your_document.pdf")

    # Query the system
    response = rag.query("What is this document about?")
    print(response)

if __name__ == "__main__":
    test_pdf_rag()