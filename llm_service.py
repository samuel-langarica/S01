from openai import OpenAI
import json


class LLMService:
    def __init__(self):
        self.openai_client = OpenAI()  # No pasamos la API key aquí

    async def process_document(self, text: str) -> dict:
        """
        Processes a document by extracting structured bits of information.

        Args:
            text (str): The full text of the document.

        Returns:
            dict: A structured JSON-like dictionary containing extracted information.
        """
        try:
            # Define the system message for instructing the AI model
            system_prompt = (
                "You are an AI that extracts structured knowledge from documents. "
                "Break the text into ordered 'bits' that contain key concepts, events, ideas, definitions, and quotes. "
                "Ensure that these bits, when combined, reconstruct the full document in order."
                "\n\nEach extracted bit must include:"
                "- `type`: The category of information (choose from: definition, idea, event, quote, summary, formula, example, explanation)."
                "- If the type is not in the provided list, use a reasonable type but mark it as 'custom' in metadata."
                "- `content`: The actual extracted information."
                "- `source`: A reference to where this bit appears in the original document."
                "- `metadata`: Additional details (e.g., related concepts, author, date, or formula variables)."
                "\n\nOutput the response in valid JSON format."
            )

            # User input (document text)
            user_prompt = f"Process the following document:\n\n{text}"

            # Call OpenAI API
            response = self.openai_client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,  
                max_tokens=4096  
            )

            # Extract the response text
            response_text = response.choices[0].message.content.strip()

            # Convert response to JSON
            structured_data = json.loads(response_text)

            # Validate and correct bit types
            for bit in structured_data.get("bits", []):
                detected_type = bit.get("type", "").lower()
                valid_type = BitType.get_valid_type(detected_type)
                if valid_type == BitType.UNKNOWN.value:
                    bit["metadata"]["custom_type"] = detected_type  # Store original unknown type
                bit["type"] = valid_type  # Use enum-based category

            return structured_data

        except json.JSONDecodeError:
            return {"error": "Failed to parse the AI response as JSON."}

        except Exception as e:
            return {"error": f"Unexpected error while processing document: {str(e)}"}


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
