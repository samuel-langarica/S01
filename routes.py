from fastapi import APIRouter, HTTPException, Response, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from gemini_service import GeminiService
from models import ChatRequest, ChatResponse, PDFResponse
from io import BytesIO

router = APIRouter()
gemini_service = GeminiService()

# Request models
class ChatRequest(BaseModel):
    context: str
    question: str

class ChatResponse(BaseModel):
    answer: str
    error: Optional[str] = None

class PDFResponse(BaseModel):
    text: str
    error: Optional[str] = None

@router.get("/")
async def root():
    return {"message": "Hello World! 👋"}

@router.post("/incoming-call")
async def handle_incoming_call():
    twiml_response = """
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="woman">Thank you for calling. This is a custom message.</Say>
        <Pause length="1"/>
        <Say voice="woman">If you need further assistance, please let us know.</Say>
    </Response>
    """
    return Response(content=twiml_response, media_type="application/xml")


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

@router.post("/extract-pdf", response_model=PDFResponse)
async def extract_pdf_text(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        return PDFResponse(
            text="",
            error="File must be a PDF"
        )
    
    try:
        contents = await file.read()
        pdf_file = BytesIO(contents)
        text = await gemini_service.extract_text_from_pdf(pdf_file)
        return PDFResponse(
            text=text,
            error=None
        )
    except Exception as e:
        return PDFResponse(
            text="",
            error=str(e)
        )
