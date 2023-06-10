from helper.format_api_requests import extract_crypto_info, get_city_id, extract_weather_info
import requests
from config.config_files import APIkeys
from config.constants import Constants


class APIRequests:

    def get_crypto_data(self, crypto):
        constants = Constants()
        constants.CRYPTO_PARAMETERS['slug'] = crypto
        constants.CRYPTO_HEADERS['X-CMC_PRO_API_KEY'] = APIkeys.cryptoAPI

        session = requests.Session()
        session.headers.update(constants.CRYPTO_HEADERS)

        response = session.get(constants.CRYPTO_URL,
                               params=constants.CRYPTO_PARAMETERS)
        response_json = response.json()
        (crypto_name,
         crypto_symbol,
         formatted_price,
         formatted_market_cap) = extract_crypto_info(response_json)

        formated_response = (
            f'The price of {crypto_name}'
            f'({crypto_symbol}) is {formatted_price}'
            f' and has market cap of {formatted_market_cap}'
        )
        return formated_response

    def get_stock_data(self, ticker):
        url = Constants.STOCK_URL.format(symbol=ticker,
                                         api_key=APIkeys.stockAPI)
        json_data = requests.get(url).json()
        get_values = json_data['values']
        get_open_position = get_values[0]['open']

        formated_response = (
                          f'Current price of {ticker}'
                          f' is {float(get_open_position)}'
                          )
        return formated_response

    def get_weather_data(self, location):
        city_id = get_city_id(location)
        url = Constants.WEATHER_URL.format(api_key=APIkeys.weatherAPI,
                                           location=city_id)
        weather_json = requests.get(url).json()
        weather_data = extract_weather_info(weather_json)

        formated_response = (
            f'Current weather of {location} is {weather_data["temp"]} celcius'
            f' sky {weather_data["weather"].lower()} and'
            f' wind speed {weather_data["wind_speed"]}'
        )
        return formated_response
