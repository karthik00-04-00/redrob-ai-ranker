import json
from pathlib import Path


INPUT_FILE = Path("data/raw/candidates.jsonl")


def build_candidate_text(candidate: dict) -> str:
    """
    Convert candidate JSON into a recruiter-friendly text document.
    """

    profile = candidate.get("profile", {})
    career_history = candidate.get("career_history", [])
    skills = candidate.get("skills", [])

    sections = []

    # Profile
    sections.append(
        f"""
CURRENT TITLE:
{profile.get('current_title', '')}

HEADLINE:
{profile.get('headline', '')}

SUMMARY:
{profile.get('summary', '')}

YEARS OF EXPERIENCE:
{profile.get('years_of_experience', '')}
"""
    )

    # Career History
    career_text = []

    for job in career_history:
        career_text.append(
            f"""
ROLE: {job.get('title', '')}
COMPANY: {job.get('company', '')}
DURATION_MONTHS: {job.get('duration_months', '')}

DESCRIPTION:
{job.get('description', '')}
"""
        )

    sections.append("\n".join(career_text))

    # Skills
    skill_names = [skill.get("name", "") for skill in skills]

    sections.append(
        f"""
SKILLS:
{', '.join(skill_names)}
"""
    )

    return "\n".join(sections).strip()


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:

        first_candidate = json.loads(next(f))

        candidate_text = build_candidate_text(first_candidate)

        print(candidate_text[:5000])


if __name__ == "__main__":
    main()