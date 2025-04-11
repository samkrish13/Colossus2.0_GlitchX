# routes/emotion_routes.py

from flask import Blueprint, request, jsonify
from ai.predict import analyze_frame
import numpy as np
import cv2
import base64

emotion_routes = Blueprint("emotion_routes", __name__)

@emotion_routes.route("/analyze", methods=["POST"])
def analyze_emotion():
    data = request.get_json()
    frame_data = data.get("frame")
    text_response = data.get("text") or ""

    if not frame_data:
        return jsonify({"error": "No frame provided"}), 400

    # Convert base64 frame to image
    try:
        frame_bytes = base64.b64decode(frame_data)
        np_arr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        return jsonify({"error": "Failed to decode frame", "details": str(e)}), 500

    # Analyze frame + optional text for comprehension
    result = analyze_frame(frame, text_response)
    return jsonify(result)
