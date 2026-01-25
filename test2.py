# test2.py

from app.astrology.drishti_engine import interpret_drishti
from app.astrology.report_formatter import format_drishti_report

# Extracted from your existing output
drishti_planet_map = {
    "Sun": ["Mars"],
    "Moon": ["Rahu"],
    "Mars": ["Moon"],
    "Jupiter": ["Rahu", "Saturn"],
    "Saturn": ["Jupiter", "Venus"],
    "Rahu": ["Jupiter", "Moon", "Venus"],
    "Ketu": ["Mars"]
}

interpretations = interpret_drishti(drishti_planet_map)
format_drishti_report(interpretations)
