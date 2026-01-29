from datetime import timedelta
from .constants import DASHA_YEARS, NAK_LEN
from .utils import years_to_days, rotate_dasha
from .antardasha import calculate_antardasha

def calculate_vimshottari(chart, birth_dt):
    moon = chart["Moon"]

    nakshatra_lord = moon["nakshatra_lord"]
    moon_deg = moon["degree"]          # degree inside sign (0–30)

    # Degree inside nakshatra
    deg_in_nak = moon_deg % NAK_LEN
    frac_elapsed = deg_in_nak / NAK_LEN

    total_years = DASHA_YEARS[nakshatra_lord]
    balance_years = total_years * (1 - frac_elapsed)

    dashas = []
    current_start = birth_dt

    sequence = rotate_dasha(nakshatra_lord)

    for i, lord in enumerate(sequence):
        years = balance_years if i == 0 else DASHA_YEARS[lord]
        days = years_to_days(years)
        end = current_start + timedelta(days=days)

        antardashas = calculate_antardasha(
            lord, current_start, years
        )

        dashas.append({
            "mahadasha": lord,
            "start": current_start,
            "end": end,
            "antardashas": antardashas
        })

        current_start = end

    return dashas
