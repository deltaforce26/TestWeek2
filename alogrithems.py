import json
from random import random, randint

from models import attack_model
from models.attack_model import Attack
from services.weather_service import weather_score


def get_max_wind_speed():
    with open('information_files/weather.json', 'r', encoding='UTF8') as json_file:
        data = json.load(json_file)
        max_wind_speed = -1
        for weather in data:
            if weather['wind_speed'] > max_wind_speed:
                max_wind_speed = weather['wind_speed']
        return max_wind_speed



def generate_missions(target_cities, aircrafts, pilots) -> list[attack_model]:
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
                    city.weather_conditions,
                    pilot.skill_level,
                    aircraft.speed,
                    aircraft.fuel_capacity,
                    city.wind_speed,
                    city.cloud_chance))
    return missions



def score_missions(missions):
    for mission in missions:
        mission.mission_fit_score = round(
            pilot_skill_calc(mission.pilot_skill) +
            priority_calc(mission.priority) +
            distance_calc(mission.distance) +
            weather_calc(mission.weather_conditions, mission.wind_speed, mission.cloud_chance), 2)


def pilot_skill_calc(pilot_skill: int):
    max_score = 10
    one_hundred_percent = 0.20
    return (pilot_skill * one_hundred_percent) / max_score


def priority_calc(priority: int):
    max_score = 5
    one_hundred_percent = 0.15
    return (priority * one_hundred_percent) / max_score


def distance_calc(distance):
    max_score = 100
    one_hundred_percent = 0.20
    k = 0.1
    score = max(1, 100 - (k * distance))
    return (score * one_hundred_percent) / max_score


def weather_calc(condition: str, wind_speed: float, cloud: int):
    weather = weather_conditions_calc(condition)
    wind = wind_speed_calc(wind_speed)
    cloud = cloud_chance(cloud)
    res = weather + wind + cloud
    max_score = 1.0
    one_hundred_percent = 0.25
    return (res * one_hundred_percent) / max_score


def weather_conditions_calc(condition: str):
    max = 1.0
    weather_condition = weather_score({'condition':condition})
    one_hundred_percent = 0.33
    return round((weather_condition * one_hundred_percent) / max, 2)



def cloud_chance(cloud_chance):
    max_cloud = 100
    one_hundred_percent = 0.33
    sum = 1 - (cloud_chance / max_cloud)
    sum *= one_hundred_percent
    return round(sum, 2)




def wind_speed_calc(wind_speed):
    one_hundred_percent = 0.34
    max_wind_speed = get_max_wind_speed()
    sum = 1 - (wind_speed / max_wind_speed)
    sum *= one_hundred_percent
    return round(sum, 2)




weights = {
    "distance": 0.20,
    "aircraft_type": 0.20,
    "pilot_skill": 0.20,
    "weather_conditions": 0.25,
    "priority": 0.15
}


weather_weights = {
    "wind_speed": 0.34,
    "cloud_chance" : 0.33,
    "weather_condition": 0.33,
}


if __name__ == '__main__':
    print(weather_conditions_calc('Stormy'))








