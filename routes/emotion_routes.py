
from flask import Blueprint, request, jsonify
from ai.predict import analyze_frame
from utils.helpers import log_event
import numpy as np
import cv2
import base64

emotion_routes = Blueprint('emotion_routes', __name__)

@emotion_routes.route('/analyze', methods=['POST'])
def analyze_emotion(from utils.helpers import log_event
log_event(f"Analysis completed for user: {user_id}"):
    try:
        data = request.get_json()

        # Get webcam frame and user text response
        frame_data = data.get("frame")
        text_response = data.get("text")
        user_id = data.get("user_id", "unknown")  # Optional field

        # Decode base64 image into OpenCV format
        frame_bytes = base64.b64decode(frame_data)
        np_arr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Call the AI model pipeline
        result = analyze_frame(
            frame,
            text_response,
            blink_rate=data.get("blink_rate", 0.2),       # optionally passed
            eye_contact=data.get("eye_contact", 0.8)      # optionally passed
        )

        # Log the analysis
        log_event(f"Analysis completed for user: {user_id}, Emotion: {result['emotion']}")

        return jsonify({
            "status": "success",
            "data": result
        }), 200

    except Exception as e:
        log_event(f"Error during analysis: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
