import csv
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
# (target_cities['city1'].weather_conditions)


missions = generate_missions(target_cities, aircrafts, pilots)



missions_dict = list()
for mission in missions:
    tmp = mission.convert_to_dict()
    missions_dict.append(tmp)
print(missions_dict)

with open('missions.csv', 'w', newline='') as csvfile:
    fieldnames = ['Target City', 'Priority', 'Assigned Pilot', 'Assigned Aircraft', 'Distance', 'Weather Conditions', 'Pilot Skill', 'Aircraft Speed', 'Fuel Capacity', 'Mission Fit Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(missions_dict)




# print(generate_missions())






