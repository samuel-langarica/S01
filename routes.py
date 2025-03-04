from fastapi import APIRouter
from models import ProcessDocumentRequest
from llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

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
