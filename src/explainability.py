def get_explanations(
    relevance,
    behavior,
    intent,
    trust,
    evidence,
    job_match,
):

    reasons = []

    if relevance >= 10:
        reasons.append(
            "Strong retrieval/ranking/recommendation experience"
        )

    if evidence >= 5:
        reasons.append(
            "Demonstrated production ML impact"
        )

    if behavior >= 10:
        reasons.append(
            "Strong recruiter engagement signals"
        )

    if intent >= 2:
        reasons.append(
            "High candidate responsiveness"
        )

    if trust >= 3:
        reasons.append(
            "Highly verified profile"
        )

    if job_match >= 6:
        reasons.append(
            "Strong match to job requirements"
        )

    if len(reasons) == 0:
        reasons.append(
            "General profile strength"
        )

    return reasons