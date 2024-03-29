
# Secure File Uploader

## API Type

Entity-Based

## Purpose

An API to upload files(.pdf, .docx etc) and have them converted into text format.

## Entity Structure

- FILE_ID
- FILE_NAME
- User

{
  PAGES []
}

## Events

 -  File Upload: UPLOAD_EVENT
 -  File Converted to Text (Processing): PROCESS_FILE_EVENT
 -  Update Text for a File: UPDATE_TEXT_EVENT
 -  Read Text for a File: UPDATE_TEXT_EVENT


## Functions

- ```create(user, filename)```: Create a Entity Record
- ```delete(user, record)```: Delete a Entity Record
- ```update(user, record, text)```: Update a Entity Record
- ```read(user)```: Reads Entity Record

## User Authentication
- ```signup(user, password)```: Signs up the user
- ```login(user, password)```: Logs in the user
