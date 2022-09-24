import json

from requests import Request, Session
from config.config_files import APIkeys

def get_crypto_data(crypto):
    URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'slug': crypto,
        'convert': 'USD'
    }
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY': APIkeys.cryptoAPI
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(URL, params=parameters)
    crypt_price = json.loads(response.text)['data']['1']['quote']['USD']['price']
    return int(crypt_price)