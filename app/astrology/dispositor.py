# app/astrology/dispositor.py

from app.astrology.rasi_lords import RASI_LORDS


def get_dispositor(planet_name, planet_data, chart):
    """
    Returns dispositor details for a given planet
    """

    sign = planet_data["sign"]
    lord = RASI_LORDS.get(sign)

    if not lord or lord not in chart:
        return None

    lord_data = chart[lord]

    return {
        "dispositor": lord,
        "dispositor_sign": lord_data["sign"],
        "dispositor_house": lord_data["house"],
        "dispositor_nakshatra": lord_data.get("nakshatra"),
        "dispositor_strength_hint": _strength_hint(lord_data)
    }


def _strength_hint(lord_data):
    """
    Very lightweight strength indicator (can be expanded later)
    """
    house = lord_data["house"]

    if house in [1, 4, 7, 10]:
        return "strong (kendra placement)"
    elif house in [5, 9]:
        return "supportive (trikona placement)"
    elif house in [6, 8, 12]:
        return "challenged (dusthana placement)"
    else:
        return "neutral"
