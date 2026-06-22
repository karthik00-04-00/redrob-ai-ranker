# inspect_high_ai.py

import json

from src.preprocess import build_candidate_text
from src.feature_engineering import (
    get_ai_score,
    get_retrieval_score,
)

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for _ in range(100):

        candidate = json.loads(next(f))

        text = build_candidate_text(candidate)

        ai = get_ai_score(text)
        retrieval = get_retrieval_score(text)

        if ai >= 5 or retrieval >= 3:

            print("=" * 80)
            print(candidate["candidate_id"])
            print("AI:", ai)
            print("RETRIEVAL:", retrieval)

            for role in candidate["career_history"]:
                print("\nTITLE:", role["title"])
                print(role["description"][:300])