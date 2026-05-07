# broken-RAG  
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load your knowledge base
documents = [
    "Saturn in 7th house causes delays in relationships and partnerships",
    "Jupiter in 10th house gives career growth and recognition",
    "Rahu aspect on Moon creates mental instability and overthinking",
    "Venus in Libra strengthens charm and public image",
]

embeddings = model.encode(documents)
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))


def retrieve_context(query, k=3):
    q_emb = model.encode([query])
    distances, indices = index.search(np.array(q_emb), k)

    results = [documents[i] for i in indices[0]]
    return results