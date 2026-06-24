import json
import pandas as pd

from src.preprocess import (
    build_candidate_text,
)

from src.embedding_ranker import (
    get_embedding,
    get_semantic_similarity,
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

# Load Top Candidates

ranking_df = pd.read_csv(
    "outputs/job_aware_ranking.csv"
)

top100 = ranking_df.head(100)

candidate_ids = set(
    top100["candidate_id"]
)

# Load Candidate Records

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

        if (
            candidate_id
            in candidate_ids
        ):

            candidate_lookup[
                candidate_id
            ] = candidate

results = []

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

    results.append(
        {
            "candidate_id":
                candidate_id,

            "semantic_score":
                round(
                    semantic_score,
                    4
                ),
        }
    )

semantic_df = pd.DataFrame(
    results
)

semantic_df = (
    semantic_df.sort_values(
        "semantic_score",
        ascending=False,
    )
)

semantic_df["rank"] = range(
    1,
    len(semantic_df) + 1
)

semantic_df.to_csv(
    "outputs/semantic_ranking.csv",
    index=False,
)

print(
    semantic_df.head(20)
)

print(
    "\nSaved outputs/semantic_ranking.csv"
)