from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from gemini_service import GeminiService

router = APIRouter()
gemini_service = GeminiService()

# Request models
class ChatRequest(BaseModel):
    context: str
    question: str

class ChatResponse(BaseModel):
    answer: str
    error: Optional[str] = None

@router.get("/")
async def root():
    return {"message": "Hello World! 👋"}

@router.post("/chat", response_model=ChatResponse)
async def chat_with_context(request: ChatRequest):
    try:
        response = await gemini_service.chat_with_context(
            context=request.context,
            question=request.question
        )
        return ChatResponse(
            answer=response,
            error=None
        )
    except Exception as e:
        return ChatResponse(
            answer="",
            error=str(e)
        )
