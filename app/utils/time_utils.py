# app/utils/time_utils.py

from datetime import datetime
import pytz

def to_utc(date_str, time_str, timezone_str):
    local_tz = pytz.timezone(timezone_str)
    dt = datetime.strptime(
        f"{date_str} {time_str}",
        "%Y-%m-%d %H:%M:%S"
    )
    local_dt = local_tz.localize(dt)
    return local_dt.astimezone(pytz.utc)
