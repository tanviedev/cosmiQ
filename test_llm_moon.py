from app.astrology.birth_chart import *
from app.utils.time_utils import to_utc
from app.astrology.nakshatra import get_nakshatra
from app.llm.interpreters.moon import interpret_moon


# STEP 1 — generate chart (same as your test1)
utc_dt = to_utc("2005-10-01", "15:57:00", "Asia/Kolkata")

chart = calculate_chart(utc_dt)

jd = get_julian_day(utc_dt)
asc_lon = calculate_ascendant(jd, 19.0760, 72.8777)

assign_houses(chart, asc_lon)

# Add nakshatra
for p in chart:
    chart[p].update(get_nakshatra(chart[p]["longitude"]))

# Add ascendant
asc = {
    "longitude": round(asc_lon, 2),
    "sign": get_sign(asc_lon),
    "degree": round(asc_lon % 30, 2),
    "house": 1
}
asc.update(get_nakshatra(asc_lon))
chart["Ascendant"] = asc


# STEP 2 — LLM Interpretation
print("\n--- MOON INTERPRETATION ---\n")
print(interpret_moon(chart))