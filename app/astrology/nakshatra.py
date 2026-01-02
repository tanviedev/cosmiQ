NAKSHATRAS = [
    ("Ashwini", "Ketu"), ("Bharani", "Venus"), ("Krittika", "Sun"),
    ("Rohini", "Moon"), ("Mrigashira", "Mars"), ("Ardra", "Rahu"),
    ("Punarvasu", "Jupiter"), ("Pushya", "Saturn"), ("Ashlesha", "Mercury"),
    ("Magha", "Ketu"), ("Purva Phalguni", "Venus"), ("Uttara Phalguni", "Sun"),
    ("Hasta", "Moon"), ("Chitra", "Mars"), ("Swati", "Rahu"),
    ("Vishakha", "Jupiter"), ("Anuradha", "Saturn"), ("Jyeshtha", "Mercury"),
    ("Mula", "Ketu"), ("Purva Ashadha", "Venus"), ("Uttara Ashadha", "Sun"),
    ("Shravana", "Moon"), ("Dhanishtha", "Mars"), ("Shatabhisha", "Rahu"),
    ("Purva Bhadrapada", "Jupiter"), ("Uttara Bhadrapada", "Saturn"),
    ("Revati", "Mercury"),
]

NAK_LEN = 13 + 1/3
PADA_LEN = NAK_LEN / 4


def get_nakshatra(lon):
    lon = lon % 360
    idx = int(lon // NAK_LEN)
    pada = int((lon % NAK_LEN) // PADA_LEN) + 1
    name, lord = NAKSHATRAS[idx]

    return {
        "nakshatra": name,
        "pada": pada,
        "nakshatra_lord": lord
    }
