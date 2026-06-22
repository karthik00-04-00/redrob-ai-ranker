import json

from src.feature_engineering import (
    get_career_ai_score,
    get_career_data_score,
    get_career_retrieval_score,
)

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for _ in range(20):

        candidate = json.loads(next(f))

        print(
            candidate["candidate_id"],
            "| AI:",
            get_career_ai_score(candidate),
            "| DATA:",
            get_career_data_score(candidate),
            "| RETRIEVAL:",
            get_career_retrieval_score(candidate),
        )