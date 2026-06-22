# inspect_candidates.py

import json

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for i in range(10):
        candidate = json.loads(next(f))

        print("=" * 80)
        print(candidate["candidate_id"])

        for role in candidate["career_history"]:
            print("\nTITLE:", role["title"])
            print("DURATION:", role["duration_months"])
            print("DESCRIPTION:")
            print(role["description"][:500])