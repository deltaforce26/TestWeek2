from models.weather_model import Weather


class TargetCity:
    def __init__(self, city, priority, wind_speed = None, cloud_chance = None, weather_conditions = None, distance = -1, weather_score = -1):
        self.city = city
        self.priority = priority
        self.wind_speed = wind_speed
        self.cloud_chance = cloud_chance
        self.weather_conditions = weather_conditions
        self.distance = distance
        self.weather_score = weather_score

    # weather = Weather()


