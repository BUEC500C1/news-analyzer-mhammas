import logging
import PyPDF2
#from werkzeug import secure_filename
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:v4pxsDMf4q3kpwuY@cluster0.hduz6.mongodb.net/newsanalyzer?retryWrites=true&w=majority")

def create(filename):
  #CreateEvent(UPLOAD_EVENT, timestamp)
  if filename is None:
    logging.info("No Filename Provided")
    return {"status": 404, "message": "No Filename Provided"}

  filename.save(filename.filename)
  pdfFileObj = open(filename.filename, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

  record = {}
  record["filename"] = filename.filename
  #record["id"] = '/file/12345'
  #record["URL"] = 'hardcoded_URL.com'
  record["text"] = []

  i = 0
  while i < pdfReader.numPages:
    pageObj = pdfReader.getPage(i)
    record["text"].append(pageObj.extractText())
    i+= 1

  db = client.get_default_database()
  files = db['files']
  files.insert_one(record)
  logging.info("File Ok")

  return {"status": 200}


def read_records():
  logging.info("Reading All Records")
  db = client.get_default_database()
  files = db['files']
  cursor = files.find({})
  docs = {}
  i = 0
  for document in cursor:
    docs[i] = {}
    docs[i]['filename'] = document['filename']
    docs[i]['text'] = document['text']
    i += 1
  return docs


def delete(record):
  if record is None:
    logging.info("Record Not Found")
    return {"status": 404, "message": "Record Not Found"}
  #add consideration for non-existing record
  #CreateEvent(DELETE_EVENT, timestamp)
  logging.info("Delete Part of The File")
  #Delete part of file
  return {"status": 200}


def update(record, text):
  if record is None:
    logging.info("Record Not Found")
    return {"status": 404, "message": "Record Not Found"}
  if text is None:
    logging.info("Text Not Found")
    return {"status": 404, "message": "Text Not Found"}
  
  logging.info("File Text Updated")
  #record.text = text
  return {"status": 200}
