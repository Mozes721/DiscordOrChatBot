import requests
from config.config_files import APIkeys
def get_stock_data(ticker):
    URL = "https://api.twelvedata.com/time_series?symbol=" + ticker + "&interval=1day&outputsize=12&include_ohlc=true&apikey=" + APIkeys.stockAPI
    json_data = requests.get(URL).json()
    get_values = json_data['values']
    get_open_position = get_values[0]['open']
    return float(get_open_position)
