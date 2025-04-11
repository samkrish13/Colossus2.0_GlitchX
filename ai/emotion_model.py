
from fer import FER
import cv2

def detect_emotion(frame):
    detector = FER()
    emotion, score = detector.top_emotion(frame)
    return emotion, score
