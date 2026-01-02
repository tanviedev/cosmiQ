from app.llm.astro_context import build_astro_context
from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import get_astrology_reading
from app.astrology.aspects import calculate_aspects
from test1 import generate_chart


chart = generate_chart(
    name="Test User",
    dob="2005-10-01",
    time="15:57:00",
    timezone="Asia/Kolkata",
    latitude=19.0760,
    longitude=72.8777
)

aspects = calculate_aspects(chart)

astro_context = build_astro_context(chart, aspects)

prompt = build_prompt(
    astro_context,
    user_question="Tell me about career and education"
)

reading = get_astrology_reading(prompt)

print("\n--- ASTROLOGY READING ---\n")
print(reading)
