from fastapi import APIRouter, HTTPException
from models import ProcessDocumentRequest
from llm_service import LLMService
from pydantic import BaseModel
from typing import Optional
from gemini_service import GeminiService

router = APIRouter()
llm_service = LLMService()
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

@router.get("/test-openai")
async def test_openai():
    result = await llm_service.test_openai()
    return {"result": result}

@router.post("/process-document")
async def process_document(request: ProcessDocumentRequest):
    result = await llm_service.process_document(request.text)
    return {"result": result}

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
