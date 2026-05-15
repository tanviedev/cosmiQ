import json
import faiss
import numpy as np

# -----------------------------------
# LOAD MODEL
# -----------------------------------

from app.rag.model_loader import embedding_model as model
from app.rag.symbolic_filter import symbolic_filter

# -----------------------------------
# LOAD INDEX
# -----------------------------------

index = faiss.read_index(
    "app/rag/vector_store/cosmiq.index"
)

# -----------------------------------
# LOAD METADATA
# -----------------------------------

with open(
    "app/rag/vector_store/metadata.json",
    "r",
    encoding="utf-8"
) as f:

    metadata = json.load(f)

# -----------------------------------
# FORMATTER
# -----------------------------------

def convert_to_text(entry):

    text_parts = []

    # -------------------------
    # PLACEMENTS
    # -------------------------

    if entry.get("planet") and entry.get("house"):

        text_parts.append(
            f"{entry['planet']} in {entry['house']}th house"
        )

    # -------------------------
    # SIGN
    # -------------------------

    if entry.get("sign"):

        text_parts.append(
            f"in {entry['sign']}"
        )

    # -------------------------
    # ASPECTS
    # -------------------------

    if entry.get("from") and entry.get("to"):

        text_parts.append(
            f"{entry['from']} aspecting {entry['to']}"
        )

    # -------------------------
    # DASHA
    # -------------------------

    if entry.get("category") == "dasha":

        text_parts.append(
            f"{entry.get('planet')} Mahadasha"
        )

    # -------------------------
    # TAGS
    # -------------------------

    if entry.get("tags"):

        text_parts.append(
            "Topics: " + ", ".join(entry["tags"])
        )

    # -------------------------
    # MEANINGS
    # -------------------------

    if entry.get("meanings"):

        text_parts.append(
            "Meanings: " + ", ".join(entry["meanings"])
        )

    return " | ".join(text_parts)

# -----------------------------------
# SEMANTIC SEARCH
# -----------------------------------

def semantic_search(documents, query, top_k=5):

    if not documents:
        return []

    doc_texts = [
        convert_to_text(doc)
        for doc in documents
    ]

    doc_embeddings = model.encode(doc_texts)

    temp_index = faiss.IndexFlatL2(
        len(doc_embeddings[0])
    )

    temp_index.add(
        np.array(doc_embeddings)
    )

    query_embedding = model.encode([query])

    distances, indices = temp_index.search(
        np.array(query_embedding),
        min(top_k, len(documents))
    )

    results = []

    for idx in indices[0]:

        item = documents[idx]

        results.append({
            "text": convert_to_text(item),
            "metadata": item
        })

    return results

# -----------------------------------
# MAIN RETRIEVAL PIPELINE
# -----------------------------------

def search_knowledge_base(
    query,
    reasoning,
    top_k=5
):

    # -----------------------------------
    # 1️⃣ SYMBOLIC FILTER
    # -----------------------------------

    filtered_docs = symbolic_filter(
        metadata,
        reasoning
    )

    # fallback safety

    if not filtered_docs:
        filtered_docs = metadata

    # -----------------------------------
    # 2️⃣ SEMANTIC SEARCH
    # -----------------------------------

    results = semantic_search(
        filtered_docs,
        query,
        top_k
    )

    return results