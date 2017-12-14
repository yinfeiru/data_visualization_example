import os
import requests

GOOGLE_PLACES_API = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
PALCES_QUERY_PARAMS = {
    'key': os.environ['GOOGLE_API_KEY'],
    'location': '37.7749,-122.4194',
    'radius': 1000,
    'type': 'restaurant',
}

print requests.get(GOOGLE_PLACES_API, params=PALCES_QUERY_PARAMS).content
