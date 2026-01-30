from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a classical Vedic astrology interpreter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,   # 🔒 LOW = less hallucination
    )

    return response.choices[0].message.content.strip()
