from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from app.core.config import settings

def get_vector_store():
    """Initializes and returns the Chroma vector store."""
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    
    vector_store = Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIRECTORY,
        embedding_function=embeddings
    )
    return vector_store

def add_to_vector_store(chunks):
    """Adds document chunks to the Chroma database."""
    vector_store = get_vector_store()
    vector_store.add_documents(documents=chunks)
    vector_store.persist()