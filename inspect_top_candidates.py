import json

TARGETS = [
    "CAND_0000031",
    "CAND_0000100",
    "CAND_0000026",
    "CAND_0000042",
    "CAND_0000069",
]

with open(
    "data/raw/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in TARGETS:

            print("\n" + "=" * 80)

            print(
                "CANDIDATE:",
                candidate["candidate_id"]
            )

            print("=" * 80)

            print(
                "HEADLINE:"
            )
            print(
                candidate["profile"].get(
                    "headline",
                    ""
                )
            )

            print(
                "\nCURRENT TITLE:"
            )
            print(
                candidate["profile"].get(
                    "current_title",
                    ""
                )
            )

            print(
                "\nYEARS OF EXPERIENCE:"
            )
            print(
                candidate["profile"].get(
                    "years_of_experience",
                    ""
                )
            )

            print(
                "\nSUMMARY:"
            )
            print(
                candidate["profile"].get(
                    "summary",
                    ""
                )
            )

            print(
                "\nCAREER HISTORY:"
            )

            for role in candidate.get(
                "career_history",
                []
            ):

                print(
                    "\nTITLE:",
                    role.get(
                        "title",
                        ""
                    )
                )

                print(
                    "DESCRIPTION:"
                )

                print(
                    role.get(
                        "description",
                        ""
                    )[:500]
                )