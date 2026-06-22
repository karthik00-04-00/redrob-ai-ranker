# inspect_signals.py

import json

with open("data/raw/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

print("\n".join(candidate["redrob_signals"].keys()))