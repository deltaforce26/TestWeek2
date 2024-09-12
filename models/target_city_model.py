from models.weather_model import Weather


class TargetCity:
    def __init__(self, city, priority, weather_conditions = None, distance = -1, weather_score = -1):
        self.city = city
        self.priority = priority
        self.weather_conditions = weather_conditions
        self.distance = distance
        self.weather_score = weather_score



