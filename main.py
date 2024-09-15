import csv
import json

from alogrithems import *
from models.attack_model import Attack
from services import json_services as js
from services.distance_service import cities_distance
# from services.weather_service import  cities_weather_to_json

api_key = 'aba4e7c1beac7cedacc89f2f4edaae8b'

# list of all the pilots
pilots = js.get_pilots_dict('information_files/pilots.json')

# list of all the aircrafts
aircrafts = js.get_aircrafts_dict('information_files/aircrafts.json')

# dictionary of all the target cities
target_cities = js.get_target_cities_dict('information_files/target_cities.json')


# api request to get all the target cities weather
list_weather = [{"condition": city.weather.weather_conditions,
                 "clouds": city.weather.cloud_chance,
                 "wind_speed": city.weather.wind_speed} for key, city in target_cities.items()]
js.cities_weather_to_json(list_weather)

# (target_cities['city1'].weather_conditions)
cities_distance(target_cities)




missions = generate_missions(target_cities, aircrafts, pilots)

score_missions(missions)


# writes missions into a csv file
def write_missins_to_csv(missions):

    missions_dict = [mission.convert_to_dict() for mission in missions]
    with open('missions.csv', 'w', newline='') as csvfile:
        fieldnames = ['Target City', 'Priority', 'Assigned Pilot','Assigned Aircraft',
                      'Distance', 'Weather Conditions','Pilot Skill',
                      'Aircraft Speed', 'Aircraft Fuel Capacity', 'Mission Fit Score']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(missions_dict)
        print("CSV file created successfully.")

# in order to get only the top 7 ->
# missions_dict = sorted([mission.convert_to_dict() for mission in missions], key=lambda mission: mission['Mission Fit Score'], reverse=True)[:8]


write_missins_to_csv(missions)
# print(generate_missions())







