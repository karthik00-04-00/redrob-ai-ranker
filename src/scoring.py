def calculate_feature_score(
    relevance_score,
    behavior_score,
    intent_score,
    trust_score,
    evidence_score,
):
    return (
        0.35 * relevance_score
        + 0.25 * behavior_score
        + 0.20 * intent_score
        + 0.10 * trust_score
        + 0.10 * evidence_score
    )