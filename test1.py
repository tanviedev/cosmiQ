from app.astrology.birth_chart import *
from app.astrology.nakshatra import get_nakshatra
from app.utils.time_utils import to_utc
from app.astrology.aspects import calculate_aspects


if __name__ == "__main__":

    utc_dt = to_utc("2005-10-01", "15:57:00", "Asia/Kolkata")

    chart = calculate_chart(utc_dt)

    jd = get_julian_day(utc_dt)
    asc_lon = calculate_ascendant(jd, 19.0760, 72.8777)

    assign_houses(chart, asc_lon)

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

# 8️⃣ Calculate Graha Drishti
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
