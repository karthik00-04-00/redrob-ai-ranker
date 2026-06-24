import json
import pandas as pd

from src.preprocess import (
    build_candidate_text,
)

from src.embedding_ranker import (
    get_embedding,
    get_semantic_similarity,
)

from src.consistency_scoring import (
    get_consistency_score,
)

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    job_text = f.read()

job_embedding = get_embedding(
    job_text
)

ranking_df = pd.read_csv(
    "outputs/job_aware_ranking.csv"
)

top100 = ranking_df.head(100)

candidate_ids = set(
    top100["candidate_id"]
)

candidate_lookup = {}

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    for line in f:

        candidate = json.loads(line)

        if (
            candidate["candidate_id"]
            in candidate_ids
        ):

            candidate_lookup[
                candidate["candidate_id"]
            ] = candidate

semantic_scores = []
consistency_scores = []

for candidate_id in candidate_ids:

    candidate = candidate_lookup[
        candidate_id
    ]

    candidate_text = (
        build_candidate_text(
            candidate
        )
    )

    semantic_score = (
        get_semantic_similarity(
            job_embedding,
            candidate_text,
        )
    )

    consistency_score = (
        get_consistency_score(
            candidate
        )
    )

    semantic_scores.append(
        semantic_score
    )

    consistency_scores.append(
        consistency_score
    )

print("\nSEMANTIC SCORE")
print(
    "mean:",
    round(
        pd.Series(
            semantic_scores
        ).mean(),
        4,
    )
)
print(
    "median:",
    round(
        pd.Series(
            semantic_scores
        ).median(),
        4,
    )
)
print(
    "max:",
    round(
        pd.Series(
            semantic_scores
        ).max(),
        4,
    )
)
print(
    "min:",
    round(
        pd.Series(
            semantic_scores
        ).min(),
        4,
    )
)

print("\nCONSISTENCY SCORE")
print(
    "mean:",
    round(
        pd.Series(
            consistency_scores
        ).mean(),
        4,
    )
)
print(
    "median:",
    round(
        pd.Series(
            consistency_scores
        ).median(),
        4,
    )
)
print(
    "max:",
    round(
        pd.Series(
            consistency_scores
        ).max(),
        4,
    )
)
print(
    "min:",
    round(
        pd.Series(
            consistency_scores
        ).min(),
        4,
    )
)