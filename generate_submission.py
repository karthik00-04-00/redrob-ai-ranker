import pandas as pd

df = pd.read_csv(
    "outputs/job_aware_ranking.csv"
)

submission = df[
    [
        "candidate_id",
        "rank",
        "recruiter_score",
    ]
]

submission.to_csv(
    "outputs/submission.csv",
    index=False,
)

print(
    "Saved outputs/submission.csv"
)

print(
    submission.head(20)
)