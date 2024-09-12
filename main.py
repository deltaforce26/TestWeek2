import json

from alogrithems import *
from models.attack_model import Attack
from services import json_services as js
from services.weather_service import cities_weather

# list of all the pilots
pilots = js.get_pilots_dict('information_files/pilots.json')

# list of all the aircrafts
aircrafts = js.get_aircrafts_dict('information_files/aircrafts.json')

# list of all the target cities
target_cities = js.get_target_cities_dict('information_files/target_cities.json')


# api request to get all the target cities weather
cities_weather(target_cities)
print(target_cities['city1'].weather_conditions)


generate_missions(target_cities, aircrafts, pilots)








# print(generate_missions())






