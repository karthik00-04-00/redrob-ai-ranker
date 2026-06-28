import pandas as pd

df = pd.read_csv(
    "outputs/hybrid_ranking_v3_full_semantic.csv"
)

submission = df[
    [
        "candidate_id",
        "rank",
    ]
]

submission.to_csv(
    "outputs/submission.csv",
    index=False,
)

submission.to_excel(
    "outputs/submission.xlsx",
    index=False,
)

print("Saved outputs/submission.csv")
print("Saved outputs/submission.xlsx")

print(submission.head(20))