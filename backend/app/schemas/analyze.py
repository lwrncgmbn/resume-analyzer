from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    resume: str
    job_description: str


class AnalyzeResponse(BaseModel):
    match_score: int
    strengths: list[str]
    missing_skills: list[str]
    recommendations: list[str]
    summary: str