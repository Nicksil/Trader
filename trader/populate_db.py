from eve.models import MarketType
from eve.models import Region
from eve.models import SolarSystem

import requests

REGION_ENDPOINT = 'https://public-crest.eveonline.com/regions/'
SOLAR_SYSTEM_ENDPOINT = 'https://public-crest.eveonline.com/solarsystems/'
MARKET_TYPE_ENDPOINT = 'https://public-crest.eveonline.com/market/types/'


def crest_request(endpoint):
    r = requests.get(endpoint)
    return r.json()


def parse_crest_data(data):
    items = []

    for d in data['items']:
        _ = {
            'id': d['id'],
            'name': d['name'],
        }
        items.append(_)

    return items


def parse_crest_market_types(data):
    types = []

    for d in data['items']:
        _ = {
            'id': d['type']['id'],
            'name': d['type']['name'],
            'market_group': d['marketGroup']['id'],
        }

        types.append(_)

    return types


def create_objects(data, model):
    objs = []

    for d in data:
        objs.append(model(id=d['id'], name=d['name']))

    return objs


def create_market_type_objects(data):
    objs = []

    for d in data:
        objs.append(MarketType(id=d['id'], name=d['name'], market_group=d['market_group']))

    return objs


def save(data, model):
    model.objects.bulk_create(data)


def populate_regions():
    print('Populating regions...\r\n')

    crest_data = crest_request(REGION_ENDPOINT)
    parsed = parse_crest_data(crest_data)
    objs = create_objects(parsed, Region)
    save(objs, Region)


def populate_solar_systems():
    print('Populating solar systems...\r\n')

    crest_data = crest_request(SOLAR_SYSTEM_ENDPOINT)
    parsed = parse_crest_data(crest_data)
    objs = create_objects(parsed, SolarSystem)
    save(objs, SolarSystem)


def populate_market_types():
    print('Populating market types...\r\n')

    crest_data = crest_request(MARKET_TYPE_ENDPOINT)
    parsed = parse_crest_market_types(crest_data)
    objs = create_market_type_objects(parsed)
    save(objs, MarketType)


def populate_all():
    populate_regions()
    populate_solar_systems()
    populate_market_types()
