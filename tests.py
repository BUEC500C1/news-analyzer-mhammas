from NewsfeedIngestor.ingestor import * # import functions from other files
from SecureFileUploader.uploader import * # import functions from other files
from TextNLPAnalysis.nlp import * # import functions from other files

def test_create():
    assert create('test_filename')["status"] == 200
    assert create(None)["status"] == 404
    assert create(1)["status"] == 200

def test_delete():
    assert delete('test_record')["status"] == 200
    assert delete(None)["status"] == 404

def test_update():
    assert update('test_record', 'test_text')["status"] == 200
    assert update('test_record', None)["status"] == 404
    assert update(None, 'test_text')["status"] == 404
    assert update(None, None)["status"] == 404

def test_sentiment():
    assert get_sentiment('test_text')["status"] == 200
    assert get_sentiment(None)["status"] == 404

def test_search_by_keyword():
    assert search_by_keyword('test_keyword')["status"] == 200
    assert search_by_keyword(None)["status"] == 404
