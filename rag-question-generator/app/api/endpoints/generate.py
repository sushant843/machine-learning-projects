from fastapi import APIRouter, Depends
from app.models.quiz import GenerateRequest, QuizResponse
from app.api.deps import get_retriever
from app.services.generator import generate_quiz

router = APIRouter()

@router.post("/", response_model=QuizResponse)
async def generate_quiz_endpoint(request: GenerateRequest, retriever = Depends(get_retriever)):
    # 1. Retrieve relevant context from Vector DB
    relevant_docs = retriever.get_relevant_documents(request.topic)
    
    # Combine chunks into a single context string
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    
    if not context:
        return QuizResponse(quiz_title="Error", questions=[])
        
    # 2. Generate JSON quiz via LLM
    quiz_data = generate_quiz(context=context, topic=request.topic, num_questions=request.num_questions)
    
    return quiz_data