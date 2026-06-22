import json

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

        relevance_score = (
            get_relevance_score(candidate)
        )

        behavior_score = (
            get_behavior_score(candidate)
        )

        intent_score = (
            get_intent_score(candidate)
        )

        trust_score = (
            get_trust_score(candidate)
        )

        evidence_score = (
            get_evidence_score(candidate)
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

                "headline":
                    candidate.get(
                        "headline",
                        ""
                    ),

                "relevance":
                    round(relevance_score, 2),

                "behavior":
                    round(behavior_score, 2),

                "intent":
                    round(intent_score, 2),

                "trust":
                    round(trust_score, 2),

                "evidence":
                    round(evidence_score, 2),

                "final":
                    round(final_score, 2),
            }
        )

results.sort(
    key=lambda x: x["final"],
    reverse=True,
)

print("\nTOP 20 CANDIDATES\n")

for row in results[:20]:

    print("=" * 80)

    print(
        row["candidate_id"]
    )

    print(
        row["headline"]
    )

    print(
        "relevance:",
        row["relevance"]
    )

    print(
        "behavior:",
        row["behavior"]
    )

    print(
        "intent:",
        row["intent"]
    )

    print(
        "trust:",
        row["trust"]
    )

    print(
        "evidence:",
        row["evidence"]
    )

    print(
        "final:",
        row["final"]
    )