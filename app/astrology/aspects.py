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
