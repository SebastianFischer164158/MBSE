import random
from pathlib import Path
from weather import weather_history

base_path = Path(__file__).parent
file_path = (base_path / "../weather_copenhagen.csv").resolve()


# SOLAR CELL
class SolarCell(object):
    
    def __init__(self, squaremeters_size):
        self.log = weather_history.WeatherLog(file_path)
        self.squaremeters = squaremeters_size

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.id)

    def power(self, datetime):
        return self.log.get_solar_rad(datetime) * random.uniform(0.175, 0.225) * self.squaremeters
