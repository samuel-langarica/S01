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
    # TODO: Implement QA generation logic
    return {
        "questions": []  # Will return list of generated QA pairs
    }

@app.post("/evaluate-question-answer")
async def evaluate_question_answer(request: QAEvaluationRequest):
    # TODO: Implement answer evaluation logic
    return {
        "score": 0,
        "feedback": ""
    }




