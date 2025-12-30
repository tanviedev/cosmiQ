# app/astrology/location.py

CITY_CACHE = {
    "Mumbai, India": (19.0760, 72.8777),
    "Delhi, India": (28.6139, 77.2090),
    "Pune, India": (18.5204, 73.8567),
    "London, UK": (51.5074, -0.1278),
}

def get_coordinates(place_name=None, latitude=None, longitude=None):
    if latitude is not None and longitude is not None:
        return latitude, longitude

    if place_name in CITY_CACHE:
        return CITY_CACHE[place_name]

    raise ValueError(
        "Location not found. Provide latitude & longitude explicitly."
    )
