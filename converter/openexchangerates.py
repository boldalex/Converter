import requests


OPENEXCHANGERATES_API_ID = '7df39ba4d20b4c7a82a08c6f2bf2d34e'

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
    rates = json['rates']
    return rates

print(currencies_names())