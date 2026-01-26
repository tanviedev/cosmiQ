from app.astrology.birth_chart import (
    calculate_chart,
    calculate_ascendant,
    assign_houses,
    get_julian_day,
    get_sign
)

from app.astrology.chart_enricher import enrich_with_dispositors
from app.utils.time_utils import to_utc
from app.astrology.nakshatra import get_nakshatra
from app.astrology.rasi_lords import RASI_LORDS

def generate_chart(
    name,
    dob,
    time,
    timezone,
    latitude,
    longitude
):
    # 1️⃣ Convert local birth time → UTC
    utc_dt = to_utc(dob, time, timezone)

    # 2️⃣ Planetary positions (sidereal)
    chart = calculate_chart(utc_dt)

    # 3️⃣ Julian Day
    jd = get_julian_day(utc_dt)

    # 4️⃣ Ascendant (sidereal)
    asc_lon = calculate_ascendant(jd, latitude, longitude)

    # 5️⃣ Assign houses (whole sign Vedic)
    chart = assign_houses(chart, asc_lon)

    # 6️⃣ Enrich with dispositor logic
    chart = enrich_with_dispositors(chart)

    # 7️⃣ Add Ascendant
    asc = {
        "longitude": round(asc_lon, 2),
        "sign": get_sign(asc_lon),
        "degree": round(asc_lon % 30, 2),
        "house": 1
    }
    asc.update(get_nakshatra(asc_lon))
    chart["Ascendant"] = asc

    return chart


# --------------------------------------------------
# TEST RUN
# --------------------------------------------------

if __name__ == "__main__":

    chart = generate_chart(
        name="Test User",
        dob="2005-10-01",
        time="15:57:00",
        timezone="Asia/Kolkata",
        latitude=19.0760,   # Mumbai
        longitude=72.8777
    )

    print("\n--- VEDIC BIRTH CHART (WITH DISPOSITORS) ---\n")

    for planet, data in chart.items():

       lord = RASI_LORDS.get(data["sign"], "—")

       print(
        f"{planet:10} | "
        f"Sign: {data['sign']:11} | "
        f"Deg: {data['degree']:5} | "
        f"House: {data['house']:2} | "
        f"Nakshatra: {data['nakshatra']:15} | "
        f"Pada: {data['pada']} | "
        f"Rāśi Lord: {lord}"
       )

       if "dispositor" in data:
        d = data["dispositor"]
        print(
            f"{'':10} | Dispositor → {d['dispositor']} | "
            f"Sign: {d['dispositor_sign']} | "
            f"House: {d['dispositor_house']} | "
            f"Strength: {d['dispositor_strength_hint']}"
        )

       print()
