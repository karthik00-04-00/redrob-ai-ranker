import json
import pandas as pd

from src.preprocess import (
    build_candidate_text,
)

from src.feature_engineering import (
    get_relevance_score,
    get_behavior_score,
    get_intent_score,
    get_trust_score,
    get_candidate_profile,
)

from src.evidence_scoring import (
    get_evidence_score,
)

from src.scoring import (
    calculate_feature_score,
)

from src.job_understanding import (
    get_job_profile,
)

from src.job_matching import (
    get_job_match_score,
)

from src.recruiter_scoring import (
    calculate_recruiter_score,
)

with open(
    "sample_jd.txt",
    "r",
    encoding="utf-8",
) as f:

    job_text = f.read()

job_profile = get_job_profile(
    job_text
)

results = []

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:

    for line in f:

        candidate = json.loads(line)

        candidate_text = (
            build_candidate_text(
                candidate
            )
        )

        relevance_score = (
            get_relevance_score(
                candidate
            )
        )

        behavior_score = (
            get_behavior_score(
                candidate
            )
        )

        intent_score = (
            get_intent_score(
                candidate
            )
        )

        trust_score = (
            get_trust_score(
                candidate
            )
        )

        evidence_score = (
            get_evidence_score(
                candidate
            )
        )

        candidate_score = (
            calculate_feature_score(
                relevance_score,
                behavior_score,
                intent_score,
                trust_score,
                evidence_score,
            )
        )

        candidate_profile = (
            get_candidate_profile(
                candidate,
                candidate_text,
            )
        )

        job_match_score = (
            get_job_match_score(
                job_profile,
                candidate_profile,
            )
        )

        recruiter_score = (
            calculate_recruiter_score(
                candidate_score,
                job_match_score,
            )
        )

        results.append(
            {
                "candidate_id":
                    candidate["candidate_id"],

                "candidate_score":
                    round(
                        candidate_score,
                        2
                    ),

                "job_match_score":
                    round(
                        job_match_score,
                        2
                    ),

                "recruiter_score":
                    round(
                        recruiter_score,
                        2
                    ),
            }
        )

df = pd.DataFrame(results)

df = df.sort_values(
    "recruiter_score",
    ascending=False,
)

df["rank"] = range(
    1,
    len(df) + 1
)

print(
    "\nTOP 20 JOB-AWARE CANDIDATES\n"
)

print(
    df.head(20)
)

df.to_csv(
    "outputs/job_aware_ranking.csv",
    index=False,
)

print(
    "\nSaved outputs/job_aware_ranking.csv"
)