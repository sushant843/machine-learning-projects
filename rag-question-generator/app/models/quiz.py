from pydantic import BaseModel, Field
from typing import List

class Question(BaseModel):
    question_text: str = Field(description="The question based on the document context")
    options: List[str] = Field(description="List of 4 multiple choice options")
    correct_answer: str = Field(description="The correct option from the list")
    explanation: str = Field(description="Brief explanation of why the answer is correct")

class QuizResponse(BaseModel):
    quiz_title: str = Field(description="Title of the quiz")
    questions: List[Question] = Field(description="List of generated questions")

class GenerateRequest(BaseModel):
    topic: str
    num_questions: int = 3