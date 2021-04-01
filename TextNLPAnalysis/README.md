
# Text NLP Analysis

## API Type

Procedural

## Purpose

An API to perform nlp analysis (e.g. sentiment analysis) on a given text.

## Implementation Details
- Built using Google Language API. A service account is needed for it along with the secret key json placed in the project directory and linked in an environment variable ('GOOGLE_APPLICATION_CREDENTIALS') as shown in Google's guide.
- The function ``get_sentiment(text)`` in ``nlp.py`` takes in text and returns the sentiment score for it
- The function ``get_entities(text)`` in ``nlp.py`` takes in text and returns the entities for it
- The function ``get_entities_sentiment(text)`` in ``nlp.py`` takes in text and returns the entities and sentiment for them
