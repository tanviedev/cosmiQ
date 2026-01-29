from datetime import timedelta
from app.astrology.vimshottariEngine.constants import DASHA_YEARS, VIMSHOTTARI_ORDER
from app.astrology.vimshottariEngine.nakshatra_lords import NAKSHATRA_LORDS

def calculate_vimshottari(chart, birth_dt):
    moon = chart["Moon"]
    nak_index = moon["nakshatra_index"]
    nak_lord = NAKSHATRA_LORDS[nak_index]
    completed = moon["nakshatra_progress"]
    total_years = DASHA_YEARS[nak_lord]
    remaining = total_years * (1 - completed)

    timeline = []
    current = birth_dt
    idx = VIMSHOTTARI_ORDER.index(nak_lord)

    timeline.append(_dasha_block(nak_lord,current,remaining))
    current = timeline[-1]["end"]

    for i in range(1,len(VIMSHOTTARI_ORDER)):
        lord = VIMSHOTTARI_ORDER[(idx+i)%9]
        yrs = DASHA_YEARS[lord]
        timeline.append(_dasha_block(lord,current,yrs))
        current = timeline[-1]["end"]

    return timeline

def _dasha_block(lord,start,years):
    return {
        "lord":lord,
        "start":start,
        "end":start+timedelta(days=int(years*365.25)),
        "years":round(years,2)
    }
