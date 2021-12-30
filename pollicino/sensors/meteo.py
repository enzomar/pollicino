try:
    from pollicino.sensors import base
except:
    from . import base

import json

import requests

OWM_KEY = "ff60ec918526de129afd61859a882e5d"
URI_WEATHER = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric"
URI_ONECALL = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&appid={2}&units=metric"


class Meteo(base.Base):
    def __init__(self, sensor_id=0):
        self.location = 'Rome'
        super().__init__('meteo', sensor_id)

    def fetch(self):
        return 100
        uri = URI_WEATHER.format(self.location, OWM_KEY)
        r = requests.get(uri)
        return r.json()


if __name__ == '__main__':
    m = Meteo()
    uri = URI_ONECALL.format(38.2414, 16.2623, OWM_KEY)
    r = requests.get(uri)
    print(json.dumps(r.json()))
