import csv
import json
import math
import os
import requests
import tempfile

class CSVGenerator:
    VALID_RATINGS = [3, 4, 5]
    GOOGLE_PLACES_API = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    PALCES_QUERY_PARAMS = {
        'key': os.environ['GOOGLE_API_KEY'],
        'radius': 1000,
        'type': 'restaurant',
    }

    def __init__(self, locations):
        self.locations = locations

    # TODO make generate_restaurant_ratings_csv work with a list of locations
    def generate_restaurant_ratings_csv(self):
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

    def generate_rating_buckets_csv(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            csvwriter = csv.writer(f)

            headers = ['Rating']
            results = {}
            for location in self.locations:
                headers.append(location)
                params = dict(self.PALCES_QUERY_PARAMS, location=location)
                places_response = requests.get(self.GOOGLE_PLACES_API, params=params).content.decode('utf-8')
                places = json.loads(places_response)

                results[location] = []
                for rating in self.VALID_RATINGS:
                    results[location].append(sum([math.floor(place['rating']) == rating for place in places['results']]))

            csvwriter.writerow(headers)

            buckets = list(results.values())
            for index, counts in enumerate(zip(buckets[0], buckets[1])):
                row = [self.VALID_RATINGS[index]] + list(counts)
                csvwriter.writerow(row)
        return f.name

if __name__ == '__main__':
    c = CSVGenerator()
    print (c.generate_csv())
