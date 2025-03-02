from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class GenerateQARequest(BaseModel):
    text: str
    num_questions: int

class QAEvaluationRequest(BaseModel):
    question: str
    correct_answer: str
    user_answer: str

@app.get("/")
async def root():
    return {"message": "S01🤓"}

@app.post("/generate-questions-from-text")
async def generate_questions_from_text(request: GenerateQARequest):
    # Placeholder questions about orbits
    sample_questions = [
        {
            "question": "What is the name of Earth's natural satellite that orbits around it?",
            "correct_answer": "The Moon"
        },
        {
            "question": "How long does it take for Earth to complete one orbit around the Sun?",
            "correct_answer": "365.25 days"
        },
        {
            "question": "Which planet has the most elliptical orbit in our solar system?",
            "correct_answer": "Mercury"
        },
        {
            "question": "What is the term for the point in a planet's orbit when it's closest to the Sun?",
            "correct_answer": "Perihelion"
        },
        {
            "question": "What keeps planets in orbit around the Sun?",
            "correct_answer": "Gravity"
        }
    ]
    return {
        "questions": sample_questions
    }

@app.post("/evaluate-question-answer")
async def evaluate_question_answer(request: QAEvaluationRequest):
    return {
        "score": 10,
        "feedback": "Your answer is correct!👍"
    }




