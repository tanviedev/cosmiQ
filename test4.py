# test4.py

from datetime import datetime
from app.astrology.birth_chart import calculate_chart
from app.astrology.vimshottariEngine.mahadasha import calculate_vimshottari

if __name__ == "__main__":

    chart = calculate_chart(
        name="Test User",
        dob="2005-10-01",
        time="15:57:00",
        timezone="Asia/Kolkata",
        latitude=19.0760,
        longitude=72.8777
    )

    birth_dt = datetime(2005, 10, 1, 15, 57)

    dashas = calculate_vimshottari(chart, birth_dt)

    print("\n--- VIMSHOTTARI MAHADASHA ---\n")

    for d in dashas:
        print(
            f"{d['lord']:8} | "
            f"{d['start']} → {d['end']} | "
            f"{d['years']} years"
        )
