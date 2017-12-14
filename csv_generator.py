import csv
import json
import os
import requests
import tempfile

class CSVGenerator:
    GOOGLE_PLACES_API = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    PALCES_QUERY_PARAMS = {
        'key': os.environ['GOOGLE_API_KEY'],
        'location': '37.7749,-122.4194',
        'radius': 1000,
        'type': 'restaurant',
    }

    def generate_csv(self):
        places_response = requests.get(self.GOOGLE_PLACES_API, params=self.PALCES_QUERY_PARAMS).content
        places = json.loads(places_response)
        with tempfile.NamedTemporaryFile(delete=False) as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(['Restaurant name', 'Rating'])
            for place in places['results']:
                if place['rating'] > 3:
                    csvwriter.writerow([place['name'].encode("utf-8"), place['rating']])

        return f.name

if __name__ == '__main__':
    c = CSVGenerator()
    print (c.generate_csv())
