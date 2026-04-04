from app.astrology.birth_chart import (
    calculate_chart,
    calculate_ascendant,
    assign_houses,
    get_julian_day,
    get_sign
)
from app.astrology.nakshatra import get_nakshatra
from app.utils.time_utils import to_utc
from app.astrology.drishtiEngine.aspects import calculate_aspects


if __name__ == "__main__":

    # 1️⃣ Convert birth time → UTC
    utc_dt = to_utc("2005-10-01", "15:57:00", "Asia/Kolkata")

    # 2️⃣ Planetary positions
    chart = calculate_chart(utc_dt)

    # 3️⃣ Ascendant
    jd = get_julian_day(utc_dt)
    asc_lon = calculate_ascendant(jd, 19.0760, 72.8777)

    # 4️⃣ Assign houses + nakshatra
    chart = assign_houses(chart, asc_lon)

    # 5️⃣ Add Ascendant
    asc = {
        "longitude": round(asc_lon, 2),
        "sign": get_sign(asc_lon),
        "degree": round(asc_lon % 30, 2),
        "house": 1
    }
    asc.update(get_nakshatra(asc_lon))
    chart["Ascendant"] = asc

    print("\n--- VEDIC BIRTH CHART ---\n")

    for p, d in chart.items():
        print(
            f"{p:10} | "
            f"Sign: {d['sign']:11} | "
            f"Deg: {d['degree']:5} | "
            f"House: {d['house']:2} | "
            f"Nakshatra: {d['nakshatra']:15} | "
            f"Pada: {d['pada']} | "
            f"Lord: {d['nakshatra_lord']}"
        )

    # 6️⃣ Graha Drishti
    aspects = calculate_aspects(chart)

    print("\n--- GRAHA DRISHTI (ASPECTS) ---\n")

    for planet, info in aspects.items():
        houses = ", ".join(str(h) for h in info["aspect_houses"])
        planets = ", ".join(info["aspect_planets"]) if info["aspect_planets"] else "None"

        print(
            f"{planet:10} | "
            f"Aspects Houses: {houses:10} | "
            f"Aspects Planets: {planets}"
        )
