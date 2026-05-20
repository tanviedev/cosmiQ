def calculate_symbolic_score(
    reasoning,
    metadata
):

    score = 0

    for r in reasoning:

        # -------------------------
        # PLANET MATCH
        # -------------------------

        if (
            r.get("planet")
            and
            metadata.get("planet")
        ):

            if r["planet"] == metadata["planet"]:
                score += 4

        # -------------------------
        # HOUSE MATCH
        # -------------------------

        if (
            r.get("house")
            and
            metadata.get("house")
        ):

            if r["house"] == metadata["house"]:
                score += 3

        # -------------------------
        # SIGN MATCH
        # -------------------------

        if (
            r.get("sign")
            and
            metadata.get("sign")
        ):

            if r["sign"] == metadata["sign"]:
                score += 2

        # -------------------------
        # CATEGORY MATCH
        # -------------------------

        if (
            r.get("type")
            and
            metadata.get("category")
        ):

            if r["type"] == metadata["category"]:
                score += 2

        # -------------------------
        # TAG MATCHES
        # -------------------------

        r_tags = set(r.get("tags", []))
        m_tags = set(metadata.get("tags", []))

        score += len(r_tags & m_tags)

    return score