def build_rag_query(intent, reasoning_list):

    reasoning_texts = []

    for item in reasoning_list:

        # structured reasoning object
        if isinstance(item, dict):

            if "text" in item:
                reasoning_texts.append(item["text"])

        # fallback plain string
        elif isinstance(item, str):
            reasoning_texts.append(item)

    combined_reasoning = " ".join(reasoning_texts)

    query = f"""
    Intent: {intent}

    Astrological Evidence:
    {combined_reasoning}
    """

    return query.strip()