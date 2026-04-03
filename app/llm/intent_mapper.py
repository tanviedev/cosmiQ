def map_question_to_intent(question: str):
    q = question.lower()

    if any(word in q for word in ["career", "job", "work", "profession"]):
        return "career"

    elif any(word in q for word in ["relationship", "love", "partner"]):
        return "relationship"

    elif any(word in q for word in ["anxiety", "overthinking", "stress", "mind"]):
        return "mental"

    return "general"