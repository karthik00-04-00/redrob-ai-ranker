import json

TARGET_ID = "CAND_0000031"

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("=" * 80)
            print("HEADLINE")
            print(candidate["profile"]["headline"])

            print("\nCURRENT TITLE")
            print(candidate["profile"]["current_title"])

            print("\nSUMMARY")
            print(candidate["profile"]["summary"])

            print("\nCAREER HISTORY")

            for role in candidate["career_history"]:
                print("\n" + "-" * 50)
                print("TITLE:", role["title"])
                print("DESCRIPTION:")
                print(role["description"])

            break