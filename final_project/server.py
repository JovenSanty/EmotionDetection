from flask import Flask, request
import json
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyse = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyse)
    
    # Si es entrada en blanco → status 400 + diccionario con None
    if response.get('dominant_emotion') is None:
        return json.dumps(response), 400
    
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)