import logging
from pynytimes import NYTAPI
import os

def search_by_keyword(keyword):
	if keyword is None:
		logging.info("No Keyword Specified")
		return {"status": 404, "message": "No Keyword Specified"}
	api_key = os.getenv("nyt_key")
	nyt = NYTAPI(str(api_key), parse_dates=True)
	keyword = str(keyword)
	articles = nyt.article_search(query=keyword,results=10,)
	ret = []
	for article in articles:
		item = dict()
		item["Summary"] = article.get('snippet')
		item["URL"] = article.get('web_url')
		ret.append(item)
	return {"articles": ret, "status": 200}