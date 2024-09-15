# from main import api_key
from services.weather_service import weather_score, get_weather
api_key = 'aba4e7c1beac7cedacc89f2f4edaae8b'

class Weather:
    def __init__(self, city: str):
        weather = get_weather(city, api_key)
        self.score = weather_score(weather)
        self.weather_conditions = weather['condition']
        self.wind_speed = weather['wind_speed']
        self.cloud_chance = weather['clouds']


