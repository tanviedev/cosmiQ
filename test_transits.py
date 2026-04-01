from app.astrology.birth_chart import *
from app.utils.time_utils import to_utc
from dashboard.transits import get_transits
from dashboard.transit_mapper import map_transits_to_houses

utc_dt = to_utc("2005-10-01", "15:57:00", "Asia/Kolkata")

chart = calculate_chart(utc_dt)

jd = get_julian_day(utc_dt)
asc_lon = calculate_ascendant(jd, 19.0760, 72.8777)

assign_houses(chart, asc_lon)

transits = get_transits()
mapped = map_transits_to_houses(transits, chart, asc_lon)

print("\n--- CURRENT TRANSITS ---\n")

for p, d in mapped.items():
    print(f"{p:10} | Sign: {d['sign']:10} | House: {d['house']}")