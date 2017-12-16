import csv
import json
import os
import requests
import tempfile

class CSVGenerator:
    GOOGLE_PLACES_API = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    PALCES_QUERY_PARAMS = {
        'key': os.environ['GOOGLE_API_KEY'],
        'radius': 1000,
        'type': 'restaurant',
    }

    def __init__(self, location):
        self.location = location

    def generate_csv(self):
        params = dict(self.PALCES_QUERY_PARAMS, location=self.location)
        places_response = requests.get(self.GOOGLE_PLACES_API, params=params).content.decode('utf-8')
        places = json.loads(places_response)
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(['Restaurant name', 'Rating'])
            for place in places['results']:
                if place['rating'] > 3:
                    csvwriter.writerow([place['name'], place['rating']])

        return f.name

if __name__ == '__main__':
    c = CSVGenerator()
    print (c.generate_csv())
