from NewsfeedIngestor.ingestor import * # import functions from other files
from SecureFileUploader.uploader import * # import functions from other files
from TextNLPAnalysis.nlp import * # import functions from other files

def test_create():
    assert create('test_filename') == 200
    assert create(1) == 200

def test_delete():
    assert delete('test_record') == 200
    assert delete(1) == 200

def test_update():
    assert update('test_record', 'test_text') == 200

def test_sentiment():
    assert get_sentiment('test_record', 1) == 200
    assert get_sentiment(1, 'test_record') == 200
    assert get_sentiment(1, 1) == 200

def test_search_by_keyword():
    assert search_by_keyword('test_keyword') == 200
    assert search_by_keyword(1) == 200
