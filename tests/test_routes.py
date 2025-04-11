# tests/test_routes.py

import unittest
import json
from app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_estimate_route(self):
        response = self.client.post('/api/learn/estimate', json={"text": "I understood everything"})
        data = json.loads(response.data)
        self.assertIn("comprehension_score", data)
        self.assertGreaterEqual(data["comprehension_score"], 0)

    def test_adaptive_answer(self):
        # Dummy base64 encoded black image
        import base64
        import numpy as np
        import cv2
        dummy_frame = cv2.imencode('.jpg', np.zeros((48, 48, 3), dtype=np.uint8))[1].tobytes()
        encoded = base64.b64encode(dummy_frame).decode('utf-8')

        payload = {
            "frame": encoded,
            "question": "Explain Newton's Third Law"
        }

        response = self.client.post('/api/learn/adaptive-answer', json=payload)
        data = json.loads(response.data)

        self.assertIn("emotion", data)
        self.assertIn("response", data)

if __name__ == "__main__":
    unittest.main()
