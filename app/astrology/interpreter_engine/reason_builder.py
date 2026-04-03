def build_reasoning(intent, chart, dashas):

    if intent == "career":
        return build_career_reasoning(chart, dashas)

    elif intent == "relationship":
        return build_relationship_reasoning(chart, dashas)

    elif intent == "mental":
        return build_mental_reasoning(chart, dashas)

    return build_general_reasoning(chart, dashas)


# ------------------ CAREER ------------------

def build_career_reasoning(chart, dashas):
    reasoning = []

    # 10th house
    for planet, data in chart.items():
        if data.get("house") == 10:
            reasoning.append(f"{planet} is placed in 10th house ({data['sign']})")

    # dispositor
    for planet, data in chart.items():
        if "dispositor" in data:
            d = data["dispositor"]
            reasoning.append(
                f"{planet}'s dispositor is {d['dispositor']} in house {d['dispositor_house']}"
            )

    # dasha
    if dashas:
        reasoning.append(f"Current Mahadasha is {dashas[0]['planet']}")

    return reasoning


# ------------------ RELATIONSHIP ------------------

def build_relationship_reasoning(chart, dashas):
    reasoning = []

    for planet, data in chart.items():
        if data.get("house") == 7:
            reasoning.append(f"{planet} is placed in 7th house ({data['sign']})")

    if "Venus" in chart:
        v = chart["Venus"]
        reasoning.append(f"Venus is in {v['sign']} in house {v['house']}")

    if dashas:
        reasoning.append(f"Current Mahadasha is {dashas[0]['planet']}")

    return reasoning


# ------------------ MENTAL ------------------

def build_mental_reasoning(chart, dashas):
    reasoning = []

    if "Moon" in chart:
        m = chart["Moon"]
        reasoning.append(f"Moon is in {m['sign']} in house {m['house']}")

    if "Rahu" in chart:
        r = chart["Rahu"]
        reasoning.append(f"Rahu is in {r['sign']} in house {r['house']}")

    if dashas:
        reasoning.append(f"Current Mahadasha is {dashas[0]['planet']}")

    return reasoning


# ------------------ GENERAL ------------------

def build_general_reasoning(chart, dashas):
    reasoning = []

    for planet, data in chart.items():
        reasoning.append(f"{planet} in {data['sign']} house {data['house']}")

    if dashas:
        reasoning.append(f"Current Mahadasha is {dashas[0]['planet']}")

    return reasoning


def format_reasoning(reasoning_list):
    return "\n".join([f"- {r['text']}" for r in reasoning_list])