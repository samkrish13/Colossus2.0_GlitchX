
from keras.models import load_model
import numpy as np
import cv2

model = load_model("ai/model_weights/emotion_model.h5")
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(gray, (48, 48))  # FER2013 uses 48x48 grayscale
    face = face.reshape(1, 48, 48, 1) / 255.0

    predictions = model.predict(face)
    top_emotion = emotion_labels[np.argmax(predictions)]
    score = float(np.max(predictions))
    
    return top_emotion, score

