import google.generativeai as genai
import os
import PyPDF2
from io import BytesIO

class GeminiService:
    def __init__(self):
        # Get API key from environment variable
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key: 
            raise Exception("GEMINI_API_KEY environment variable not set")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    async def chat_with_context(self, context: str, question: str) -> str:
        """Process a single chat interaction with context."""
        try:
            prompt = f"Context: {context}\n\nQuestion: {question}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error in chat: {str(e)}")

    async def extract_text_from_pdf(self, file: BytesIO) -> str:
        """Extract text from a PDF file."""
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")

gemini_service = GeminiService()