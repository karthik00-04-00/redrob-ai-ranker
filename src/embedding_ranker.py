from sentence_transformers import (
    SentenceTransformer,
    util,
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_embedding(text):

    return model.encode(
        text,
        convert_to_tensor=True,
    )


def get_embeddings(texts):

    return model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        convert_to_tensor=True,
    )


def get_semantic_similarity(
    job_embedding,
    candidate_text,
):

    candidate_embedding = (
        model.encode(
            candidate_text,
            convert_to_tensor=True,
        )
    )

    similarity = util.cos_sim(
        job_embedding,
        candidate_embedding,
    )

    return float(
        similarity.item()
    )


def get_semantic_similarities(
    job_embedding,
    candidate_texts,
):

    candidate_embeddings = (
        get_embeddings(
            candidate_texts
        )
    )

    similarities = util.cos_sim(
        job_embedding,
        candidate_embeddings,
    )[0]

    return (
        similarities
        .cpu()
        .numpy()
    )