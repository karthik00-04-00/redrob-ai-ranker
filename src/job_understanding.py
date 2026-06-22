AI_KEYWORDS = [
    "machine learning",
    "deep learning",
    "llm",
    "nlp",
    "transformer",
]

RETRIEVAL_KEYWORDS = [
    "retrieval",
    "search",
    "ranking",
    "recommendation",
    "embedding",
    "vector",
]

DATA_KEYWORDS = [
    "spark",
    "etl",
    "airflow",
    "kafka",
    "data pipeline",
]

MLOPS_KEYWORDS = [
    "mlops",
    "deployment",
    "monitoring",
    "docker",
    "kubernetes",
]


def count_matches(text, keywords):

    text = text.lower()

    return sum(
        text.count(keyword.lower())
        for keyword in keywords
    )


def get_job_profile(job_text):

    return {
        "ai": count_matches(
            job_text,
            AI_KEYWORDS,
        ),

        "retrieval": count_matches(
            job_text,
            RETRIEVAL_KEYWORDS,
        ),

        "data": count_matches(
            job_text,
            DATA_KEYWORDS,
        ),

        "mlops": count_matches(
            job_text,
            MLOPS_KEYWORDS,
        ),
    }