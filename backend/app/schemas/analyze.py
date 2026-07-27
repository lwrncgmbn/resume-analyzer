from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str


class AnalyzeResponse(BaseModel):
    match_score: int
    strengths: list[str]
    missing_skills: list[str]
    skill_breakdown: dict[str, dict[str, list[str]]]
    recommendations: list[str]
    summary: str