ASPECTS = {
    "conjunction": 0,
    "sextile": 60,
    "square": 90,
    "trine": 120,
    "opposition": 180
}

def calculate_aspect(deg1, deg2):
    diff = abs(deg1 - deg2)
    diff = min(diff, 360 - diff)
    return diff

# Classical Vedic Drishti rules (Whole Sign based)
ASPECT_RULES = {
    "Sun":     [7],
    "Moon":    [7],
    "Mars":    [4, 7, 8],
    "Mercury": [7],
    "Jupiter": [5, 7, 9],
    "Venus":   [7],
    "Saturn":  [3, 7, 10],
    "Rahu":    [5, 7, 9],
    "Ketu":    [5, 7, 9],
}


def calculate_aspects(chart):
    """
    chart: dict returned after assign_houses()
    returns: dict of planet-wise aspects
    """

    aspects = {}

    # Build reverse lookup: house -> planets
    house_map = {}
    for planet, data in chart.items():
        house = data["house"]
        house_map.setdefault(house, []).append(planet)

    for planet, data in chart.items():
        if planet == "Ascendant":
            continue

        base_house = data["house"]
        aspect_houses = []

        for offset in ASPECT_RULES.get(planet, []):
            target_house = ((base_house - 1 + offset) % 12) + 1
            aspect_houses.append(target_house)

        # Which planets are aspected
        aspected_planets = []
        for h in aspect_houses:
            aspected_planets.extend(house_map.get(h, []))

        # Remove self-aspect
        aspected_planets = [
            p for p in aspected_planets if p != planet
        ]

        aspects[planet] = {
            "aspect_houses": sorted(set(aspect_houses)),
            "aspect_planets": sorted(set(aspected_planets))
        }

    return aspects