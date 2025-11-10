from fastapi import APIRouter
from pydantic import BaseModel
from app.services.qa_service import ask_question

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question_endpoint(request: QuestionRequest):
    answer = ask_question(request.question)
    return {"answer": answer}



"""from fastapi import APIRouter
from app.services.qa_service import ask_question

router = APIRouter()

@router.post("/ask")
async def ask_question_endpoint(question: str):
    answer = ask_question(question)
    return {"answer": answer}"""
