from app.schemas.analyze import AnalyzeResponse


def analyze_resume(resume: str, job_description: str):

    return AnalyzeResponse(
        match_score=85,
        strengths=[
            "React",
            "JavaScript",
            "HTML/CSS",
            "HubSpot CMS experience"
        ],
        missing_skills=[
            "Docker",
            "AWS",
            "TypeScript"
        ],
        recommendations=[
            "Add measurable achievements to your resume.",
            "Include cloud deployment experience.",
            "Highlight backend or DevOps projects."
        ],
        summary=(
            "The candidate has strong frontend development "
            "experience but lacks some cloud and infrastructure skills."
        )
    )