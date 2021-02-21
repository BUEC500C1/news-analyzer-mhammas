from NewsfeedIngestor.ingestor import * # import functions from other files
from SecureFileUploader.uploader import * # import functions from other files
from TextNLPAnalysis.nlp import * # import functions from other files

def test_create():
    assert create('test_filename') == 200

def test_delete():
    assert delete('test_record') == 200

def test_update():
    assert update('test_record', 'test_text') == 200

def test_sentiment():
    assert get_sentiment('test_record', 1) == 200

def test_search_by_keyword():
    assert search_by_keyword('test_keyword') == 200
