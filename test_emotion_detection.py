import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am so happy and grateful today!")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I feel empty and depressed.")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_anger(self):
        result = emotion_detector("I hate when this happens.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_fear(self):
        result = emotion_detector("I’m terrified this might happen again.")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_blank_input(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
