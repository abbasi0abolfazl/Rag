from setuptools import setup, find_packages

setup(
    name="pdf_rag",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pypdf",
        "chromadb",
        "requests"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A RAG application for PDF documents using ChromaDB and Ollama",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
