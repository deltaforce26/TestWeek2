import requests as re
from models.weather_model import Weather
import json









def get_weather(city):
    response = re.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=aba4e7c1beac7cedacc89f2f4edaae8b').json()
    weather = response['list']
    tmp = dict()
    for weather_entry in weather:
        if weather_entry.get('dt_txt') == '2024-09-13 00:00:00':
            tmp = weather_entry
            break
    weather_model = dict()
    weather_model['condition'] = tmp['weather'][0]['main']
    weather_model['clouds'] = tmp['clouds']['all']
    weather_model['wind_speed'] = tmp['wind']['speed']
    return weather_model


def cities_weather_to_json(list_weather):
    with open('information_files/weather.json', 'w') as outfile:
        json.dump(list_weather, outfile, indent=4, ensure_ascii=False)

# def cities_weather_2(target_cities):
#     with open('information_files/weather.json', 'r') as infile:
#         data = json.load(infile)
#         for key, city in target_cities.items():
#             city.weather_conditions =



def cities_weather(target_cities):
    list_weather = list()
    for key, value in target_cities.items():
        weather = get_weather(value.city)
        value.weather_score = weather_score(weather)
        value.weather_conditions = weather['condition']
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
    print(get_weather('yemen'))