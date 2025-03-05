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