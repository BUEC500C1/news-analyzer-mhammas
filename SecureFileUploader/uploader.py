import logging
import PyPDF2
#from werkzeug import secure_filename
import pymongo

client = pymongo.MongoClient("ADD API KEY HERE")


def signup_user(user, password):
  db = client.get_default_database()
  users = db['users']
  cursor = users.find({})
  for user_obj in cursor:
    if user_obj['username'] == user:
      return {"status": 404, "message": "Username already Taken"}
  users.insert_one({'username': user, 'password': password})  
  return {'status': 200}

def login_user(user, password):
  db = client.get_default_database()
  users = db['users']
  cursor = users.find({})
  for user_obj in cursor:
    if user_obj['username'] == user and user_obj['password'] == password:
      return {"status": 200}
  return {"status": 404, "message": "User not found"}

def create(user, filename):
  #CreateEvent(UPLOAD_EVENT, timestamp)
  if filename is None:
    logging.info("No Filename Provided")
    return {"status": 404, "message": "No Filename Provided"}

  filename.save(filename.filename)
  pdfFileObj = open(filename.filename, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

  record = {}
  record["filename"] = filename.filename
  record["user"] = user
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


def read_records(user):
  logging.info("Reading All Records")
  db = client.get_default_database()
  files = db['files']
  cursor = files.find({})
  docs = {}
  i = 0
  for document in cursor:
    if document['user'] == user:
      docs[i] = {}
      docs[i]['filename'] = document['filename']
      docs[i]['text'] = document['text']
      i += 1
  return docs


def delete(username, filename):
  if filename is None:
    logging.info("Record Not Found")
    return {"status": 404, "message": "Record Not Found"}
  db = client.get_default_database()
  files = db['files']
  cursor = files.find({})
  
  for document in cursor:
    if document['user'] == username and str(document["filename"]) == str(filename):
      db['files'].remove(document)
      logging.info("Delete The File")
      return {"status": 200}
  
  logging.info("Record Not Found")
  return {"status": 404, "message": "Record Not Found"}



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
