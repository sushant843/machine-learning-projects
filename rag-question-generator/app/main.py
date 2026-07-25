from fastapi import FastAPI
from app.api.endpoints import upload, generate
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for ingesting PDFs and generating JSON-based quizzes via RAG."
)

app.include_router(upload.router, prefix="/api/upload", tags=["Ingestion"])
app.include_router(generate.router, prefix="/api/generate", tags=["Generation"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the RAG Question Generator API. Visit /docs for the Swagger UI."}