from fastapi import APIRouter

from app.schemas.analyze import AnalyzeRequest
from app.services.gemini_service import analyze_resume

router = APIRouter(
    prefix="/analyze",
    tags=["Analyze"]
)


@router.post("/")
async def analyze(data: AnalyzeRequest):
    return analyze_resume(
        data.resume_text,
        data.job_description
    )