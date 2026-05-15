from app.llm.intent_detection.intent_classifier import (
    classify_intent_llm
)

from app.astrology.interpreter_engine.reason_builder import (
    build_reasoning
)

from app.rag.query_builder import (
    build_rag_query
)

from app.rag.retriever import (
    search_knowledge_base
)

from app.llm.prompt_builder import (
    build_prompt
)

from app.llm.llm_client import (
    call_llm
)

# -----------------------------------
# MAIN AGENT
# -----------------------------------

def ask_cosmiq(
    question,
    chart,
    dashas,
    aspects=None
):

    # -----------------------------------
    # 1️⃣ INTENT DETECTION
    # -----------------------------------

    intent = classify_intent_llm(question)

    print(f"\nDETECTED INTENT: {intent}")

    # -----------------------------------
    # 2️⃣ STRUCTURED REASONING
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

        return (
            "Insufficient astrological evidence."
        )

    # -----------------------------------
    # 3️⃣ FORMAT REASONING
    # -----------------------------------

    reasoning_text = "\n".join([
        f"- {str(r)}"
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
        query=rag_query,
        reasoning=reasoning_list,
        top_k=5
    )

    print("\nRAG RESULTS:")
    print(rag_results)

    # -----------------------------------
    # 6️⃣ FORMAT RAG
    # -----------------------------------

    rag_text = "\n".join([

        f"- {r['text']}"

        for r in rag_results

    ])

    # -----------------------------------
    # 7️⃣ BUILD PROMPT
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