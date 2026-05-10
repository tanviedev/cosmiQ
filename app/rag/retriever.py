from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load index
index = faiss.read_index("app/rag/vector_store/cosmiq.index")

# Load documents
with open("app/rag/vector_store/documents.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines()]


def search_knowledge_base(query, k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):
            results.append(documents[idx])

    return results