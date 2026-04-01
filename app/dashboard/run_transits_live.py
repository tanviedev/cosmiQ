import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import time
from export_transits import export_transits
import app.astrology.birth_chart
from app.utils.time_utils import to_utc # pyright: ignore[reportMissingImports]

# generate natal chart once
utc_dt = to_utc("2005-10-01", "15:57:00", "Asia/Kolkata")

chart = app.astrology.birth_chart.calculate_chart(utc_dt)
jd = app.astrology.birth_chart.get_julian_day(utc_dt)
asc_lon = app.astrology.birth_chart.calculate_ascendant(jd, 19.0760, 72.8777)

app.astrology.birth_chart.assign_houses(chart, asc_lon)

print("🔄 Running live transit updates...")

while True:
    export_transits(chart, asc_lon)
    time.sleep(60)   # update every 60 seconds