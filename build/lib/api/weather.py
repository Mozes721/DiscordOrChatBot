import requests
from pprint import pprint
from ..config.config_files import APIkeys
import os


def getweather(location):
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  Final_url = base_url + "appid=" + APIkeys.weatherAPI + "&id=" + location
  weather_data = requests.get(Final_url).json()
  pprint(weather_data)


getweather("107392")