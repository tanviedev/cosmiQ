from datetime import timedelta
from .constants import DASHA_YEARS, NAK_LEN
from .utils import years_to_days, rotate_dasha

def calculate_antardasha(md_lord, md_start, md_years):
    antars = []
    order = rotate_dasha(md_lord)
    current = md_start

    for antar in order:
        antar_years = md_years * DASHA_YEARS[antar] / 120
        days = years_to_days(antar_years)
        end = current + timedelta(days=days)

        antars.append({
            "antardasha": antar,
            "start": current,
            "end": end
        })

        current = end

    return antars
