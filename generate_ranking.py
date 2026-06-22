import json
import pandas as pd

from src.feature_engineering import (
    get_relevance_score,
    get_behavior_score,
    get_intent_score,
    get_trust_score,
)

from src.evidence_scoring import (
    get_evidence_score,
)

from src.scoring import (
    calculate_feature_score,
)

results = []

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        relevance_score = get_relevance_score(candidate)
        behavior_score = get_behavior_score(candidate)
        intent_score = get_intent_score(candidate)
        trust_score = get_trust_score(candidate)
        evidence_score = get_evidence_score(candidate)

        final_score = calculate_feature_score(
            relevance_score,
            behavior_score,
            intent_score,
            trust_score,
            evidence_score,
        )

        results.append(
            {
                "candidate_id":
                    candidate["candidate_id"],

                "relevance_score":
                    round(relevance_score, 2),

                "behavior_score":
                    round(behavior_score, 2),

                "intent_score":
                    round(intent_score, 2),

                "trust_score":
                    round(trust_score, 2),

                "evidence_score":
                    round(evidence_score, 2),

                "final_score":
                    round(final_score, 2),
            }
        )

df = pd.DataFrame(results)

df = df.sort_values(
    "final_score",
    ascending=False,
)

df["rank"] = (
    range(1, len(df) + 1)
)

df.to_csv(
    "outputs/ranking_v1.csv",
    index=False,
)

print(
    "Saved:",
    len(df),
    "candidates"
)

print(
    df.head(20)
)