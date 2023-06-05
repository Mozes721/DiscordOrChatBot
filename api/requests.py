import json
import requests
from config.config_files import APIkeys
from config.constants import Constants


class APIRequests:

    def get_crypto_data(self, crypto):
        params = Constants.CRYPTO_PARAMETERS['slug'] = crypto
        headers = Constants.CRYPTO_HEADERS['X-CMC_PRO_API_KEY'] = APIkeys.cryptoAPI

        session = requests.Session()
        session.headers.update(headers)

        response = session.get(Constants.CRYPTO_URL, params=params)
        crypt_price = json.loads(response.text)['data']['1']['quote']['USD']['price']
        return int(crypt_price)

    def get_stock_data(self, ticker):
        url = Constants.STOCK_URL.format(symbol=ticker,
                                         api_key=APIkeys.stockAPI)
        json_data = requests.get(url).json()
        get_values = json_data['values']
        get_open_position = get_values[0]['open']
        return float(get_open_position)

    def get_weather_data(self,location):
        url = Constants.WEATHER_URL.format(api_key=APIkeys.weatherAPI,
                                           location=location)
        weather_data = requests.get(url).json()
        return weather_data