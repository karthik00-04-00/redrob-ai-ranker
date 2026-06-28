import pandas as pd

old = pd.read_csv("outputs/job_aware_ranking.csv")
new = pd.read_csv("outputs/hybrid_ranking_v2.csv")

old = old[["candidate_id", "rank"]].rename(
    columns={"rank": "old_rank"}
)

new = new[
    [
        "candidate_id",
        "rank",
        "semantic_score",
        "consistency_score",
        "hybrid_score",
    ]
].rename(
    columns={"rank": "new_rank"}
)

comparison = old.merge(
    new,
    on="candidate_id",
    how="inner"
)

comparison["rank_change"] = (
    comparison["old_rank"] - comparison["new_rank"]
)

positive_movers = comparison.sort_values(
    "rank_change",
    ascending=False
).head(20)

negative_movers = comparison.sort_values(
    "rank_change",
    ascending=True
).head(20)

print("\n" + "="*80)
print("TOP POSITIVE MOVERS")
print("="*80)

print(
    positive_movers[
        [
            "candidate_id",
            "old_rank",
            "new_rank",
            "rank_change",
            "semantic_score",
            "consistency_score",
            "hybrid_score"
        ]
    ]
)

print("\n" + "="*80)
print("TOP NEGATIVE MOVERS")
print("="*80)

print(
    negative_movers[
        [
            "candidate_id",
            "old_rank",
            "new_rank",
            "rank_change",
            "semantic_score",
            "consistency_score",
            "hybrid_score"
        ]
    ]
)

# Entered Top 100
entered_top100 = comparison[
    (comparison["old_rank"] > 100)
    & (comparison["new_rank"] <= 100)
]

# Left Top 100
left_top100 = comparison[
    (comparison["old_rank"] <= 100)
    & (comparison["new_rank"] > 100)
]

print("\nEntered Top 100:", len(entered_top100))
print("Left Top 100:", len(left_top100))

comparison.to_csv(
    "outputs/ranking_comparison.csv",
    index=False
)

print("\nSaved: outputs/ranking_comparison.csv")    