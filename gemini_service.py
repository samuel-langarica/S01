import sys
print("Python path:", sys.executable)
print("System path:", sys.path)

from google import genai
import PyPDF2
import os

class GeminiService:
    def __init__(self):
        # Get API key from environment variable
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            raise Exception("GEMINI_API_KEY environment variable not set")
        self.client = genai.Client(api_key=api_key)

    def extract_text_from_pdf(self, pdf_path):
        """Extract text from a PDF file."""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None

    async def chat_with_context(self, context: str, question: str) -> str:
        """Process a single chat interaction with context."""
        try:
            prompt = f"Context: {context}\n\nQuestion: {question}"
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            raise Exception(f"Error in chat: {str(e)}") 
gemini_service = GeminiService()