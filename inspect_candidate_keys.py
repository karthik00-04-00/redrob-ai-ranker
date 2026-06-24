import json

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    candidate = json.loads(
        next(f)
    )

for key in candidate.keys():

    print(key)