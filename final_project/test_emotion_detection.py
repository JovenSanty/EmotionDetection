import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_alegria(self):
        texto_es = "Me alegra que esto haya sucedido"
        texto_en = "I'm glad this happened"  # traducción manual
        result = emotion_detector(texto_en)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_ira(self):
        texto_es = "Estoy realmente enojado por esto"
        texto_en = "I'm really angry about this"
        result = emotion_detector(texto_en)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_desagrado(self):
        texto_es = "Me siento disgustado solo de oír sobre esto"
        texto_en = "I feel disgusted just hearing about this"
        result = emotion_detector(texto_en)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_tristeza(self):
        texto_es = "Estoy tan triste por esto"
        texto_en = "I'm so sad about this"
        result = emotion_detector(texto_en)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_miedo(self):
        texto_es = "Tengo mucho miedo de que esto suceda"
        texto_en = "I'm very afraid this will happen"
        result = emotion_detector(texto_en)
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == '__main__':
    print("🚀 Ejecutando pruebas unitarias para Emotion Detection (con traducción a inglés)...\n")
    unittest.main(verbosity=2)