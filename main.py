import json

from src.preprocess import build_candidate_text

from src.feature_engineering import (
    get_ai_score,
    get_retrieval_score,
    get_mlops_score,
    get_behavior_score,
    get_career_ai_score,
    get_career_data_score,
    get_career_retrieval_score,
    get_relevance_score,
)

from src.scoring import calculate_feature_score


candidate = None

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:
        row = json.loads(line)

        if row["candidate_id"] == "CAND_0000031":
            candidate = row
            break


if candidate is None:
    raise ValueError(
        "Candidate CAND_0000031 not found"
    )


candidate_text = build_candidate_text(
    candidate
)

ai_score = get_ai_score(
    candidate_text
)

retrieval_score = get_retrieval_score(
    candidate_text
)

mlops_score = get_mlops_score(
    candidate_text
)

behavior_score = get_behavior_score(
    candidate
)

career_ai_score = get_career_ai_score(
    candidate
)

career_data_score = get_career_data_score(
    candidate
)

career_retrieval_score = (
    get_career_retrieval_score(
        candidate
    )
)

relevance_score = get_relevance_score(
    candidate
)

final_score = calculate_feature_score(
    ai_score,
    retrieval_score,
    mlops_score,
    behavior_score,
)

print("=" * 60)
print(
    "CANDIDATE:",
    candidate["candidate_id"]
)
print("=" * 60)

print(
    "AI SCORE:",
    ai_score
)

print(
    "RETRIEVAL SCORE:",
    retrieval_score
)

print(
    "MLOPS SCORE:",
    mlops_score
)

print(
    "BEHAVIOR SCORE:",
    behavior_score
)

print(
    "CAREER AI:",
    career_ai_score
)

print(
    "CAREER DATA:",
    career_data_score
)

print(
    "CAREER RETRIEVAL:",
    career_retrieval_score
)

print(
    "RELEVANCE SCORE:",
    relevance_score
)

print(
    "FINAL SCORE:",
    final_score
)