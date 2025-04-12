from fer import FER
import cv2

detector = FER(mtcnn=True)

def detect_emotion(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = detector.top_emotion(rgb)
    return result if result else ("neutral", 0)
