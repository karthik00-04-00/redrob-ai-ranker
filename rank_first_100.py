import json

from src.preprocess import build_candidate_text

from src.feature_engineering import (
    get_behavior_score,
    get_relevance_score,
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

    for i, line in enumerate(f):

        if i >= 100:
            break

        candidate = json.loads(line)

        candidate_text = build_candidate_text(
            candidate
        )

        relevance_score = (
            get_relevance_score(
                candidate
            )
        )

        behavior_score = (
            get_behavior_score(
                candidate
            )
        )

        intent_score = (
            get_intent_score(
                candidate
            )
        )

        trust_score = (
            get_trust_score(
                candidate
            )
        )

        evidence_score = (
            get_evidence_score(
                candidate
            )
        )

        final_score = (
            calculate_feature_score(
                relevance_score,
                behavior_score,
                intent_score,
                trust_score,
                evidence_score,
            )
        )

        results.append(
            {
                "candidate_id":
                    candidate["candidate_id"],

                "relevance_score":
                    round(
                        relevance_score,
                        2
                    ),

                "behavior_score":
                    round(
                        behavior_score,
                        2
                    ),

                "intent_score":
                    round(
                        intent_score,
                        2
                    ),

                "trust_score":
                    round(
                        trust_score,
                        2
                    ),

                "evidence_score":
                    round(
                        evidence_score,
                        2
                    ),

                "final_score":
                    round(
                        final_score,
                        2
                    ),
            }
        )

results.sort(
    key=lambda x: x["final_score"],
    reverse=True,
)

print("\nTOP 20 CANDIDATES\n")

for row in results[:20]:

    print(
        row["candidate_id"],
        "| relevance:",
        row["relevance_score"],
        "| behavior:",
        row["behavior_score"],
        "| intent:",
        row["intent_score"],
        "| trust:",
        row["trust_score"],
        "| evidence:",
        row["evidence_score"],
        "| final:",
        row["final_score"],
    )

    print(
    max(r["relevance_score"] for r in results)
)

print(
    max(r["behavior_score"] for r in results)
)

print(
    max(r["intent_score"] for r in results)
)

print(
    max(r["trust_score"] for r in results)
)

print(
    max(r["evidence_score"] for r in results)
)