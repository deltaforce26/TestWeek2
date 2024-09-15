from typing import Any

import requests as re

import json


def get_weather(city: str, api_key: str) -> dict[str, any] :
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





def weather_score(weather):
    match weather['condition']:
        case 'Clear':
            return  1.0
        case 'Clouds':
            return 0.7
        case 'Rain':
            return 0.4
        case 'Stormy':
            return 0.2
        case _:
            return 0.0


if __name__ == '__main__':
    print(get_weather('yemen', 'aba4e7c1beac7cedacc89f2f4edaae8b'))