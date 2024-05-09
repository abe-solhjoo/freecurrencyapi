import requests
import json

URL = 'https://api.freecurrencyapi.com/v1/latest?apikey='


def get_rates(api_key):
    """
    get currencies rates from api
    :return: rates in json
    """
    response = requests.get(URL + api_key)
    if response.status_code == 200:
        return json.loads(response.text)
    return response.status_code