from app.astrology.dispositorEngine.dispositor import get_dispositor

def enrich_with_dispositors(chart):
    for planet, data in chart.items():
        if planet == "Ascendant":
            continue
        d = get_dispositor(planet, data, chart)
        if d:
            data["dispositor"] = d
    return chart
