from app.llm.interpreters.moon import interpret_moon

moon_data = {
    "sign": "Leo",
    "house": 8,
    "nakshatra": "Purva Phalguni",
    "nakshatra_lord": "Venus"
}

print("\n--- MOON INTERPRETATION ---\n")
print(interpret_moon(moon_data))
