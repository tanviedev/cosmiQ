def symbolic_filter(documents, reasoning):

    filtered = []

    for doc in documents:

        metadata = doc["metadata"]

        for ev in reasoning:

            # -------------------------
            # PLANET MATCH
            # -------------------------

            if (
                "planet" in ev
                and metadata.get("planet") == ev["planet"]
            ):
                filtered.append(doc)
                break

            # -------------------------
            # HOUSE MATCH
            # -------------------------

            if (
                "house" in ev
                and metadata.get("house") == ev["house"]
            ):
                filtered.append(doc)
                break

            # -------------------------
            # CATEGORY MATCH
            # -------------------------

            if metadata.get("category") == ev["type"]:
                filtered.append(doc)
                break

            # -------------------------
            # TAG OVERLAP
            # -------------------------

            if (
                "tags" in ev
                and any(
                    tag in metadata.get("tags", [])
                    for tag in ev["tags"]
                )
            ):
                filtered.append(doc)
                break

    return filtered