from app.astrology.dispositor import get_dispositor

def enrich_with_dispositors(chart):
    for planet, data in chart.items():
        if planet == "Ascendant":
            continue

        dispositor = get_dispositor(planet, data, chart)
        if dispositor:
            data["dispositor"] = dispositor

    return chart
