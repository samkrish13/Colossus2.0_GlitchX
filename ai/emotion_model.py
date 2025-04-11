from fer import FER
import cv2

# Load the emotion detector model once
detector = FER(mtcnn=True)

def detect_emotion(frame):
 
    emotion, score = detector.top_emotion(frame)
    return emotion, score
