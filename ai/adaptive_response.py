def adapt_response(emotion, comprehension_score, raw_response):
    """
    Adapts AI response based on emotion and understanding.

    Args:
        emotion (str): Detected emotion (e.g., sad, happy, confused)
        comprehension_score (float): Value between 0–1
        raw_response (str): Original GPT response

    Returns:
        str: Modified/adapted explanation
    """
    if emotion in ["sad", "angry", "confused"] or comprehension_score < 0.5:
        return simplify_response(raw_response)
    elif emotion in ["happy", "surprised"] and comprehension_score >= 0.7:
        return raw_response
    else:
        return clarify_response(raw_response)

def simplify_response(text):
    return "Let’s simplify this:\n" + "\n".join(text.split(".")[:2]) + "..."

def clarify_response(text):
    return text + "\n\nLet me know which part you want more clarity on!"
