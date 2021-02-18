
def create(File Filename(s)):
  CreateEvent(UPLOAD_EVENT, timestamp)
  if(filename == NULL){
    log(info, "No Filename Provided")
    SendError
  }
  log(info, "File OK")
  record.filename = Filename
  record.id = '/file/12345'
  record.URL = 'hardcoded_URL.com'
  record.text = 'EXAMPLE TEXT'
  
  return success

def delete(record):
  CreateEvent(DELETE_EVENT, timestamp)
  log(info, "Delete Part of The File")
  #Delete part of file


def update(text):
  record.text = text