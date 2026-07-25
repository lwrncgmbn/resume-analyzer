from openai import OpenAI

from app.config.settings import settings
from app.schemas.analyze import AnalyzeResponse

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def analyze_resume(resume: str, job_description: str) -> AnalyzeResponse:

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the resume against the job description.

Resume:
{resume}

Job Description:
{job_description}

Return:
- match_score (0-100)
- strengths
- missing_skills
- recommendations
- summary
"""

    response = client.responses.parse(
        model=settings.OPENAI_MODEL,
        input=prompt,
        text_format=AnalyzeResponse,
    )

    return response.output_parsed