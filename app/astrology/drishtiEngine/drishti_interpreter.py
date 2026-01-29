from app.astrology.drishtiEngine.drishti_rules import DRISHTI_RULES

def interpret_drishti(drishti_data):
    interpretations = []
    for asp, info in drishti_data.items():
        for target in info["aspect_planets"]:
            text = DRISHTI_RULES.get(asp, {}).get("effects", {}).get(
                target,
                f"{asp} influences {target} generally"
            )
            interpretations.append({
                "from": asp,
                "to": target,
                "meaning": text
            })
    return interpretations
