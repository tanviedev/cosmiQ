import swisseph as swe
from app.astrology.nakshatra import get_nakshatra

# 🔴 ABSOLUTELY REQUIRED
swe.set_ephe_path(".")          # <-- CRITICAL FIX
swe.set_sid_mode(swe.SIDM_LAHIRI)

PLANETS = [
    ("Sun", swe.SUN),
    ("Moon", swe.MOON),
    ("Mars", swe.MARS),
    ("Mercury", swe.MERCURY),
    ("Jupiter", swe.JUPITER),
    ("Venus", swe.VENUS),
    ("Saturn", swe.SATURN),
    ("Rahu", swe.MEAN_NODE),
]

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def get_sign(lon):
    return SIGNS[int(lon // 30)]


def get_julian_day(dt):
    return swe.julday(
        dt.year, dt.month, dt.day,
        dt.hour + dt.minute / 60
    )


def calculate_chart(utc_dt):
    jd = get_julian_day(utc_dt)
    chart = {}

    rahu_lon = None

    for name, pid in PLANETS:
        pos, ret = swe.calc_ut(jd, pid, swe.FLG_SIDEREAL)

        # 🔴 SAFETY CHECK
        if ret < 0:
            raise RuntimeError(f"Swiss Ephemeris failed for {name}")

        lon = pos[0] % 360

        if name == "Rahu":
            rahu_lon = lon

        chart[name] = {
            "longitude": round(lon, 2),
            "sign": get_sign(lon),
            "degree": round(lon % 30, 2),
        }

    # Ketu derived AFTER Rahu
    ketu_lon = (rahu_lon + 180) % 360
    chart["Ketu"] = {
        "longitude": round(ketu_lon, 2),
        "sign": get_sign(ketu_lon),
        "degree": round(ketu_lon % 30, 2),
    }

    return chart


def calculate_ascendant(jd, lat, lon):
    _, ascmc = swe.houses(jd, lat, lon, b'P')
    asc = ascmc[0]
    ayan = swe.get_ayanamsa(jd)
    return (asc - ayan) % 360


def assign_houses(chart, asc_lon):
    asc_sign = int(asc_lon // 30)

    for body in chart:
        data = chart[body]
        body_sign = int(data["longitude"] // 30)
        house = (body_sign - asc_sign) % 12 + 1
        data["house"] = house
        data.update(get_nakshatra(data["longitude"]))

    return chart
