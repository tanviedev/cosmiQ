# app/astrology/vimshottariEngine/mahadasha.py

from datetime import timedelta
from .constants import DASHA_YEARS, VIMSHOTTARI_ORDER
from .utils import get_nakshatra_index, get_dasha_lord

NAKSHATRA_SPAN = 13 + 20/60  # 13°20′ = 13.333...

def calculate_vimshottari(chart, birth_dt):
    moon = chart["Moon"]

    nak_name = moon["nakshatra"]
    moon_deg = moon["degree"]

    # 1️⃣ Nakshatra index
    nak_index = get_nakshatra_index(nak_name)

    # 2️⃣ Mahadasha lord
    md_lord = get_dasha_lord(nak_index)

    # 3️⃣ Balance of first Mahadasha
    progressed = moon_deg / NAKSHATRA_SPAN
    total_years = DASHA_YEARS[md_lord]
    balance_years = total_years * (1 - progressed)

    # 4️⃣ Build timeline
    dashas = []
    current_date = birth_dt

    start_idx = VIMSHOTTARI_ORDER.index(md_lord)

    for i in range(9):
        lord = VIMSHOTTARI_ORDER[(start_idx + i) % 9]
        years = DASHA_YEARS[lord]

        if i == 0:
            years = balance_years

        days = int(years * 365.25)
        end_date = current_date + timedelta(days=days)

        dashas.append({
            "lord": lord,
            "start": current_date.date(),
            "end": end_date.date(),
            "years": round(years, 2)
        })

        current_date = end_date

    return dashas
