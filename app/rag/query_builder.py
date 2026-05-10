def build_rag_query(intent, reasoning_list):

    chunks = []

    # intent
    chunks.append(intent)

    # evidence
    chunks.extend(reasoning_list)

    return " ".join(chunks)