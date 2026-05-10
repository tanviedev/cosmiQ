import json
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


# ============================================
# LOAD MODEL
# ============================================

model = SentenceTransformer("all-MiniLM-L6-v2")


# ============================================
# LOAD KNOWLEDGE BASE
# ============================================

with open("app/rag/kb/placements.json", "r") as f:
    placements_kb = json.load(f)

with open("app/rag/kb/aspects.json", "r") as f:
    aspects_kb = json.load(f)


KNOWLEDGE_BASE = placements_kb + aspects_kb


# ============================================
# BUILD SEARCH TEXTS
# ============================================

search_texts = []

for item in KNOWLEDGE_BASE:

    text = f"""
    {item.get('planet', '')}
    {item.get('house', '')}
    {item.get('category', '')}
    {' '.join(item.get('meanings', []))}
    """

    search_texts.append(text)


# ============================================
# EMBEDDINGS
# ============================================

embeddings = model.encode(search_texts)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))


# ============================================
# SYMBOLIC FILTER
# ============================================

def symbolic_filter(reasoning):

    matches = []

    for signal in reasoning:

        for item in KNOWLEDGE_BASE:

            # placement match
            if signal["category"] == "placement":

                if (
                    item.get("planet") == signal.get("planet")
                    and item.get("house") == signal.get("house")
                ):
                    matches.append(item)

            # aspect match
            elif signal["category"] == "aspect":

                if (
                    item.get("from") == signal.get("from")
                    and item.get("to") == signal.get("to")
                ):
                    matches.append(item)

    return matches