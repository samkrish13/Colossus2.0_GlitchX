# webcam_feed.py
from flask import Response, Blueprint
import cv2
from ai.emotion_model import detect_emotion

video_bp = Blueprint("video_bp", __name__)

@video_bp.route('/video_feed')
def video_feed():
    def generate():
        camera = cv2.VideoCapture(0)
        while True:
            success, frame = camera.read()
            if not success:
                break
            emotion, score = detect_emotion(frame)
            text = f"{emotion} ({score*100:.1f}%)"
            cv2.putText(frame, text, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
