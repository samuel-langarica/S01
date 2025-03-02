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

@app.post("/generate-qa")
async def generate_qa(request: GenerateQARequest):
    # TODO: Implement QA generation logic
    return {
        "questions": []  # Will return list of generated QA pairs
    }

@app.post("/evaluate-qa")
async def evaluate_qa(request: QAEvaluationRequest):
    # TODO: Implement answer evaluation logic
    return {
        "is_correct": False,
        "feedback": ""
    }




