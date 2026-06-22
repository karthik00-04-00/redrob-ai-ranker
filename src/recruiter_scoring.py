def calculate_recruiter_score(
    candidate_score,
    job_match_score,
):

    return (
        0.70 * candidate_score
        + 0.30 * job_match_score
    )