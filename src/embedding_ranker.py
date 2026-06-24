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