import unittest
from emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_alegría(self):
        result = emotion_detector("Me alegra que esto haya sucedido")
        self.assertEqual(result["dominant_emotion"], "joy")   # alegría → joy
        def test_ira(self):
        result = emotion_detector("Estoy realmente enojado por esto")
        self.assertEqual(result["dominant_emotion"], "anger")  # ira → anger
    def test_desagrado(self):
        result = emotion_detector("Me siento disgustado solo de oír sobre esto")
        self.assertEqual(result["dominant_emotion"], "disgust")  # desagrado → disgust
    def test_tristeza(self):
        result = emotion_detector("Estoy tan triste por esto")
        self.assertEqual(result["dominant_emotion"], "sadness")  # tristeza → sadness
    def test_miedo(self):
        result = emotion_detector("Tengo mucho miedo de que esto suceda")
        self.assertEqual(result["dominant_emotion"], "fear")   # miedo → fear
if name == 'main':
    print("🚀 Ejecutando pruebas unitarias para Emotion Detection...\n")
    unittest.main(verbosity=2)
    EOF