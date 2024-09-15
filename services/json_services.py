import json
from random import random, randint

from models.aircraft_model import Aircraft_Model
from models.pilot_model import PilotModel
from models.target_city_model import TargetCity


def read_from_json_file(json_file) -> list:
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data


def get_pilots_dict(path) -> dict[str, PilotModel]:
    file_path_pilots = path
    pilots_list = sorted(read_from_json_file(file_path_pilots), key=lambda k: k['skill_level'], reverse=True)
    pilots_models = {}
    for i in range(1,len(pilots_list) + 1):
            pilots_models["pilot{0}".format(i)] = (
                PilotModel(
                    pilots_list[i - 1]['name'],
                    pilots_list[i - 1]['skill_level']))
    return pilots_models


def get_aircrafts_dict(path) -> dict[str, Aircraft_Model]:
    file_path_aircrafts = path
    aircrafts_list = sorted(read_from_json_file(file_path_aircrafts), key=lambda k: k['fuel_capacity'], reverse=True)
    aircrafts_models = {}
    for i in range(1,len(aircrafts_list) + 1):
        aircrafts_models["aircraft{0}".format(i)] = (
            Aircraft_Model(
                aircrafts_list[i - 1]['type'],
                aircrafts_list[i - 1]['speed'],
                aircrafts_list[i - 1]['fuel_capacity']))
    return aircrafts_models


def get_target_cities_dict(path) -> dict[str, TargetCity]:
    file_path = path
    target_cities_list = sorted(read_from_json_file(file_path), key=lambda k: k['Priority'], reverse=True)
    target_cities_models = dict()
    for i in range(1,len(target_cities_list) + 1):
        target_cities_models["city{0}".format(i)] = (
            TargetCity(
                target_cities_list[i - 1]['City'],
                target_cities_list[i - 1]['Priority'],
                ))
    return target_cities_models

if __name__ == '__main__':
    print(randint(1, 100)/ 100)
    get_target_cities_dict('../information_files/target_cities.json')