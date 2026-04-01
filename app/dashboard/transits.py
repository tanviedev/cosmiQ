import swisseph as swe
from datetime import datetime

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
    "Aries","Taurus","Gemini","Cancer","Leo","Virgo",
    "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"
]


def get_sign(lon):
    return SIGNS[int(lon // 30)]


def get_transits():
    now = datetime.utcnow()
    jd = swe.julday(now.year, now.month, now.day,
                    now.hour + now.minute/60)

    transits = {}

    for name, pid in PLANETS:
        pos, _ = swe.calc_ut(jd, pid)
        lon = pos[0] % 360

        transits[name] = {
            "longitude": round(lon, 2),
            "sign": get_sign(lon),
            "degree": round(lon % 30, 2)
        }

    return transits