from pollicino.helpers import gpio
from pollicino.sensors import base


class Moisture(base.Base):
    def __init__(self, sensor_id):
        super().__init__('moisture', sensor_id)

    def fetch(self):
        return gpio.get(self.gpio_mode, self.pin_input)
