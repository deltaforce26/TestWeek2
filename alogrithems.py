import json

from models.attack_model import Attack


def get_max_wind_speed():
    with open('information_files/weather.json', 'r', encoding='UTF8') as json_file:
        data = json.load(json_file)
        max_wind_speed = -1
        for weather in data:
            if weather['wind_speed'] > max_wind_speed:
                max_wind_speed = weather['wind_speed']
        return max_wind_speed



def generate_missions(target_cities, aircrafts, pilots):
    missions = []
    for key, city in target_cities.items():
        for key, aircraft in aircrafts.items():
            for key, pilot in pilots.items():
                missions.append(Attack(
                    city.city,
                    city.priority,
                    pilot.name,
                    aircraft.type,
                    city.distance,
                    city.weather_score,
                    city.weather_conditions,
                    pilot.skill_level,
                    aircraft.speed,
                    aircraft.fuel_capacity))
    return missions



def calc_somthing(max_wind_speed, missions):
    for mission in missions:






weights = {
    "distance": 0.20,
    "aircraft_type": 0.20,
    "pilot_skill": 0.20,
    "weather_conditions": 0.25,
    "priority": 0.15
}