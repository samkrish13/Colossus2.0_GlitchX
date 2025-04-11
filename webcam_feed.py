import cv2
from ai.emotion_model import detect_emotion

cap = cv2.VideoCapture(0)  # Use webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotion, score = detect_emotion(frame)
    label = f"{emotion}: {score:.2f}" if emotion else "No Face Detected"

    # Display the label on the frame
    cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
