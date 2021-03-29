import logging
from google.cloud import language_v1

def get_sentiment(text):
    if text is None:
        logging.info("Text Not Given")
        return {"status": 404, "message": "Text Not Given"}
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    sent_score = sentiment.score * sentiment.magnitude
    logging.info("Sentiment Calculated")
    return {"sentiment": sent_score, "status": 200}

def get_entities(text):
    if text is None:
        logging.info("Text Not Given")
        return {"status": 404, "message": "Text Not Given"}
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(request={'document': document})
    entities = []
    for entity in response.entities:
        entities.append(entity.name)
    logging.info("Entities Calculated")
    return {"entities": entities, "status": 200}

def get_entities_and_sentiment(text):
    if text is None:
        logging.info("Text Not Given")
        return {"status": 404, "message": "Text Not Given"}
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entity_sentiment(request={'document': document})
    entities = []
    for entity in response.entities:
        item = dict()
        item["Entity"] = entity.name
        item["Score"] = entity.sentiment.score * entity.sentiment.magnitude
        entities.append(item)
    logging.info("Entities Calculated")
    return {"entities": entities, "status": 200}