from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def estimate_comprehension(text_response):
    result = classifier(text_response)[0]
    label = result["label"]
    score = result["score"]

    if label == "POSITIVE":
        return min(1.0, score + 0.1)
    return max(0.0, 1 - score)
