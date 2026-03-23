from flask import Flask, request
from emotion_detection import emotion_detector  # Importa tu función existente

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyse = request.args.get('textToAnalyze')
    
    if not text_to_analyse:
        return "No text provided", 400  # Opcional: manejo básico de error
    
    response = emotion_detector(text_to_analyse)
    
    # Formato EXACTO del ejemplo: JSON con floats y comillas
    formatted_response = (
        f'{{"anger": {response["anger"]}, '
        f'"disgust": {response["disgust"]}, '
        f'"fear": {response["fear"]}, '
        f'"joy": {response["joy"]}, '
        f'"sadness": {response["sadness"]}, '
        f'"dominant_emotion": "{response["dominant_emotion"]}"}}'
    )
    
    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)