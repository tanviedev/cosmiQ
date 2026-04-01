def map_transits_to_houses(transits, natal_chart, asc_lon):

    asc_sign = int(asc_lon // 30)

    results = {}

    for planet, data in transits.items():
        sign_index = int(data["longitude"] // 30)

        house = (sign_index - asc_sign) % 12 + 1

        results[planet] = {
            "sign": data["sign"],
            "house": house
        }

    return results