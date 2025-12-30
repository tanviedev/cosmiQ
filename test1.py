# test1.py

from app.astrology.birth_chart import (
    calculate_chart,
    calculate_ascendant,
    assign_houses,
    get_julian_day
)
from app.astrology.location import get_coordinates
from app.utils.time_utils import to_utc


def generate_chart(
    name,
    dob,
    time,
    timezone,
    location=None,
    latitude=None,
    longitude=None
):
    # 1️⃣ Get coordinates (offline-safe)
    lat, lon = get_coordinates(
        place_name=location,
        latitude=latitude,
        longitude=longitude
    )

    # 2️⃣ Convert local birth time → UTC
    utc_dt = to_utc(dob, time, timezone)

    # 3️⃣ Calculate planetary positions (SIDEREAL)
    chart = calculate_chart(utc_dt)

    # 4️⃣ Calculate Julian Day
    jd = get_julian_day(utc_dt)

    # 5️⃣ Calculate SIDEREAL ascendant
    ascendant_longitude = calculate_ascendant(jd, lat, lon)

    # 6️⃣ Assign houses using degree-based Vedic logic
    chart = assign_houses(chart, ascendant_longitude)

    return chart


# -----------------------------
# TEST CASE
# -----------------------------

if __name__ == "__main__":
    chart = generate_chart(
        name="Test User",
        dob="2005-10-01",
        time="15:57:00",
        timezone="Asia/Kolkata",
        latitude=19.0760,      # Mumbai
        longitude=72.8777
    )

    print("\n--- VEDIC BIRTH CHART ---\n")
    for planet, data in chart.items():
        print(
            f"{planet:8} | "
            f"Sign: {data['sign']:11} | "
            f"Deg: {data['degree']:5} | "
            f"House: {data['house']}"
        )
