from fastapi import APIRouter
from models import ProcessDocumentRequest
from llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.get("/")
async def root():
    return {"message": "Connection with S01🤓 is successful"}

@router.post("/process-document")
async def process_document(request: ProcessDocumentRequest):
    result = await llm_service.process_document(request.text)
    return {"result": result} 