import json
import pandas as pd

from src.explainability import (
    get_evidence_explanations,
)

from src.evidence_extractor import (
    extract_evidence,
)

from src.snippet_extractor import (
    extract_snippets,
)

# Load Hybrid Ranking results
df = pd.read_csv(
    "outputs/hybrid_ranking_v2.csv"
)

top20 = df.head(20)

# Load all candidates
candidate_map = {}

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8",
) as f:
    for line in f:
        candidate = json.loads(line)
        candidate_map[
            candidate["candidate_id"]
        ] = candidate

# Generate explanations
with open(
    "outputs/top20_explanations.txt",
    "w",
    encoding="utf-8",
) as f:

    for _, row in top20.iterrows():

        candidate = candidate_map[
            row["candidate_id"]
        ]

        reasons = (
            get_evidence_explanations(
                candidate,
                row["semantic_score"],
                row["consistency_score"],
                row["job_match_score"],
            )
        )

        # Build text for evidence extraction
        text = ""

        profile = candidate.get(
            "profile", {}
        )

        text += (
            profile.get(
                "headline", ""
            )
            + " "
        )

        text += (
            profile.get(
                "summary", ""
            )
            + " "
        )

        for job in candidate.get(
            "career_history", []
        ):
            text += (
                job.get(
                    "description", ""
                )
                + " "
            )

        evidence = extract_evidence(
            text
        )

        snippets = extract_snippets(
            candidate
        )

        # Write output
        f.write(
            "=" * 60 + "\n"
        )

        f.write(
            f"Candidate: {row['candidate_id']}\n"
        )

        f.write(
            f"Rank: {row['rank']}\n"
        )

        f.write(
            f"Hybrid Score: "
            f"{row['hybrid_score']:.4f}\n"
        )

        f.write(
            f"Semantic Score: "
            f"{row['semantic_score']:.4f}\n"
        )

        f.write(
            f"Consistency Score: "
            f"{row['consistency_score']:.4f}\n"
        )

        f.write(
            f"Job Match Score: "
            f"{row['job_match_score']:.4f}\n\n"
        )

        # Reasons
        f.write(
            "Reasons:\n"
        )

        for reason in reasons:
            f.write(
                f"- {reason}\n"
            )

        # Evidence
        if evidence:
            f.write(
                "\nEvidence:\n"
            )

            for item in evidence:
                f.write(
                    f"- {item}\n"
                )

        # Profile snippets
        if snippets:
            f.write(
                "\nProfile Evidence:\n"
            )

            for snippet in snippets:
                f.write(
                    f'- "{snippet}"\n'
                )

        f.write("\n")

print(
    "Saved outputs/top20_explanations.txt"
)