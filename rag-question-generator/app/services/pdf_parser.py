from langchain_community.document_loaders import PyPDFLoader

def parse_pdf(file_path: str):
    """Extracts text from a PDF file."""
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents