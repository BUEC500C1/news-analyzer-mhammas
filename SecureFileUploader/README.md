API Type: Entity Based

Object for Storing the File:
FILE_ID
URL_STORED
PROCESSED_TEXT

{
  Paragraphs []
}

Events:
  File Upload: UPLOAD_EVENT
  File Converted to Text (Processing): PROCESS_FILE_EVENT
  Update Text for a File: UPDATE_TEXT_EVENT


Create(): Create a Entity Record
Delete(): Delete a Entity Record
Update(): Update a Entity Record
Read(): Read a Entity Record

Parameters:
Files()

Create(File Filename(s)){
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
  
}

Delete(record){
  CreateEvent(DELETE_EVENT, timestamp)
  log(info, "Delete Part of The File")
  //Delete part of file
}

Update(text){
  record.text = text
}


Other examples:

Logs:
  File Uploaded Percentage
  File Type: doc/pdf

Warning:
  Deprecated file format

Errors:
  Text Conversion Failed
  User cannot upload file
  User cannot convert
