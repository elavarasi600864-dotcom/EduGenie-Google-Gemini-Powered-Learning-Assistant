from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from learning_path import get_learning_recommendations
from fastapi.templating import Jinja2Templates

from schemas import (
    QARequest,
    ExplainRequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
    QuizResponse,
    LearningPathResponse,
)

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "EduGenie is running"
    }


@app.post("/qa")
async def qa(payload: QARequest):
    try:
        answer = answer_question(payload.question)

        return {
            "success": True,
            "answer": answer
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.post("/explain")
async def explain(payload: ExplainRequest):
    try:
        explanation = explain_topic(
            payload.topic,
            payload.level
        )

        return {
            "success": True,
            "explanation": explanation
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.post("/quiz", response_model=QuizResponse)
async def quiz(payload: QuizRequest):
    return generate_quiz(
        payload.text,
        payload.question_count
    )


@app.post("/summarize")
async def summarize(payload: SummaryRequest):
    try:
        summary = summarize_text(
            payload.text,
            payload.max_words
        )

        return {
            "success": True,
            "summary": summary
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.post(
    "/learn/recommendations",
    response_model=LearningPathResponse
)
async def learning_recommendations(
    payload: LearningPathRequest
):
    return get_learning_recommendations(
        payload.topic,
        payload.level,
        payload.goal
    )