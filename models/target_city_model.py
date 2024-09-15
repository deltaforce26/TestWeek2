from models.weather_model import *


class TargetCity:
    def __init__(self, city, priority, distance = -1):
        self.city = city
        self.priority = priority
        self.distance = distance
        self.weather = Weather(city)


