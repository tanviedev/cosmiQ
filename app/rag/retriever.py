import json
import faiss
import numpy as np

# -----------------------------
# LOAD MODEL
# -----------------------------

from app.rag.model_loader import embedding_model as model   

# -----------------------------
# LOAD INDEX
# -----------------------------

index = faiss.read_index(
    "app/rag/vector_store/cosmiq.index"
)

# -----------------------------
# LOAD METADATA
# -----------------------------

with open(
    "app/rag/vector_store/metadata.json",
    "r",
    encoding="utf-8"
) as f:

    metadata = json.load(f)

# -----------------------------
# SAME FORMATTER AS EMBEDDER
# -----------------------------

def convert_to_text(entry):

    text_parts = []

    if entry.get("planet") and entry.get("house"):
        text_parts.append(
            f"{entry['planet']} in {entry['house']}th house"
        )

    if entry.get("sign"):
        text_parts.append(
            f"in {entry['sign']}"
        )

    if entry.get("tags"):
        text_parts.append(
            "Topics: " + ", ".join(entry["tags"])
        )

    if entry.get("meanings"):
        text_parts.append(
            "Meanings: " + ", ".join(entry["meanings"])
        )

    return " | ".join(text_parts)

# -----------------------------
# SEARCH
# -----------------------------

def search_knowledge_base(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []

    for idx in indices[0]:

        item = metadata[idx]

        results.append({
            "text": convert_to_text(item),
            "metadata": item
        })

    return results