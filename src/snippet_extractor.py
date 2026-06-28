def extract_snippets(candidate):
    snippets = []

    for job in candidate.get(
        "career_history", []
    ):
        desc = job.get(
            "description",
            ""
        ).strip()

        if not desc:
            continue

        sentences = desc.split(".")

        for s in sentences:
            s = s.strip()

            if len(s) < 30:
                continue

            keywords = [
                "ranking",
                "recommendation",
                "semantic search",
                "faiss",
                "rag",
                "pinecone",
                "embedding",
                "evaluation",
                "retrieval",
            ]

            if any(
                k in s.lower()
                for k in keywords
            ):
                snippets.append(s)

    return snippets[:3]