
from flask import Blueprint, request, jsonify
from ai.comprehension_model import estimate_comprehension

learning_routes = Blueprint('learning_routes', __name__)

@learning_routes.route('/estimate', methods=['POST'])
def estimate():
    data = request.get_json()
    response_text = data.get("text")
    score = estimate_comprehension(response_text)
    return jsonify({"comprehension_score": score})
