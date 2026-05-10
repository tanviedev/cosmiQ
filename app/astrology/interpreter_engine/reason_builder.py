# ============================================
# MAIN ROUTER
# ============================================

def build_reasoning(intent, chart, dashas, aspects=None):

    if intent in ["career", "career_decision"]:
        return build_career_reasoning(chart, dashas, aspects)

    elif intent == "relationship":
        return build_relationship_reasoning(chart, dashas, aspects)

    elif intent == "mental":
        return build_mental_reasoning(chart, dashas, aspects)

    return build_general_reasoning(chart, dashas, aspects)


# ============================================
# CAREER
# ============================================

def build_career_reasoning(chart, dashas, aspects):

    reasoning = []

    # ----------------------------------------
    # 10TH HOUSE
    # ----------------------------------------

    for planet, data in chart.items():

        if data.get("house") == 10:

            reasoning.append({
                "type": "placement",
                "planet": planet,
                "house": 10,
                "sign": data["sign"],
                "tags": ["career"]
            })

    # ----------------------------------------
    # SATURN CAREER DELAY
    # ----------------------------------------

    if "Saturn" in chart:

        saturn = chart["Saturn"]

        reasoning.append({
            "type": "placement",
            "planet": "Saturn",
            "house": saturn["house"],
            "sign": saturn["sign"],
            "tags": ["career"]
        })

    # ----------------------------------------
    # DISPOSITORS
    # ----------------------------------------

    for planet, data in chart.items():

        if "dispositor" not in data:
            continue

        d = data["dispositor"]

        reasoning.append({
            "type": "dispositor",
            "planet": planet,
            "dispositor": d["dispositor"],
            "house": d["dispositor_house"],
            "strength": d["dispositor_strength_hint"],
            "tags": ["career"]
        })

    # ----------------------------------------
    # ASPECTS
    # ----------------------------------------

    if aspects:

        for asp in aspects:

            if asp["to"] in ["Saturn", "Jupiter", "Venus"]:

                reasoning.append({
                    "type": "aspect",
                    "from": asp["from"],
                    "to": asp["to"],
                    "meaning": asp["meaning"],
                    "tags": ["career"]
                })

    # ----------------------------------------
    # CURRENT DASHA
    # ----------------------------------------

    current = get_current_dasha(dashas)

    if current:

        reasoning.append({
            "type": "dasha",
            "planet": current,
            "tags": ["career"]
        })

    return reasoning


# ============================================
# RELATIONSHIP
# ============================================

def build_relationship_reasoning(chart, dashas, aspects):

    reasoning = []

    # ----------------------------------------
    # 7TH HOUSE
    # ----------------------------------------

    for planet, data in chart.items():

        if data.get("house") == 7:

            reasoning.append({
                "type": "placement",
                "planet": planet,
                "house": 7,
                "sign": data["sign"],
                "tags": ["relationship"]
            })

    # ----------------------------------------
    # VENUS
    # ----------------------------------------

    if "Venus" in chart:

        venus = chart["Venus"]

        reasoning.append({
            "type": "placement",
            "planet": "Venus",
            "house": venus["house"],
            "sign": venus["sign"],
            "tags": ["relationship"]
        })

    # ----------------------------------------
    # ASPECTS TO VENUS
    # ----------------------------------------

    if aspects:

        for asp in aspects:

            if asp["to"] == "Venus":

                reasoning.append({
                    "type": "aspect",
                    "from": asp["from"],
                    "to": "Venus",
                    "meaning": asp["meaning"],
                    "tags": ["relationship"]
                })

    # ----------------------------------------
    # DASHA
    # ----------------------------------------

    current = get_current_dasha(dashas)

    if current:

        reasoning.append({
            "type": "dasha",
            "planet": current,
            "tags": ["relationship"]
        })

    return reasoning


# ============================================
# MENTAL
# ============================================

def build_mental_reasoning(chart, dashas, aspects):

    reasoning = []

    # ----------------------------------------
    # MOON
    # ----------------------------------------

    if "Moon" in chart:

        moon = chart["Moon"]

        reasoning.append({
            "type": "placement",
            "planet": "Moon",
            "house": moon["house"],
            "sign": moon["sign"],
            "tags": ["mental"]
        })

    # ----------------------------------------
    # RAHU
    # ----------------------------------------

    if "Rahu" in chart:

        rahu = chart["Rahu"]

        reasoning.append({
            "type": "placement",
            "planet": "Rahu",
            "house": rahu["house"],
            "sign": rahu["sign"],
            "tags": ["mental"]
        })

    # ----------------------------------------
    # ASPECTS TO MOON
    # ----------------------------------------

    if aspects:

        for asp in aspects:

            if asp["to"] == "Moon":

                reasoning.append({
                    "type": "aspect",
                    "from": asp["from"],
                    "to": "Moon",
                    "meaning": asp["meaning"],
                    "tags": ["mental"]
                })

    # ----------------------------------------
    # DASHA
    # ----------------------------------------

    current = get_current_dasha(dashas)

    if current:

        reasoning.append({
            "type": "dasha",
            "planet": current,
            "tags": ["mental"]
        })

    return reasoning


# ============================================
# GENERAL
# ============================================

def build_general_reasoning(chart, dashas, aspects):

    reasoning = []

    for planet, data in chart.items():

        reasoning.append({
            "type": "placement",
            "planet": planet,
            "house": data["house"],
            "sign": data["sign"],
            "tags": ["general"]
        })

    if aspects:

        for asp in aspects:

            reasoning.append({
                "type": "aspect",
                "from": asp["from"],
                "to": asp["to"],
                "meaning": asp["meaning"],
                "tags": ["general"]
            })

    current = get_current_dasha(dashas)

    if current:

        reasoning.append({
            "type": "dasha",
            "planet": current,
            "tags": ["general"]
        })

    return reasoning


# ============================================
# CURRENT DASHA
# ============================================

from datetime import datetime


def get_current_dasha(dashas):

    now = datetime.utcnow().replace(tzinfo=None)

    for d in dashas:

        start = d["start"].replace(tzinfo=None)
        end = d["end"].replace(tzinfo=None)

        if start <= now <= end:
            return d["mahadasha"]

    return None