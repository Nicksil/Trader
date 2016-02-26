from eve.models import MarketType
from eve.models import Region
from eve.models import SolarSystem

import requests

MODEL_DATA = {
    'region': {
        'model': Region,
        'endpoint': 'https://public-crest.eveonline.com/regions/',
    },
    'solar_system': {
        'model': SolarSystem,
        'endpoint': 'https://public-crest.eveonline.com/solarsystems/',
    },
    'market_type': {
        'model': MarketType,
        'endpoint': 'https://public-crest.eveonline.com/market/types/',
    },
}


class Populate(object):

    def __init__(self, model):
        self.data = []
        self.endpoint = MODEL_DATA[model]['endpoint']
        self.model = MODEL_DATA[model]['model']
        self.objects = []

    def call_crest(self):
        r = requests.get(self.endpoint)
        r.raise_for_status()

        return r.json()

    def parse(self, data):
        for i in data['items']:
            if self.model is MarketType:
                _ = {
                    'id': i['type']['id'],
                    'name': i['type']['name'],
                    'market_group': i['marketGroup']['id'],
                }
            else:
                _ = {
                    'id': i['id'],
                    'name': i['name'],
                }

            self.data.append(_)

    def check_next(self, data):
        """
        Check if returned JSON data contains a 'next' attribute indicating
        there's more than one page of results to collect

        If next, return two-tuple (True, [href of next page])

        else, return two-tuple (False, None)
        """
        if 'next' in data.keys():
            return True, data['next']['href']

        return False, None

    def create_objects(self):
        for d in self.data:
            self.objects.append(self.model(**d))

    def save(self):
        self.model.objects.bulk_create(self.objects)

    def populate(self):
        crest_data = self.call_crest()
        has_next, self.endpoint = self.check_next(crest_data)

        self.parse(crest_data)

        if has_next:
            self.populate()
        else:
            self.create_objects()
            self.save()
