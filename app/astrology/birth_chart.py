# app/astrology/birth_chart.py

import swisseph as swe
from app.astrology.nakshatra import get_nakshatra

# --------------------------------------------------
# CONSTANTS
# --------------------------------------------------

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE,
    "Ketu": swe.MEAN_NODE,
}

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Vedic Rāśi Lords
RASI_LORDS = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter",
}

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def get_sign(longitude: float) -> str:
    return SIGNS[int(longitude // 30)]


def get_julian_day(utc_datetime):
    return swe.julday(
        utc_datetime.year,
        utc_datetime.month,
        utc_datetime.day,
        utc_datetime.hour + utc_datetime.minute / 60.0
    )

# --------------------------------------------------
# CORE CALCULATIONS
# --------------------------------------------------

def calculate_chart(utc_datetime):
    """
    Calculates sidereal (Lahiri) planetary longitudes.
    Houses and nakshatras are assigned later.
    """
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    jd = get_julian_day(utc_datetime)
    chart = {}

    for planet, pid in PLANETS.items():
        pos, _ = swe.calc_ut(jd, pid, swe.FLG_SIDEREAL)
        lon = pos[0] % 360

        # Ketu is always opposite Rahu
        if planet == "Ketu":
            lon = (lon + 180) % 360

        sign = get_sign(lon)

        chart[planet] = {
            "longitude": round(lon, 2),
            "sign": sign,
            "degree": round(lon % 30, 2),
            "rasi_lord": RASI_LORDS[sign],
        }

    return chart


def calculate_ascendant(jd, latitude, longitude):
    """
    Calculates sidereal ascendant using Lahiri ayanamsa.
    """
    houses, ascmc = swe.houses(jd, latitude, longitude, b'P')
    tropical_asc = ascmc[0]

    ayanamsa = swe.get_ayanamsa(jd)
    sidereal_asc = (tropical_asc - ayanamsa) % 360

    return sidereal_asc


def assign_houses(chart, ascendant_longitude):
    """
    Assigns houses using WHOLE SIGN VEDIC logic
    and adds Nakshatra + Pada.
    """
    asc_sign_index = int(ascendant_longitude // 30)

    for planet, data in chart.items():
        planet_sign_index = int(data["longitude"] // 30)

        # Whole sign house system
        house = (planet_sign_index - asc_sign_index) % 12 + 1
        data["house"] = house

        # Nakshatra + Pada + Nakshatra Lord
        nakshatra_data = get_nakshatra(data["longitude"])
        data.update(nakshatra_data)

    return chart
