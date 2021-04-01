
# NewsFeed Ingestor

## API Type

Procedural

## Purpose

An API to discover news content on the internet (e.g. looking for Super bowl). It supports searching by keyword.

## Implementation Details

- The function ``search_by_keyword(keyword)`` in ``ingestor.py`` takes in a keyword argument to search NYT API for related articles
- Needs a developer account at NYTimes and a environment variable ``nyt_key`` with the secret developer key

