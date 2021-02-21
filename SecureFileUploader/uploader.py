import logging

def create(filename):
  #CreateEvent(UPLOAD_EVENT, timestamp)
  if filename is None:
    logging.info("No Filename Provided")
    return {"status": 404, "message": "No Filename Provided"}

  filename = str(filename)
  record = {}
  record["filename"] = filename
  record["id"] = '/file/12345'
  record["URL"] = 'hardcoded_URL.com'
  record["text"] = 'EXAMPLE TEXT'
  
  logging.info("File Ok")

  return {"status": 200}

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
