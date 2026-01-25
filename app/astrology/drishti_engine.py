# app/astrology/drishti_engine.py

from app.astrology.drishti_rules import DRISHTI_RULES

def interpret_drishti(drishti_data):
    """
    drishti_data format:
    {
        "Saturn": ["Jupiter", "Venus"],
        "Mars": ["Moon"]
    }
    """
    interpretations = []

    for aspecting_planet, aspected_planets in drishti_data.items():
        rules = DRISHTI_RULES.get(aspecting_planet, {})
        general = rules.get("general", "")

        for target in aspected_planets:
            specific = rules.get("effects", {}).get(
                target,
                f"{aspecting_planet} influences {target} in a general manner."
            )

            interpretations.append({
                "from": aspecting_planet,
                "to": target,
                "theme": general,
                "meaning": specific
            })

    return interpretations
