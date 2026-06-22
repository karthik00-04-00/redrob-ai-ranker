AI_KEYWORDS = [
    "llm",
    "nlp",
    "transformer",
    "embedding",
    "vector",
    "rag",
    "fine-tuning",
    "lora",
]

RETRIEVAL_KEYWORDS = [
    "retrieval",
    "search",
    "ranking",
    "recommendation",
    "bm25",
    "elasticsearch",
    "faiss",
    "milvus",
]

MLOPS_KEYWORDS = [
    "mlops",
    "deployment",
    "monitoring",
    "airflow",
    "kubeflow",
    "bentoml",
]

CAREER_AI_KEYWORDS = [
    "machine learning",
    "deep learning",
    "classification",
    "prediction",
    "xgboost",
    "sklearn",
    "neural network",
]

CAREER_DATA_KEYWORDS = [
    "spark",
    "pyspark",
    "kafka",
    "airflow",
    "etl",
    "data pipeline",
    "data warehouse",
]

CAREER_RETRIEVAL_KEYWORDS = [
    "retrieval",
    "search",
    "ranking",
    "recommendation",
    "embedding",
    "vector",
]

RELEVANCE_KEYWORDS = [
    "ranking",
    "learning-to-rank",
    "recommendation",
    "retrieval",
    "search",
    "relevance",
    "embeddings",
    "information retrieval",
    "vector search",
    "offline-online correlation",
    "evaluation",
    "ab test",
    "a/b test",
    "feature pipeline",
]


def count_keywords(text, keywords):
    text = text.lower()

    score = 0

    for keyword in keywords:
        score += text.count(keyword.lower())

    return score


def get_ai_score(text):
    return count_keywords(text, AI_KEYWORDS)


def get_retrieval_score(text):
    return count_keywords(text, RETRIEVAL_KEYWORDS)


def get_mlops_score(text):
    return count_keywords(text, MLOPS_KEYWORDS)


def get_career_description_text(candidate):

    texts = []

    for role in candidate.get(
        "career_history",
        []
    ):
        texts.append(
            role.get("description", "")
        )

    return " ".join(texts).lower()


def get_career_ai_score(candidate):

    text = get_career_description_text(
        candidate
    )

    return count_keywords(
        text,
        CAREER_AI_KEYWORDS
    )


def get_career_data_score(candidate):

    text = get_career_description_text(
        candidate
    )

    return count_keywords(
        text,
        CAREER_DATA_KEYWORDS
    )


def get_career_retrieval_score(candidate):

    text = get_career_description_text(
        candidate
    )

    return count_keywords(
        text,
        CAREER_RETRIEVAL_KEYWORDS
    )


def get_relevance_score(candidate):

    text = get_career_description_text(
        candidate
    )

    return count_keywords(
        text,
        RELEVANCE_KEYWORDS
    )


def get_behavior_score(candidate):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    score = 0.0

    score += (
        signals.get(
            "github_activity_score",
            0
        )
        / 100
    )

    score += (
        signals.get(
            "profile_views_received_30d",
            0
        )
        / 100
    )

    score += (
        signals.get(
            "saved_by_recruiters_30d",
            0
        )
        / 50
    )

    score += (
        signals.get(
            "search_appearance_30d",
            0
        )
        / 100
    )

    score += (
        signals.get(
            "endorsements_received",
            0
        )
        / 100
    )

    score += signals.get(
        "interview_completion_rate",
        0
    )

    return score


def get_intent_score(candidate):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    score = 0.0

    if signals.get(
        "open_to_work_flag",
        False
    ):
        score += 2

    score += (
        signals.get(
            "applications_submitted_30d",
            0
        )
        / 50
    )

    score += signals.get(
        "recruiter_response_rate",
        0
    )

    score += signals.get(
        "offer_acceptance_rate",
        0
    )

    score -= (
        signals.get(
            "avg_response_time_hours",
            0
        )
        / 100
    )

    return score


def get_trust_score(candidate):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    score = 0.0

    score += (
        signals.get(
            "profile_completeness_score",
            0
        )
        / 100
    )

    score += int(
        signals.get(
            "verified_email",
            False
        )
    )

    score += int(
        signals.get(
            "verified_phone",
            False
        )
    )

    score += int(
        signals.get(
            "linkedin_connected",
            False
        )
    )

    return score

def get_candidate_profile(
    candidate,
    candidate_text,
):

    return {
        "ai":
            get_ai_score(
                candidate_text
            ),

        "retrieval":
            get_retrieval_score(
                candidate_text
            ),

        "mlops":
            get_mlops_score(
                candidate_text
            ),

        "career_ai":
            get_career_ai_score(
                candidate
            ),

        "career_data":
            get_career_data_score(
                candidate
            ),

        "career_retrieval":
            get_career_retrieval_score(
                candidate
            ),
    }