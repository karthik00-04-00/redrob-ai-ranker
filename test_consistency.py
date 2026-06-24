import json

from src.consistency_scoring import (
    get_consistency_score,
)

candidate_ids = [
    "CAND_0000031",
    "CAND_0030953",
    "CAND_0030348",
    "CAND_0000082",
]

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    candidates = {
        row["candidate_id"]: row
        for row in (
            json.loads(line)
            for line in f
        )
        if row["candidate_id"]
        in candidate_ids
    }

for candidate_id in candidate_ids:

    score = (
        get_consistency_score(
            candidates[
                candidate_id
            ]
        )
    )

    print(
        candidate_id,
        "->",
        round(score, 4)
    )