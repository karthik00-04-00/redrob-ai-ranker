import json

from src.evidence_scoring import (
    get_evidence_score
)

TARGETS = [
    "CAND_0000031",
    "CAND_0000100",
]

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        if (
            candidate["candidate_id"]
            in TARGETS
        ):

            print(
                candidate["candidate_id"],
                get_evidence_score(
                    candidate
                )
            )