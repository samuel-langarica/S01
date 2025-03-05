from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    context: str
    question: str

class ChatResponse(BaseModel):
    answer: str
    error: Optional[str] = None

class PDFResponse(BaseModel):
    text: str
    error: Optional[str] = None 