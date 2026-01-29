# app/astrology/vimshottariEngine/utils.py

from .constants import NAKSHATRAS, VIMSHOTTARI_ORDER

def get_nakshatra_index(nakshatra_name):
    if nakshatra_name not in NAKSHATRAS:
        raise ValueError(f"Unknown Nakshatra: {nakshatra_name}")
    return NAKSHATRAS.index(nakshatra_name)

def get_dasha_lord(nak_index):
    return VIMSHOTTARI_ORDER[nak_index % 9]
