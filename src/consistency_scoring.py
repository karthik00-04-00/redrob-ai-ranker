from sentence_transformers import (
    util,
)

from src.embedding_ranker import (
    get_embedding,
)


def get_consistency_score(
    candidate,
):

    career_texts = []

    for role in candidate.get(
        "career_history",
        []
    ):

        career_texts.append(
            role.get(
                "description",
                ""
            )
        )

    career_text = " ".join(
        career_texts
    )

    skills = candidate.get(
        "skills",
        []
    )

    skill_names = []

    for skill in skills:

        skill_names.append(
            skill.get(
                "name",
                ""
            )
        )

    skills_text = " ".join(
        skill_names
    )

    if (
        not career_text.strip()
        or
        not skills_text.strip()
    ):
        return 0.0

    career_embedding = (
        get_embedding(
            career_text
        )
    )

    skills_embedding = (
        get_embedding(
            skills_text
        )
    )

    score = util.cos_sim(
        career_embedding,
        skills_embedding,
    )

    return float(
        score.item()
    )