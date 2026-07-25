from app.services.vector_store import get_vector_store

def get_retriever():
    """Dependency to inject the Chroma retriever."""
    vector_store = get_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": 4})