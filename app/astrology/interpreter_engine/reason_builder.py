def build_reasoning(intent, chart, dashas, aspects=None):

    if intent in ["career", "career_decision"]:
        return build_career_reasoning(chart, dashas, aspects)

    elif intent == "relationship":
        return build_relationship_reasoning(chart, dashas, aspects)

    elif intent == "mental":
        return build_mental_reasoning(chart, dashas, aspects)

    return build_general_reasoning(chart, dashas)
# ------------------ CAREER ------------------

def build_career_reasoning(chart, dashas, aspects):
    reasoning = []

    # 🔹 1. Current Dasha (REAL LOGIC)
    if dashas:
        current = dashas[0]["mahadasha"]
        reasoning.append(f"Current Mahadasha: {current}")

    # 🔹 2. 10th House (CAREER CORE)
    for planet, data in chart.items():
        if data.get("house") == 10:
            reasoning.append(
                f"{planet} in 10th house ({data['sign']}) → career focus, visibility"
            )

    # 🔹 3. Dispositors (CHAIN LOGIC)
    for planet, data in chart.items():
        if "dispositor" in data:
            d = data["dispositor"]
            reasoning.append(
                f"{planet} dispositor → {d['dispositor']} in house {d['dispositor_house']} ({d['dispositor_strength_hint']})"
            )

    # 🔹 4. Saturn Delay Factor
    if "Saturn" in chart and chart["Saturn"]["house"] == 7:
        reasoning.append(
            "Saturn in 7th → delays in external opportunities / partnerships"
        )

    # 🔹 5. Aspects (VERY IMPORTANT 🔥)
    if aspects:
        for asp in aspects:
            if asp["to"] in ["Saturn", "Rahu"]:
                reasoning.append(
                    f"{asp['from']} aspects {asp['to']} → {asp['meaning']}"
                )

    return reasoning
# ------------------ RELATIONSHIP ------------------

def build_relationship_reasoning(chart, dashas, aspects):
    reasoning = []

    # 7th house
    for planet, data in chart.items():
        if data.get("house") == 7:
            reasoning.append(
                f"{planet} in 7th house ({data['sign']}) → relationship focus"
            )

    # Venus
    if "Venus" in chart:
        v = chart["Venus"]
        reasoning.append(
            f"Venus in {v['sign']} house {v['house']} → love style and attraction"
        )

    # Saturn (karmic delay)
    if "Saturn" in chart and chart["Saturn"]["house"] == 7:
        reasoning.append(
            "Saturn in 7th → delayed or karmic relationships"
        )

    # Dasha
    if dashas:
        reasoning.append(f"Current Mahadasha: {dashas[0]['mahadasha']}")

    # Aspects
    if aspects:
        for asp in aspects:
            if asp["to"] == "Venus":
                reasoning.append(
                    f"{asp['from']} influences Venus → {asp['meaning']}"
                )

    return reasoning


# ------------------ MENTAL ------------------

def build_mental_reasoning(chart, dashas, aspects):
    reasoning = []

    # Moon (core mind)
    if "Moon" in chart:
        m = chart["Moon"]
        reasoning.append(
            f"Moon in {m['sign']} house {m['house']} → emotional nature"
        )

    # Rahu (anxiety amplifier)
    if "Rahu" in chart:
        r = chart["Rahu"]
        reasoning.append(
            f"Rahu in {r['sign']} house {r['house']} → mental amplification, restlessness"
        )

    # Moon aspects
    if aspects:
        for asp in aspects:
            if asp["to"] == "Moon":
                reasoning.append(
                    f"{asp['from']} affects Moon → {asp['meaning']}"
                )

    # Dasha influence
    if dashas:
        reasoning.append(f"Current Mahadasha: {dashas[0]['mahadasha']}")

    return reasoning

# ------------------ GENERAL ------------------

def build_general_reasoning(chart, dashas):
    reasoning = []

    for planet, data in chart.items():
        reasoning.append(
            f"{planet} in {data['sign']} house {data['house']}"
        )

    if dashas:
        reasoning.append(f"Current Mahadasha: {dashas[0]['mahadasha']}")

    return reasoning

def format_reasoning(reasoning_list):
    return "\n".join([f"- {r}" for r in reasoning_list])