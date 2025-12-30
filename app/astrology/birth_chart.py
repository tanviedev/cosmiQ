# app/astrology/birth_chart.py

import swisseph as swe

# --- CONSTANTS ---

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

# --- HELPERS ---

def get_sign(longitude):
    return SIGNS[int(longitude // 30)]

def get_julian_day(utc_datetime):
    return swe.julday(
        utc_datetime.year,
        utc_datetime.month,
        utc_datetime.day,
        utc_datetime.hour + utc_datetime.minute / 60
    )

# --- CORE LOGIC ---

def calculate_chart(utc_datetime):
    # ✅ Lahiri Ayanamsa
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    jd = get_julian_day(utc_datetime)
    chart = {}

    for planet, pid in PLANETS.items():
        pos, _ = swe.calc_ut(jd, pid, swe.FLG_SIDEREAL)
        lon = pos[0] % 360

        # Ketu always opposite Rahu
        if planet == "Ketu":
            lon = (lon + 180) % 360

        chart[planet] = {
            "longitude": round(lon, 2),
            "sign": get_sign(lon),
            "degree": round(lon % 30, 2),
        }

    return chart

def calculate_ascendant(jd, latitude, longitude):
    # Tropical ascendant
    houses, ascmc = swe.houses(jd, latitude, longitude, b'P')
    tropical_asc = ascmc[0]

    # Convert to sidereal ascendant
    ayanamsa = swe.get_ayanamsa(jd)
    sidereal_asc = (tropical_asc - ayanamsa) % 360

    return sidereal_asc


def assign_houses(chart, ascendant_longitude):
    asc_sign_index = int(ascendant_longitude // 30)

    for planet, data in chart.items():
        planet_sign_index = int(data["longitude"] // 30)

        # Whole sign house calculation
        house = (planet_sign_index - asc_sign_index) % 12 + 1
        data["house"] = house

    return chart


