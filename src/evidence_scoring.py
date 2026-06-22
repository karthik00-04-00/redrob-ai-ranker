STRONG_EVIDENCE_PHRASES = [
    "trained and shipped",
    "ranking model",
    "ranking models",
    "learning-to-rank",
    "relevance labeling",
    "feature pipeline",
    "offline-online correlation",
    "retrieval",
    "recommendation system",
    "recommendation systems",
    "search product",
    "a/b test",
    "ab test",
]


def get_evidence_score(candidate):

    score = 0

    career_history = candidate.get(
        "career_history",
        []
    )

    for role in career_history:

        description = role.get(
            "description",
            ""
        ).lower()

        for phrase in (
            STRONG_EVIDENCE_PHRASES
        ):

            if phrase in description:
                score += 1

    return score