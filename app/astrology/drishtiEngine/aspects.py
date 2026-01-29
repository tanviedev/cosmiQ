ASPECT_RULES = {
    "Sun": [7],
    "Moon": [7],
    "Mars": [4, 7, 8],
    "Mercury": [7],
    "Jupiter": [5, 7, 9],
    "Venus": [7],
    "Saturn": [3, 7, 10],
    "Rahu": [5, 7, 9],
    "Ketu": [5, 7, 9],
}

def calculate_aspects(chart):
    aspects = {}
    house_map = {}
    for p, d in chart.items():
        house_map.setdefault(d["house"], []).append(p)

    for p, d in chart.items():
        if p == "Ascendant":
            continue

        base = d["house"]
        targets = []
        for offset in ASPECT_RULES.get(p, []):
            target_house = ((base - 1 + offset) % 12) + 1
            targets.append(target_house)

        planets = []
        for h in targets:
            planets.extend(house_map.get(h, []))

        planets = [x for x in planets if x != p]
        aspects[p] = {
            "aspect_houses": sorted(targets),
            "aspect_planets": sorted(set(planets))
        }

    return aspects
