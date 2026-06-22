import json

TARGET_ID = "CAND_0000082"

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        if (
            candidate["candidate_id"]
            == TARGET_ID
        ):

            print("=" * 80)

            print(
                candidate["profile"]
            )

            print("\nSKILLS")
            print(
                candidate["skills"]
            )

            print("\nCAREER")
            print(
                candidate[
                    "career_history"
                ]
            )

            break