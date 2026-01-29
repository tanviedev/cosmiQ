# app/astrology/vimshottariEngine/utils.py

from app.astrology.nakshatra import NAKSHATRAS
from .constants import DASHA_ORDER, DASHA_YEARS

def normalize(name: str):
    return (
        name.lower()
        .replace(" ", "")
        .replace("-", "")
        .replace("ā", "a")
        .replace("ī", "i")
        .replace("ū", "u")
        .replace("ṛ", "r")
    )


def get_nakshatra_index(nakshatra_name):
    normalized_input = normalize(nakshatra_name)

    for idx, nak in enumerate(NAKSHATRAS):
        nak_name = nak[0]  # 👈 unpack tuple safely
        if normalize(nak_name) == normalized_input:
            return idx

    raise ValueError(f"Nakshatra '{nakshatra_name}' not found in NAKSHATRAS")


def years_to_days(years: float) -> int:
    return int(years * 365.25)


def rotate_dasha(start):
    idx = DASHA_ORDER.index(start)
    return DASHA_ORDER[idx:] + DASHA_ORDER[:idx]


def next_dasha_sequence(start_lord):
    idx = DASHA_ORDER.index(start_lord)
    return DASHA_ORDER[idx:] + DASHA_ORDER[:idx]


def antardasha_sequence(mahadasha_lord):
    return next_dasha_sequence(mahadasha_lord)


def dasha_balance_years(moon_degree_in_nakshatra):
    NAKSHATRA_SPAN = 13 + 1 / 3
    remaining = NAKSHATRA_SPAN - moon_degree_in_nakshatra
    return remaining / NAKSHATRA_SPAN
