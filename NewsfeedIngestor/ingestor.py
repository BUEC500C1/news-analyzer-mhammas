import logging

def search_by_keyword(keyword):
	if keyword is None:
		logging.info("No Keyword Specified")
		return {"status": 404, "message": "No Keyword Specified"}

	keyword = str(keyword)

	return {"articles": [1, 2, 3, 4, 5], "status": 200}