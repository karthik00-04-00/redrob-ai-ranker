import pandas as pd

df = pd.read_csv(
    "outputs/ranking_v1.csv"
)

features = [
    "relevance_score",
    "behavior_score",
    "intent_score",
    "trust_score",
    "evidence_score",
]

for feature in features:

    print("\n", feature)

    print(
        "mean:",
        df[feature].mean()
    )

    print(
        "median:",
        df[feature].median()
    )

    print(
        "max:",
        df[feature].max()
    )

    print(
        "min:",
        df[feature].min()
    )