import json
from app.llm.vedic_knowledge import VEDIC_RULES


def build_prompt(astro_context, user_question=None):
    base_prompt = f"""
{VEDIC_RULES}

Below is the birth chart data (already calculated accurately).

ASTROLOGY DATA (JSON):
{json.dumps(astro_context, indent=2)}

"""

    if user_question:
        base_prompt += f"""
USER QUESTION:
{user_question}

Respond using classical Vedic astrology logic.
"""

    else:
        base_prompt += """
Provide a general life overview based on:
- Ascendant
- Strong planets
- Major aspects
"""

    return base_prompt
