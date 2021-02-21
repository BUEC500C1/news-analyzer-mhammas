
# Secure File Uploader

## API Type

Entity-Based

## Purpose

An API to upload files(.pdf, .docx etc) and have them converted into text format.

## Entity Structure

- FILE_ID
- URL_STORED
- PROCESSED_TEXT

{
  Paragraphs []
}

## Events

  File Upload: UPLOAD_EVENT
  File Converted to Text (Processing): PROCESS_FILE_EVENT
  Update Text for a File: UPDATE_TEXT_EVENT

## Functions

- ```create(filename)```: Create a Entity Record
- ```delete(record)```: Delete a Entity Record
- ```update(record, text)```: Update a Entity Record
