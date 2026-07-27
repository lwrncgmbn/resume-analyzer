# from app.schemas.analyze import AnalyzeResponse


# def analyze_resume(resume: str, job_description: str):

#     return AnalyzeResponse(
#         match_score=85,
#         strengths=[
#             "React",
#             "JavaScript",
#             "HTML/CSS",
#             "HubSpot CMS experience"
#         ],
#         missing_skills=[
#             "Docker",
#             "AWS",
#             "TypeScript"
#         ],
#         recommendations=[
#             "Add measurable achievements to your resume.",
#             "Include cloud deployment experience.",
#             "Highlight backend or DevOps projects."
#         ],
#         summary=(
#             "The candidate has strong frontend development "
#             "experience but lacks some cloud and infrastructure skills."
#         )
#     )

from app.schemas.analyze import AnalyzeResponse

# from app.data.skills import SKILLS
from app.data.skills import SKILLS, SKILL_INFO


def analyze_resume(resume: str, job_description: str):

    resume = resume.lower()
    job_description = job_description.lower()

    strengths = set()
    missing_skills = set()

    skill_breakdown = {}

    earned_points = 0
    possible_points = 0

    for category, skills in SKILLS.items():

        matched = []
        missing = []

        for skill in skills:

            aliases = SKILL_INFO[skill]["aliases"]

            job_has_skill = any(
                alias in job_description
                for alias in aliases
            )

            resume_has_skill = any(
                alias in resume
                for alias in aliases
            )

            # if skill in job_description:
            if job_has_skill:

                weight = SKILL_INFO[skill]["weight"]
                possible_points += weight

                if resume_has_skill:
                    earned_points += weight
                    strengths.add(SKILL_INFO[skill]["display"])
                    matched.append(SKILL_INFO[skill]["display"])
                else:
                    missing_skills.add(SKILL_INFO[skill]["display"])
                    missing.append(SKILL_INFO[skill]["display"])

        skill_breakdown[category] = {
            "matched": matched,
            "missing": missing
        }

    if strengths or missing_skills:
        match_score = (
            int((earned_points / possible_points) * 100)
            if possible_points
            else 0
        )
    else:
        match_score = 0

    recommendations = []

    if missing_skills:
        recommendations.append(
            f"Consider learning: {', '.join(missing_skills)}."
        )

    if match_score < 50:
        recommendations.append(
            "Your resume needs significant improvement for this role."
        )
    elif match_score < 80:
        recommendations.append(
            "Your resume is a decent match, but adding the missing skills would strengthen your application."
        )
    else:
        recommendations.append(
            "Your resume is a strong match for this position."
        )

    # Convert sets to sorted lists
    strengths = sorted(list(strengths))
    missing_skills = sorted(list(missing_skills))

    summary = (
        f"The resume matches approximately {match_score}% "
        f"of the required skills. "
        f"It demonstrates strengths in {', '.join(strengths) if strengths else 'no matching skills'}, "
        f"while missing {', '.join(missing_skills) if missing_skills else 'no required skills'}."
    )
    
    return AnalyzeResponse(
        match_score=match_score,
        strengths=strengths,
        missing_skills=missing_skills,
        skill_breakdown=skill_breakdown,
        recommendations=recommendations,
        summary=summary
    )