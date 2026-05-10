from app.llm.intent_detection.intent_classifier import (
    classify_intent_llm
)

from app.astrology.interpreter_engine.reason_builder import (
    build_reasoning
)

from app.rag.query_builder import build_rag_query
from app.rag.retriever import search_knowledge_base

from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import call_llm


def ask_cosmiq(question, chart, dashas, aspects=None):

    # -----------------------------------
    # 1️⃣ INTENT DETECTION
    # -----------------------------------

    intent = classify_intent_llm(question)

    print(f"\nDETECTED INTENT: {intent}")

    # -----------------------------------
    # 2️⃣ STRUCTURED ASTRO REASONING
    # -----------------------------------

    reasoning_list = build_reasoning(
        intent,
        chart,
        dashas,
        aspects
    )

    print("\nREASONING:")
    print(reasoning_list)

    if not reasoning_list:
        return "Insufficient astrological evidence."

    # -----------------------------------
    # 3️⃣ FORMAT REASONING TEXT
    # -----------------------------------

    reasoning_text = "\n".join([

        f"- {r['text']}"
        if isinstance(r, dict) and "text" in r

        else f"- {str(r)}"

        for r in reasoning_list
    ])

    # -----------------------------------
    # 4️⃣ BUILD RAG QUERY
    # -----------------------------------

    rag_query = build_rag_query(
        intent,
        reasoning_list
    )

    print("\nRAG QUERY:")
    print(rag_query)

    # -----------------------------------
    # 5️⃣ RETRIEVE KNOWLEDGE
    # -----------------------------------

    rag_results = search_knowledge_base(
        rag_query,
        top_k=5
    )

    print("\nRAG RESULTS:")
    print(rag_results)

    # -----------------------------------
    # 6️⃣ FORMAT RAG CONTEXT
    # -----------------------------------

    rag_text = "\n".join([

        f"- {item['text']}"

        for item in rag_results

        if isinstance(item, dict)
        and "text" in item
    ])

    # -----------------------------------
    # 7️⃣ BUILD FINAL PROMPT
    # -----------------------------------

    prompt = build_prompt(
        "base.txt",
        {
            "question": question,
            "reasoning": reasoning_text,
            "rag_context": rag_text
        }
    )

    print("\nFINAL PROMPT:")
    print(prompt)

    # -----------------------------------
    # 8️⃣ LLM INTERPRETATION
    # -----------------------------------

    response = call_llm(prompt)

    return response