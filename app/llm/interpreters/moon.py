from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import call_llm

def interpret_moon(moon_data: dict) -> str:
    prompt = build_prompt(
        "moon_interpretation.txt",
        {
            "sign": moon_data["sign"],
            "house": moon_data["house"],
            "nakshatra": moon_data["nakshatra"],
            "nakshatra_lord": moon_data["nakshatra_lord"],
        }
    )

    return call_llm(prompt)
