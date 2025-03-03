from pydantic import BaseModel

class ProcessDocumentRequest(BaseModel):
    text: str