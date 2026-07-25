from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "RAG Question Generator"
    OPENAI_API_KEY: str
    CHROMA_PERSIST_DIRECTORY: str = "./data/chromadb"
    UPLOAD_DIRECTORY: str = "./data/uploads"

    class Config:
        env_file = ".env"

# Ensure directories exist
os.makedirs(Settings().UPLOAD_DIRECTORY, exist_ok=True)
os.makedirs(Settings().CHROMA_PERSIST_DIRECTORY, exist_ok=True)

settings = Settings()