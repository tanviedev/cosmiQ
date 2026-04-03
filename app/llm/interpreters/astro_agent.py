from app.llm.intent_mapper import map_question_to_intent
from app.astrology.interpreter_engine.reason_builder import build_reasoning
from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import call_llm
from app.llm.guardrails import is_valid_question


def ask_cosmiq(question, chart, dashas):

    # 1️⃣ intent
    intent = map_question_to_intent(question)

    # 2️⃣ 🚨 GUARD CHECK
    valid, message = is_valid_question(intent, question)
    if not valid:
        return message

    # 3️⃣ reasoning
    reasoning_list = build_reasoning(intent, chart, dashas)

    # 🚨 If no reasoning → STOP
    if not reasoning_list:
        return "I don’t have enough astrological evidence to answer that."

    reasoning_text = "\n".join([f"- {r}" for r in reasoning_list])

    # 4️⃣ prompt
    prompt = build_prompt("base.txt", {
        "question": question,
        "reasoning": reasoning_text
    })

    # 5️⃣ LLM
    return call_llm(prompt)