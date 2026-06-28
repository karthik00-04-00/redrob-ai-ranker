import json
import pandas as pd

ranking = pd.read_csv(
    "outputs/hybrid_ranking_v2.csv"
)

top10 = ranking.head(10)

candidate_ids = set(
    top10["candidate_id"]
)

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    for line in f:
        candidate = json.loads(line)

        if (
            candidate["candidate_id"]
            in candidate_ids
        ):

            print("\n" + "=" * 100)
            print(
                candidate["candidate_id"]
            )
            print("=" * 100)

            profile = candidate.get(
                "profile",
                {}
            )

            print(
                "Headline:",
                profile.get(
                    "headline",
                    ""
                )
            )

            print(
                "\nSummary:"
            )

            print(
                profile.get(
                    "summary",
                    ""
                )
            )

            print(
                "\nCareer:"
            )

            for job in candidate.get(
                "career_history",
                []
            ):
                print(
                    "-",
                    job["title"],
                    "|",
                    job["company"]
                )