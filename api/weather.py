import requests
from pprint import pprint
import json
from config.config_files import APIkeys

def get_json_data(location):
  with open('/home/mozes/Desktop/TwitterBot/TwitterBot/config/city_list.json') as weather_data:
    json_data = json.load(weather_data)
    for data in json_data:
      if data['name'] == 'London':
       return data['id']


def kelvin_to_celcius_farhreinheit(response):
  temp_kelvin = response['main']['temp']
  celsius = temp_kelvin - 273.15
  fahrenheit = celsius * (9/5) + 32

  return int(celsius), int(fahrenheit)



def get_weather_data(location):
  location_id = str(get_json_data(location))
  BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
  URL = BASE_URL + "appid=" +APIkeys.weatherAPI + "&id=" + location_id
  response = requests.get(URL).json()
  temp_celsius, temp_fahrenheit = kelvin_to_celcius_farhreinheit(response)
  return temp_celsius, temp_fahrenheit


