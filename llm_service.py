from openai import OpenAI

class LLMService:
    def __init__(self):
        self.openai_client = OpenAI()  # No pasamos la API key aquí

    async def process_document(self, text: str) -> str:
        return "processed"

    async def test_openai(self) -> str:
        try:
            completion = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Write a haiku about recursion in programming."}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error al llamar a OpenAI: {e}"


llm_service = LLMService()
