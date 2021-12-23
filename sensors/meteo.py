try:
    from sensors import base
except:
    import base

import requests

OWM_KEY = "ff60ec918526de129afd61859a882e5d"
URI_TEMPLATE="https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric"

class Meteo(base.Base):
    def __init__(self, sensor_id=0):
        self.location='Rome'
        super().__init__('meteo', sensor_id)

    def fetch(self):
        return 100
        uri=URI_TEMPLATE.format(self.location, OWM_KEY)
        r=requests.get(uri)
        return r.json() 


