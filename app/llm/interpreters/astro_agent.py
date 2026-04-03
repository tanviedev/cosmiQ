from app.llm.intent_mapper import map_question_to_intent
from app.astrology.interpreter_engine.reason_builder import build_reasoning
from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import call_llm


def ask_cosmiq(question, chart, dashas):

    # 1️⃣ detect intent
    intent = map_question_to_intent(question)

    # 2️⃣ build reasoning
    reasoning_list = build_reasoning(intent, chart, dashas)

    # 3️⃣ format reasoning
    reasoning_text = "\n".join([f"- {r}" for r in reasoning_list])

    # 4️⃣ build prompt
    prompt = build_prompt("base.txt", {
        "question": question,
        "reasoning": reasoning_text
    })

    # 5️⃣ call LLM
    return call_llm(prompt)