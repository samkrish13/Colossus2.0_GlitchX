# routes/learning_routes.py

from flask import Blueprint, request, jsonify
from ai.predict import analyze_frame
from ai.adaptive_response import adapt_response
from ai.openai_gpt import get_gpt_response
import numpy as np
import cv2
import base64

learning_routes = Blueprint("learning_routes", __name__)

@learning_routes.route("/adaptive-answer", methods=["POST"])
def adaptive_answer():
    data = request.get_json()
    frame_data = data.get("frame")
    question = data.get("question")

    if not frame_data or not question:
        return jsonify({"error": "Missing frame or question"}), 400

    # Decode image
    try:
        frame_bytes = base64.b64decode(frame_data)
        np_arr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        return jsonify({"error": "Failed to decode frame", "details": str(e)}), 500

    # Analyze emotion and comprehension
    analysis = analyze_frame(frame, question)

    # Generate GPT response
    gpt_answer = get_gpt_response(question)

    # Adapt response based on emotion/comprehension
    final_response = adapt_response(
        emotion=analysis["emotion"],
        comprehension_score=analysis["comprehension_score"],
        raw_response=gpt_answer
    )

    return jsonify({
        "emotion": analysis["emotion"],
        "comprehension_score": analysis["comprehension_score"],
        "response": final_response
    })
