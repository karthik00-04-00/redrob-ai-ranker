def get_evidence_explanations(
    candidate,
    semantic_score,
    consistency_score,
    job_match_score,
):
    reasons = []

    profile = candidate.get(
        "profile", {}
    )

    headline = profile.get(
        "headline", ""
    ).lower()

    summary = profile.get(
        "summary", ""
    ).lower()

    text = headline + " " + summary

    for job in candidate.get(
        "career_history", []
    ):
        text += " "
        text += job.get(
            "description", ""
        ).lower()

    # Scores
    if semantic_score >= 0.65:
        reasons.append(
            "High semantic similarity with the job description"
        )

    if consistency_score >= 0.40:
        reasons.append(
            "Strong consistency between experience and profile evidence"
        )

    if job_match_score >= 6:
        reasons.append(
            "Strong match to job requirements"
        )

    # Profile evidence
    if (
        "learning-to-rank" in text
        or "ranking" in text
    ):
        reasons.append(
            "Experience building ranking systems"
        )

    if (
        "recommendation" in text
        or "recommender" in text
    ):
        reasons.append(
            "Experience building recommendation systems"
        )

    if (
        "semantic search" in text
        or "faiss" in text
        or "retrieval" in text
    ):
        reasons.append(
            "Experience with retrieval and semantic search systems"
        )

    if (
        "rag" in text
        or "pinecone" in text
        or "embedding" in text
    ):
        reasons.append(
            "Experience with embeddings and RAG pipelines"
        )

    if (
        "evaluation" in text
        or "eval framework" in text
    ):
        reasons.append(
            "Experience designing evaluation frameworks"
        )

    if (
        "mlflow" in text
        or "kubeflow" in text
        or "monitoring" in text
    ):
        reasons.append(
            "Experience operating production ML systems"
        )

    if len(reasons) == 0:
        reasons.append(
            "General profile strength"
        )

    return reasons