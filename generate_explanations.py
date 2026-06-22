import pandas as pd

from src.explainability import (
    get_explanations,
)

df = pd.read_csv(
    "outputs/job_aware_ranking.csv"
)

top20 = df.head(20)

with open(
    "outputs/top20_explanations.txt",
    "w",
    encoding="utf-8",
) as f:

    for _, row in top20.iterrows():

        reasons = (
            get_explanations(
                relevance=10,
                behavior=10,
                intent=2,
                trust=3,
                evidence=5,
                job_match=row[
                    "job_match_score"
                ],
            )
        )

        f.write(
            "=" * 60 + "\n"
        )

        f.write(
            f"Candidate: {row['candidate_id']}\n"
        )

        f.write(
            f"Rank: {row['rank']}\n"
        )

        f.write(
            f"Recruiter Score: "
            f"{row['recruiter_score']}\n\n"
        )

        f.write(
            "Reasons:\n"
        )

        for reason in reasons:

            f.write(
                f"- {reason}\n"
            )

        f.write("\n")

print(
    "Saved outputs/top20_explanations.txt"
)