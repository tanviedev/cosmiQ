from app.astrology.birth_chart import (
    calculate_chart,
    calculate_ascendant,
    assign_houses,
    get_julian_day,
    get_sign
)

from app.astrology.nakshatra import get_nakshatra
from app.astrology.drishtiEngine.aspects import calculate_aspects
from app.astrology.drishtiEngine.drishti_interpreter import interpret_drishti
from app.astrology.dispositorEngine.chart_enricher import enrich_with_dispositors
from app.astrology.vimshottariEngine.mahadasha import calculate_vimshottari

from app.utils.time_utils import to_utc


def generate_full_chart(dob, time, timezone, lat, lon):
    
    # 1️⃣ UTC
    utc_dt = to_utc(dob, time, timezone)

    # 2️⃣ Base chart
    chart = calculate_chart(utc_dt)

    # 3️⃣ Ascendant
    jd = get_julian_day(utc_dt)
    asc_lon = calculate_ascendant(jd, lat, lon)

    # 4️⃣ Houses
    chart = assign_houses(chart, asc_lon)

    # 5️⃣ Add nakshatra to planets (IMPORTANT)
    for planet, data in chart.items():
        data.update(get_nakshatra(data["longitude"]))

    # 6️⃣ Add Ascendant
    asc = {
        "longitude": round(asc_lon, 2),
        "sign": get_sign(asc_lon),
        "degree": round(asc_lon % 30, 2),
        "house": 1
    }
    asc.update(get_nakshatra(asc_lon))
    chart["Ascendant"] = asc

    # 7️⃣ Dispositors
    chart = enrich_with_dispositors(chart)

    # 8️⃣ Aspects
    aspects = calculate_aspects(chart)

    # 9️⃣ Drishti interpretation (rule-based, NOT LLM)
    drishti_text = interpret_drishti(aspects)

    # 🔟 Vimshottari
    dashas = calculate_vimshottari(chart, utc_dt)

    return {
        "chart": chart,
        "aspects": aspects,
        "drishti": drishti_text,
        "dashas": dashas
    }