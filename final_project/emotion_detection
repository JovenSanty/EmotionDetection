import requests
import json
def emotion_detector(text_to_analyse):
    """
    Detecta emociones en el texto usando la API EmotionPredict de Watson NLP.
    Args:
        text_to_analyse (str): Texto a analizar.
    Returns:
        dict: Diccionario con puntajes de emociones y la emoción dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {
        "raw_document": {
            "text": text_to_analyse}}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_dict = response.json()
        emotions = response_dict['emotionPredictions'][0]['emotion']
        anger_score   = emotions.get('anger', 0.0)
        disgust_score = emotions.get('disgust', 0.0)
        fear_score    = emotions.get('fear', 0.0)
        joy_score     = emotions.get('joy', 0.0)
        sadness_score = emotions.get('sadness', 0.0)
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score}
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}
        return result
    except requests.exceptions.RequestException as e:
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'error',
            'error_message': str(e)}
    except (KeyError, IndexError, TypeError) as e:
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'unknown',
            'error_message': f"Formato de respuesta inesperado: {str(e)}"}
