import json

from src.preprocess import (
    build_candidate_text,
)

from src.embedding_ranker import (
    get_semantic_similarity,
)

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    job_text = f.read()

candidate_ids = [
    "CAND_0000031",
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

    candidate = candidates[
        candidate_id
    ]

    candidate_text = (
        build_candidate_text(
            candidate
        )
    )

    score = (
        get_semantic_similarity(
            job_text,
            candidate_text,
        )
    )

    print(
        candidate_id,
        "->",
        round(score, 4),
    )