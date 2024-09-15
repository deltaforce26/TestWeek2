class Attack:
    def __init__(self, target_city, priority, assigned_pilot, assigned_aircraft, distance, weather_conditions, pilot_skill, aircraft_speed, aircraft_fuel_capacity, wind_speed, cloud_chance , mission_fit_score = -1):
        self.target_city = target_city
        self.priority = priority
        self.assigned_pilot = assigned_pilot
        self.assigned_aircraft = assigned_aircraft
        self.distance = distance
        self.weather_conditions = weather_conditions
        self.pilot_skill = pilot_skill
        self.aircraft_speed = aircraft_speed
        self.aircraft_fuel_capacity = aircraft_fuel_capacity
        self.wind_speed = wind_speed
        self.cloud_chance = cloud_chance
        self.mission_fit_score = mission_fit_score


    # converts the attack model into a dictionary
    def convert_to_dict(self):
        return {
            "Target City": self.target_city,
            "Priority": self.priority,
            "Assigned Pilot": self.assigned_pilot,
            "Assigned Aircraft": self.assigned_aircraft,
            "Distance": self.distance,
            "Weather Conditions": self.weather_conditions,
            "Pilot Skill": self.pilot_skill,
            "Aircraft Speed": self.aircraft_speed,
            "Aircraft Fuel Capacity": self.aircraft_fuel_capacity,
            "Mission Fit Score": self.mission_fit_score
        }

