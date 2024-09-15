from typing import Any

import requests as re
from models.weather_model import Weather
import json


def get_weather(city: str, api_key: str) :
    date_to_get = '2024-09-16 00:00:00'
    try:
        response = re.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}').json()
    except Exception as e:
        print(f'error: {e}')
        exit()
    weather = response['list']
    tmp = dict()
    for weather_entry in weather:
        if weather_entry.get('dt_txt') == date_to_get:
            tmp = weather_entry
            break
    weather_model = dict()
    weather_model['condition'] = tmp['weather'][0]['main']
    weather_model['clouds'] = tmp['clouds']['all']
    weather_model['wind_speed'] = tmp['wind']['speed']
    return weather_model


def cities_weather_to_json(list_weather: list):
    with open('information_files/weather.json', 'w') as outfile:
        json.dump(list_weather, outfile, indent=4, ensure_ascii=False)



# def cities_weather_2(target_cities):
#     with open('information_files/weather.json', 'r') as infile:
#         data = json.load(infile)
#         for key, city in target_cities.items():
#             city.weather_conditions =



def cities_weather(target_cities, api_key):
    list_weather = list()
    for key, value in target_cities.items():
        weather = get_weather(value.city, api_key)
        value.weather_score = weather_score(weather)
        value.weather_conditions = weather['condition']
        value.wind_speed = weather['wind_speed']
        value.cloud_chance = weather['clouds']
        list_weather.append(weather)
    cities_weather_to_json(list_weather)




def weather_score(weather):
    if weather['condition'] == 'Clear':
        return  1.0
    elif weather['condition'] == 'Clouds':
        return 0.7
    elif weather['condition'] == 'Rain':
        return 0.4
    elif weather['condition'] == 'Stormy':
        return 0.2
    else:
        return 0.0



if __name__ == '__main__':
    print(get_weather('yemen', 'aba4e7c1beac7cedacc89f2f4edaae8b'))