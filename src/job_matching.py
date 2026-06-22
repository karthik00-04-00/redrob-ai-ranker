def get_job_match_score(
    job_profile,
    candidate_profile,
):

    score = 0

    score += (
        job_profile["ai"]
        * candidate_profile["ai"]
    )

    score += (
        job_profile["retrieval"]
        * candidate_profile["retrieval"]
    )

    score += (
        job_profile["data"]
        * candidate_profile["career_data"]
    )

    score += (
        job_profile["mlops"]
        * candidate_profile["mlops"]
    )

    return score / 20