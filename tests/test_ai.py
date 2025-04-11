# tests/test_ai.py

import unittest
import numpy as np
import cv2
from ai.predict import analyze_frame
from ai.comprehension_model import estimate_comprehension
from ai.engagement_model import infer_engagement
from ai.emotion_model import detect_emotion

class TestAIModels(unittest.TestCase):

    def test_comprehension_estimation(self):
        text = "I totally understand the topic now!"
        score = estimate_comprehension(text)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)

    def test_engagement_score(self):
        blink_rate = 0.2
        eye_contact = 0.9
        score = infer_engagement(blink_rate, eye_contact)
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)

    def test_emotion_detection(self):
        # Create a dummy image
        frame = np.zeros((48, 48, 3), dtype=np.uint8)
        emotion, score = detect_emotion(frame)
        self.assertIsInstance(emotion, str)
        self.assertIsInstance(score, float)

    def test_analyze_frame(self):
        frame = np.zeros((48, 48, 3), dtype=np.uint8)
        result = analyze_frame(frame, "I love this lesson!", blink_rate=0.1, eye_contact=0.8)
        self.assertIn("emotion", result)
        self.assertIn("engagement_score", result)
        self.assertIn("comprehension_score", result)

if __name__ == "__main__":
    unittest.main()
