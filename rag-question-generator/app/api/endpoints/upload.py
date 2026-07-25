from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.config import settings
from app.services.pdf_parser import parse_pdf
from app.services.chunker import chunk_documents
from app.services.vector_store import add_to_vector_store
import os
import shutil

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
    file_path = os.path.join(settings.UPLOAD_DIRECTORY, file.filename)
    
    # Save the file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # 1. Parse PDF
        documents = parse_pdf(file_path)
        # 2. Chunk Text
        chunks = chunk_documents(documents)
        # 3. Store in Vector DB
        add_to_vector_store(chunks)
        
        return {"message": f"Successfully ingested {file.filename}", "chunks_processed": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))