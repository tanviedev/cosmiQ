import pandas as pd
from  transits import get_transits
from  transit_mapper import map_transits_to_houses

def export_transits(natal_chart, asc_lon):

    transits = get_transits()
    mapped = map_transits_to_houses(transits, natal_chart, asc_lon)

    rows = []

    for planet, data in mapped.items():
        rows.append({
            "planet": planet,
            "current_sign": data["sign"],
            "current_house": data["house"]
        })

    df = pd.DataFrame(rows)
    df.to_csv("transits.csv", index=False)

    print("✅ Exported transits.csv")