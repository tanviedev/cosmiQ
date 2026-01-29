# test2.py

from app.astrology.drishtiEngine.drishti_interpreter import interpret_drishti
from app.astrology.drishtiEngine.report_formatter import format_drishti_report

# -----------------------------------------
# MOCKED OUTPUT OF calculate_aspects(chart)
# (This mimics REAL engine output)
# -----------------------------------------

drishti_data = {
    "Sun": {
        "aspect_planets": ["Mars"],
        "aspect_houses": [4]
    },
    "Moon": {
        "aspect_planets": ["Rahu"],
        "aspect_houses": [3]
    },
    "Mars": {
        "aspect_planets": ["Moon"],
        "aspect_houses": [8, 11, 12]
    },
    "Jupiter": {
        "aspect_planets": ["Rahu", "Saturn"],
        "aspect_houses": [3, 5, 7]
    },
    "Saturn": {
        "aspect_planets": ["Jupiter", "Venus"],
        "aspect_houses": [2, 5, 10]
    },
    "Rahu": {
        "aspect_planets": ["Jupiter", "Moon", "Venus"],
        "aspect_houses": [8, 10, 12]
    },
    "Ketu": {
        "aspect_planets": ["Mars"],
        "aspect_houses": [2, 4, 6]
    }
}

# -----------------------------------------
# INTERPRET
# -----------------------------------------

interpretations = interpret_drishti(drishti_data)

# -----------------------------------------
# FORMAT OUTPUT
# -----------------------------------------

format_drishti_report(interpretations)
