import json
import sys

candidate_id = sys.argv[1]

candidate = None

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        row = json.loads(line)

        if row["candidate_id"] == candidate_id:
            candidate = row
            break

if candidate is None:
    print("Candidate not found")
    exit()

print("=" * 80)
print("ID:", candidate["candidate_id"])
print("=" * 80)

print("\nHEADLINE")
print(candidate.get("headline", ""))

print("\nCURRENT TITLE")
print(candidate.get("current_title", ""))

print("\nSUMMARY")
print(candidate.get("summary", ""))

print("\nCAREER HISTORY")

for role in candidate.get(
    "career_history",
    []
):
    print("\n" + "-" * 50)

    print(
        "TITLE:",
        role.get("title", "")
    )

    print(
        "DESCRIPTION:"
    )

    print(
        role.get(
            "description",
            ""
        )
    )