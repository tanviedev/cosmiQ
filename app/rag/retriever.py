import json
import faiss
import numpy as np

# -----------------------------------
# LOAD EMBEDDING MODEL
# -----------------------------------

from app.rag.model_loader import embedding_model as model

# -----------------------------------
# IMPORT SYMBOLIC FILTER
# -----------------------------------

from app.rag.symbolic_filter import symbolic_filter

# -----------------------------------
# IMPORT SYMBOLIC SCORER
# -----------------------------------

from app.rag.scorer import calculate_symbolic_score

# -----------------------------------
# LOAD VECTOR INDEX
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
# Converts KB entries into text
# for embeddings + LLM context
# -----------------------------------

def convert_to_text(entry):

    text_parts = []

    # --------------------------------
    # PLANETARY PLACEMENTS
    # --------------------------------

    if entry.get("planet") and entry.get("house"):

        text_parts.append(
            f"{entry['planet']} in {entry['house']}th house"
        )

    # --------------------------------
    # SIGN
    # --------------------------------

    if entry.get("sign"):

        text_parts.append(
            f"in {entry['sign']}"
        )

    # --------------------------------
    # ASPECTS
    # --------------------------------

    if entry.get("from") and entry.get("to"):

        text_parts.append(
            f"{entry['from']} aspecting {entry['to']}"
        )

    # --------------------------------
    # DASHA
    # --------------------------------

    if entry.get("category") == "dasha":

        text_parts.append(
            f"{entry.get('planet')} Mahadasha"
        )

    # --------------------------------
    # TAGS
    # --------------------------------

    if entry.get("tags"):

        text_parts.append(
            "Topics: " + ", ".join(entry["tags"])
        )

    # --------------------------------
    # MEANINGS
    # --------------------------------

    if entry.get("meanings"):

        text_parts.append(
            "Meanings: " + ", ".join(entry["meanings"])
        )

    return " | ".join(text_parts)

# -----------------------------------
# SEMANTIC SEARCH
# Performs vector similarity search
# -----------------------------------

def semantic_search(
    documents,
    query,
    reasoning,
    top_k=5
):

    # --------------------------------
    # SAFETY CHECK
    # --------------------------------

    if not documents:
        return []

    # --------------------------------
    # CONVERT DOCS TO TEXT
    # --------------------------------

    doc_texts = [
        convert_to_text(doc)
        for doc in documents
    ]

    # --------------------------------
    # CREATE DOCUMENT EMBEDDINGS
    # --------------------------------

    doc_embeddings = model.encode(
        doc_texts
    )

    # --------------------------------
    # CREATE TEMP FAISS INDEX
    # --------------------------------

    temp_index = faiss.IndexFlatL2(
        len(doc_embeddings[0])
    )

    temp_index.add(
        np.array(doc_embeddings)
    )

    # --------------------------------
    # ENCODE QUERY
    # --------------------------------

    query_embedding = model.encode(
        [query]
    )

    # --------------------------------
    # VECTOR SEARCH
    # --------------------------------

    distances, indices = temp_index.search(
        np.array(query_embedding),
        min(top_k, len(documents))
    )

    # --------------------------------
    # BUILD RESULTS
    # --------------------------------

    results = []

    for rank, idx in enumerate(indices[0]):

        item = documents[idx]

        # ----------------------------
        # SYMBOLIC SCORE
        # ----------------------------

        symbolic_score = calculate_symbolic_score(
            reasoning,
            item
        )

        # ----------------------------
        # STORE RESULT
        # ----------------------------

        results.append({

            "text": convert_to_text(item),

            "metadata": item,

            "semantic_distance": float(
                distances[0][rank]
            ),

            "symbolic_score": symbolic_score
        })

    # --------------------------------
    # FINAL HYBRID RANKING
    # --------------------------------

    results = sorted(

        results,

        key=lambda x: (
            x["symbolic_score"]
            - x["semantic_distance"]
        ),

        reverse=True
    )

    return results[:top_k]

# -----------------------------------
# MAIN RETRIEVAL PIPELINE
# -----------------------------------

def search_knowledge_base(
    query,
    reasoning,
    top_k=5
):

    # --------------------------------
    # STEP 1:
    # SYMBOLIC FILTERING
    # --------------------------------

    filtered_docs = symbolic_filter(
        metadata,
        reasoning
    )

    # --------------------------------
    # FALLBACK SAFETY
    # --------------------------------

    if not filtered_docs:

        filtered_docs = metadata

    # --------------------------------
    # STEP 2:
    # HYBRID SEMANTIC SEARCH
    # --------------------------------

    results = semantic_search(
        filtered_docs,
        query,
        reasoning,
        top_k
    )

    return results