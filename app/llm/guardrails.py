def is_valid_question(intent, question):
    q = question.lower()

    # 🚫 Non-astrology / inappropriate
    banned = ["color", "dress", "what should i wear", "funeral"]

    if any(word in q for word in banned):
        return False, "This question is outside the scope of astrological analysis."

    # 🚫 Empty / vague
    if len(q.strip()) < 5:
        return False, "Please ask a more specific question."

    return True, None