""" This package allows to make a request to the Watson API to get the
    sentiment analysis of a provided string.
"""
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """ Runs a sentiment analysis of the provided string making a POST
        request to the Watson API.
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/' \
          'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {"label": label, "score": score}
