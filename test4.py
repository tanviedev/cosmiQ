# test4.py

from datetime import datetime
from app.astrology.birth_chart import (
    calculate_chart,
    calculate_ascendant,
    assign_houses,
    get_julian_day
)
from app.utils.time_utils import to_utc
from app.astrology.vimshottariEngine.mahadasha import calculate_vimshottari

if __name__ == "__main__":

    # 1️⃣ Birth details
    birth_dt = to_utc("2005-10-01", "15:57:00", "Asia/Kolkata")

    # 2️⃣ Calculate planets
    chart = calculate_chart(birth_dt)

    # 3️⃣ Ascendant
    jd = get_julian_day(birth_dt)
    asc_lon = calculate_ascendant(jd, 19.0760, 72.8777)

    # 4️⃣ MUST enrich chart before Vimshottari
    chart = assign_houses(chart, asc_lon)

    # 5️⃣ Vimshottari
    dashas = calculate_vimshottari(chart, birth_dt)

    # 6️⃣ Print
    print("\n--- VIMSHOTTARI DASHA ---\n")

    for md in dashas:
        print(
            f"{md['planet']} Mahadasha | "
            f"{md['start'].date()} → {md['end'].date()}"
        )

        for ad in md["antardashas"]:
            print(
                f"   └─ {ad['planet']} Antardasha | "
                f"{ad['start'].date()} → {ad['end'].date()}"
            )

        print()
