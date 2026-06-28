import json

DATASET_PATH = "data/raw/candidates.jsonl"

candidate_ids = [
    "CAND_0041568",
    "CAND_0027801"
]

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] in candidate_ids:

            print("\n" + "=" * 100)
            print("CANDIDATE ID:", candidate["candidate_id"])
            print("=" * 100)

            profile = candidate.get("profile", {})

            print("\nHEADLINE:")
            print(profile.get("headline", "N/A"))

            print("\nSUMMARY:")
            print(profile.get("summary", "N/A"))

            print("\nSKILLS:")
            print(profile.get("skills", []))

            print("\nCAREER HISTORY:")
            for job in candidate.get("career_history", []):
                print(job)

            print("\nEDUCATION:")
            for edu in candidate.get("education", []):
                print(edu)