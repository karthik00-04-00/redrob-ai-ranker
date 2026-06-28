def extract_evidence(text):
    text = text.lower()

    evidence = []

    if "learning-to-rank" in text:
        evidence.append(
            "Built learning-to-rank systems"
        )

    if "ranking" in text:
        evidence.append(
            "Worked on ranking systems"
        )

    if "recommendation" in text:
        evidence.append(
            "Built recommendation systems"
        )

    if "semantic search" in text:
        evidence.append(
            "Built semantic search systems"
        )

    if "faiss" in text:
        evidence.append(
            "Used FAISS for vector retrieval"
        )

    if "pinecone" in text:
        evidence.append(
            "Used Pinecone vector database"
        )

    if "rag" in text:
        evidence.append(
            "Built RAG pipelines"
        )

    if "embedding" in text:
        evidence.append(
            "Worked with embeddings"
        )

    if "evaluation" in text:
        evidence.append(
            "Designed evaluation frameworks"
        )

    if "mlflow" in text:
        evidence.append(
            "Used MLflow in production"
        )

    if "kubeflow" in text:
        evidence.append(
            "Built ML pipelines with Kubeflow"
        )

    return list(set(evidence))