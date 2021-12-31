import random

from pollicino.sensors import base


class Humidity(base.Base):
    def __init__(self, sensor_id):
        super().__init__('humidity', sensor_id)

    def fetch(self):
        return random.randint(0, 100)
        # return super().fetch() * gpio.get(self.gpio_mode, self.pin_input)
