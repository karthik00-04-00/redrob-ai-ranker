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

score = (
    get_semantic_similarity(
        job_text,
        candidate_text,
    )
)

print(
    "Semantic Score:",
    score
)