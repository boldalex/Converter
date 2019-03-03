import requests
from decimal import Decimal

OPENEXCHANGERATES_API_ID = <YOUR_API_ID>

#function for getting json response from Openexchangerates.org api
def get_json(route):
    API_URL = 'https://openexchangerates.org/api/{route}?app_id={app_id}'
    response = requests.get(API_URL.format(route= route, app_id=OPENEXCHANGERATES_API_ID))
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError('API returned error')

#function for getting currencies names according to it's code
def currencies_names():
    json = get_json('currencies.json')
    return json

#function for getting currencies rates to usd
def get_rates():
    json = get_json('latest.json')
    rates_float = json['rates']
    TENPLACES = Decimal('10') ** -10
    rates = {k: Decimal(v).quantize(TENPLACES) for (k, v) in rates_float.items()}
    return rates

