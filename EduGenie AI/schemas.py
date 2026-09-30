from pydantic import BaseModel, Field
from typing import List, Any


class QARequest(BaseModel):
    question: str


class ExplainRequest(BaseModel):
    topic: str
    level: str = "beginner"


class QuizRequest(BaseModel):
    text: str
    question_count: int = 5


class SummaryRequest(BaseModel):
    text: str
    max_words: int = 150


class LearningPathRequest(BaseModel):
    topic: str
    level: str = "beginner"
    goal: str = ""


class QuizResponse(BaseModel):
    questions: List[Any] = []


class LearningPathResponse(BaseModel):
    recommendations: List[Any] = []