import json
import os

PROCESSED_DIR = "data/processed"

def log_result(result_dict):
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.json"
    with open(os.path.join(PROCESSED_DIR, filename), "w") as f:
        json.dump(result_dict, f)

from ai.emotion_model import detect_emotion
from ai.engagement_model import infer_engagement
from ai.comprehension_model import estimate_comprehension

def analyze_frame(frame, text_response, blink_rate=0.2, eye_contact=0.8):
    emotion, emotion_score = detect_emotion(frame)
    engagement_score = infer_engagement(blink_rate, eye_contact)
    comprehension_score = estimate_comprehension(text_response)
    
    return {
        "emotion": emotion,
        "emotion_score": emotion_score,
        "engagement_score": engagement_score,
        "comprehension_score": comprehension_score
    }
