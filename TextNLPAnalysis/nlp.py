import logging

def get_sentiment(text):
	if text is None:
		logging.info("Text Not Given")
		return {"status": 404, "message": "Text Not Given"}
	
	logging.info("Sentiment Calculated")
	return {"sentiment": 0.5, "status": 200}