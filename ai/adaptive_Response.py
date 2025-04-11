def adapt_response(emotion, comprehension_score, raw_response):

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
