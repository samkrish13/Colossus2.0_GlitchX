def infer_engagement(blink_rate, eye_contact):

    score = max(0, min(1, (eye_contact * 0.7 + (1 - blink_rate) * 0.3)))
    return round(score, 2)
