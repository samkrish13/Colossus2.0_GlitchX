# adaptive_response.py

def adapt_response(emotion, comprehension_score, raw_response):

    if emotion in ["sad", "angry", "confused"] or comprehension_score < 0.5:
        return simplify_response(raw_response)
    elif emotion in ["happy", "surprised"] and comprehension_score >= 0.7:
        return raw_response
    else:
        return clarify_response(raw_response)

def simplify_response(text):
    sentences = text.split(".")
    simplified = ". ".join(sentences[:2]) + "..." if len(sentences) > 2 else text
    return f"Let's break it down:\n{simplified}"

def clarify_response(text):
   
    return f"{text}\n\nLet me know which part you'd like more clarity on!"
