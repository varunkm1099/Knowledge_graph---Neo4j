from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pipeline import answer_question

app = FastAPI(title="AI4I KG + LLM API")

# allow React dev server to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    cypher: str
    rows: list
    answer: str

@app.post("/ask", response_model=AnswerResponse)
def ask(req: QuestionRequest):
    result = answer_question(req.question)
    return AnswerResponse(**result)
