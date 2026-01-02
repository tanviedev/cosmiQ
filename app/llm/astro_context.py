# app/llm/astro_context.py

def build_astro_context(chart, aspects):
    """
    Converts raw chart + drishti into LLM-safe structured context
    """

    planets = []

    for planet, data in chart.items():
        if planet == "Ascendant":
            continue

        planets.append({
            "planet": planet,
            "sign": data["sign"],
            "house": data["house"],
            "degree": data["degree"],
            "nakshatra": data["nakshatra"],
            "pada": data["pada"],
            "nakshatra_lord": data["nakshatra_lord"],
            "aspects": aspects.get(planet, {})
        })

    asc = chart["Ascendant"]

    return {
        "ascendant": {
            "sign": asc["sign"],
            "degree": asc["degree"],
            "nakshatra": asc["nakshatra"],
            "pada": asc["pada"]
        },
        "planets": planets
    }
