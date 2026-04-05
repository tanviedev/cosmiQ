from app.llm.llm_client import call_llm

ALLOWED_INTENTS = {
    "career",
    "relationship",
    "mental",
    "career_decision",
    "general"
}


def classify_intent_llm(question: str) -> str:
  try:
    prompt = f"""
You are an intent classifier for an astrology AI system.

Classify the user's question into ONE of these intents:

- career
- relationship
- mental
- career_decision
- general

Rules:
- Output ONLY the intent (one word)
- No explanation
- No extra text

Question: {question}
"""

    response = call_llm(prompt).strip().lower()

    # 🔒 GUARDRAIL
    if response not in ALLOWED_INTENTS:
        return "general"

    return response

  except Exception:
    return "general"