import logging

def get_sentiment(record, paragraph):
	if record is None:
		logging.info("Record Not Found")
		return {"status": 404, "message": "Record Not Found"}
	if paragraph is None:
		logging.info("Paragraph Not Found")
		return {"status": 404, "message": "Paragraph Not Found"}
	if paragraph < 1:
		logging.info("Wrong Paragraph Number")
		return {"status": 404, "message": "Wrong Paragraph Number"}
	#if paragraph > 100:
	#	logging.info("Paragraph Number Exceeds Text Paragraphs")
	#	return {"status": 404, "message": "Paragraph Number Exceeds Text Paragraphs"}

	logging.info("Sentiment Calculated")
	return {"sentiment": 0.5, "status": 200}