def create(filename):
  #CreateEvent(UPLOAD_EVENT, timestamp)
  if(filename is None):
    return 404
    #log(info, "No Filename Provided")
    #SendError

  #log(info, "File OK")
  #record.filename = Filename
  #record.id = '/file/12345'
  #record.URL = 'hardcoded_URL.com'
  #record.text = 'EXAMPLE TEXT'
  
  return 200

def delete(record):
  #CreateEvent(DELETE_EVENT, timestamp)
  #log(info, "Delete Part of The File")
  #Delete part of file
  return 200


def update(record, text):
  #record.text = text
  return 200