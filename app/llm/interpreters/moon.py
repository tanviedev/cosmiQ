from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import call_llm

def interpret_moon(chart: dict) -> str:
    moon = chart["Moon"]

    prompt = build_prompt(
        "moon.txt",
        {
            "sign": moon["sign"],
            "house": moon["house"],
            "nakshatra": moon["nakshatra"],
            "nakshatra_lord": moon["nakshatra_lord"]
        }
    )

    return call_llm(prompt)