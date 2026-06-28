import json
import pandas as pd

from src.preprocess import (
    build_candidate_text,
)

from src.embedding_ranker import (
    get_embedding,
    get_semantic_similarities,
)

from src.consistency_scoring import (
    get_consistency_score,
)

# --------------------
# Load JD
# --------------------

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    job_text = f.read()

job_embedding = get_embedding(
    job_text
)

# --------------------
# Load ranking
# --------------------

ranking_df = pd.read_csv(
    "outputs/job_aware_ranking.csv"
)

# --------------------
# Load ALL candidates
# --------------------

candidate_lookup = {}
candidate_texts = []
candidate_ids = []

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

        candidate_lookup[
            candidate_id
        ] = candidate

        candidate_ids.append(
            candidate_id
        )

        candidate_texts.append(
            build_candidate_text(
                candidate
            )
        )

print(
    "Computing semantic similarity for all candidates..."
)

# --------------------
# Semantic scores
# --------------------

semantic_scores = (
    get_semantic_similarities(
        job_embedding,
        candidate_texts,
    )
)

semantic_dict = dict(
    zip(
        candidate_ids,
        semantic_scores,
    )
)

ranking_df[
    "semantic_score"
] = (
    ranking_df[
        "candidate_id"
    ].map(
        semantic_dict
    )
)

# --------------------
# Stage 1 Retrieval
# --------------------

ranking_df[
    "retrieval_score"
] = (
    0.70
    * ranking_df[
        "recruiter_score"
    ]
    +
    0.30
    * (
        ranking_df[
            "semantic_score"
        ]
        * 10
    )
)

top1000 = (
    ranking_df
    .sort_values(
        "retrieval_score",
        ascending=False,
    )
    .head(1000)
    .copy()
)

print(
    "Computing consistency scores..."
)

# --------------------
# Consistency
# --------------------

consistency_scores = {}

for candidate_id in top1000[
    "candidate_id"
]:

    candidate = (
        candidate_lookup[
            candidate_id
        ]
    )

    consistency_scores[
        candidate_id
    ] = (
        get_consistency_score(
            candidate
        )
    )

top1000[
    "consistency_score"
] = (
    top1000[
        "candidate_id"
    ].map(
        consistency_scores
    )
)

# --------------------
# Final Hybrid Score
# --------------------

top1000[
    "hybrid_score"
] = (
    0.70
    * top1000[
        "recruiter_score"
    ]
    +
    0.20
    * (
        top1000[
            "semantic_score"
        ]
        * 10
    )
    +
    0.10
    * (
        top1000[
            "consistency_score"
        ]
        * 10
    )
)

top100 = (
    top1000
    .sort_values(
        "hybrid_score",
        ascending=False,
    )
    .head(100)
    .copy()
)

top100["rank"] = range(
    1,
    len(top100) + 1
)

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