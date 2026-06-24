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

# Load JD

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    job_text = f.read()

job_embedding = get_embedding(
    job_text
)

# Load ranking

ranking_df = pd.read_csv(
    "outputs/job_aware_ranking.csv"
)

top100 = ranking_df.head(100).copy()

candidate_ids = set(
    top100["candidate_id"]
)

# Load candidates

candidate_lookup = {}

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    for line in f:

        candidate = json.loads(
            line
        )

        candidate_id = (
            candidate["candidate_id"]
        )

        if candidate_id in candidate_ids:

            candidate_lookup[
                candidate_id
            ] = candidate

semantic_scores = {}
consistency_scores = {}

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

    semantic_scores[
        candidate_id
    ] = semantic_score

    consistency_scores[
        candidate_id
    ] = consistency_score

# Add features

top100["semantic_score"] = (
    top100["candidate_id"]
    .map(semantic_scores)
)

top100["consistency_score"] = (
    top100["candidate_id"]
    .map(consistency_scores)
)

# V0.2 Hybrid Score

top100["hybrid_score"] = (
    0.70
    * top100["recruiter_score"]
    +
    0.20
    * (
        top100["semantic_score"]
        * 10
    )
    +
    0.10
    * (
        top100["consistency_score"]
        * 10
    )
)

# Sort

top100 = top100.sort_values(
    "hybrid_score",
    ascending=False,
)

top100["rank"] = range(
    1,
    len(top100) + 1
)

# Save

top100.to_csv(
    "outputs/hybrid_ranking_v2.csv",
    index=False,
)

print(
    top100[
        [
            "candidate_id",
            "recruiter_score",
            "semantic_score",
            "consistency_score",
            "hybrid_score",
            "rank",
        ]
    ].head(20)
)

print(
    "\nSaved outputs/hybrid_ranking_v2.csv"
)