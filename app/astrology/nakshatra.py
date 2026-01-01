# app/astrology/nakshatra.py

NAKSHATRAS = [
    ("Ashwini", "Ketu"),
    ("Bharani", "Venus"),
    ("Krittika", "Sun"),
    ("Rohini", "Moon"),
    ("Mrigashira", "Mars"),
    ("Ardra", "Rahu"),
    ("Punarvasu", "Jupiter"),
    ("Pushya", "Saturn"),
    ("Ashlesha", "Mercury"),
    ("Magha", "Ketu"),
    ("Purva Phalguni", "Venus"),
    ("Uttara Phalguni", "Sun"),
    ("Hasta", "Moon"),
    ("Chitra", "Mars"),
    ("Swati", "Rahu"),
    ("Vishakha", "Jupiter"),
    ("Anuradha", "Saturn"),
    ("Jyeshtha", "Mercury"),
    ("Mula", "Ketu"),
    ("Purva Ashadha", "Venus"),
    ("Uttara Ashadha", "Sun"),
    ("Shravana", "Moon"),
    ("Dhanishta", "Mars"),
    ("Shatabhisha", "Rahu"),
    ("Purva Bhadrapada", "Jupiter"),
    ("Uttara Bhadrapada", "Saturn"),
    ("Revati", "Mercury"),
]

NAKSHATRA_SPAN = 13.333333333333334   # 13°20'
PADA_SPAN = 3.3333333333333335        # 3°20'


def get_nakshatra(longitude: float) -> dict:
    """
    Returns Nakshatra, Nakshatra Lord, and Pada for a given sidereal longitude.
    """

    longitude = longitude % 360

    nak_index = int(longitude // NAKSHATRA_SPAN)
    nak_name, nak_lord = NAKSHATRAS[nak_index]

    pada = int((longitude % NAKSHATRA_SPAN) // PADA_SPAN) + 1

    return {
        "nakshatra": nak_name,
        "nakshatra_lord": nak_lord,
        "pada": pada
    }

