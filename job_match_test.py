import json

from src.preprocess import (
    build_candidate_text,
)

from src.job_understanding import (
    get_job_profile,
)

from src.job_matching import (
    get_job_match_score,
)

from src.feature_engineering import (
    get_candidate_profile,
)

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    job_text = f.read()

job_profile = get_job_profile(
    job_text
)

candidate = None

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    for line in f:

        row = json.loads(line)

        if (
            row["candidate_id"]
            == "CAND_0000031"
        ):
            candidate = row
            break

candidate_text = (
    build_candidate_text(
        candidate
    )
)

candidate_profile = (
    get_candidate_profile(
        candidate,
        candidate_text,
    )
)

match_score = (
    get_job_match_score(
        job_profile,
        candidate_profile,
    )
)

print(
    "Job Profile:"
)

print(job_profile)

print(
    "\nCandidate Profile:"
)

print(candidate_profile)

print(
    "\nMatch Score:"
)

print(match_score)