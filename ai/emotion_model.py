from fer import FER
import cv2

detector = FER(mtcnn=True)

def detect_emotion(frame):
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect emotions
    results = detector.detect_emotions(rgb_frame)
    
    if results:
        top_emotion = detector.top_emotion(rgb_frame)
        return top_emotion  # Returns tuple (emotion, confidence)
    else:
        return None, 0
