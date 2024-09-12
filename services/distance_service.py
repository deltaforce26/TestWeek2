import math
import requests as re

def calc_distance(city):
    response = re.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=aba4e7c1beac7cedacc89f2f4edaae8b').json()
    target_lat = round(response[0]['lat'], 2)
    target_lon = round(response[0]['lon'], 2)
    base_lat = 31.23
    base_lon = 34.65
    distance = haversine_distance(target_lat, target_lon, base_lat, base_lon)
    return round(distance, 2)



def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance


def cities_distance(target_cities):
    for key, value in target_cities.items():
        value.distance = calc_distance(value.city)