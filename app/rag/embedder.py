import os
import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# -----------------------------
# PATHS
# -----------------------------

KB_FOLDER = "app/rag/kb"
VECTOR_FOLDER = "app/rag/vector_store"

os.makedirs(VECTOR_FOLDER, exist_ok=True)

# -----------------------------
# MODEL
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# LOAD KNOWLEDGE BASE
# -----------------------------

documents = []
metadata = []

# -----------------------------
# FORMATTER
# -----------------------------

def convert_to_text(entry):

    text_parts = []

    # planet + house
    if entry.get("planet") and entry.get("house"):
        text_parts.append(
            f"{entry['planet']} in {entry['house']}th house"
        )

    # sign
    if entry.get("sign"):
        text_parts.append(f"in {entry['sign']}")

    # tags
    if entry.get("tags"):
        text_parts.append(
            "Topics: " + ", ".join(entry["tags"])
        )

    # meanings
    if entry.get("meanings"):
        text_parts.append(
            "Meanings: " + ", ".join(entry["meanings"])
        )

    return " | ".join(text_parts)

# -----------------------------
# READ FILES
# -----------------------------

for file in os.listdir(KB_FOLDER):

    if not file.endswith(".json"):
        continue

    path = os.path.join(KB_FOLDER, file)

    try:

        with open(path, "r", encoding="utf-8") as f:

            content = f.read().strip()

            if not content:
                print(f"❌ Empty file: {file}")
                continue

            data = json.loads(content)

            for item in data:

                text = convert_to_text(item)

                documents.append(text)
                metadata.append(item)

    except Exception as e:
        print(f"❌ Error in {file}: {e}")

# -----------------------------
# EMBEDDINGS
# -----------------------------

print(f"Loaded {len(documents)} knowledge chunks")

embeddings = model.encode(documents)

# -----------------------------
# FAISS INDEX
# -----------------------------

dimension = len(embeddings[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

# -----------------------------
# SAVE
# -----------------------------

faiss.write_index(
    index,
    f"{VECTOR_FOLDER}/cosmiq.index"
)

with open(
    f"{VECTOR_FOLDER}/metadata.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(metadata, f, indent=2)

print("✅ Vector DB created successfully")