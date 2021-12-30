import random
import gpio


class Base(object):
    def __init__(self, sensor_type, sensor_id):
        self.type = sensor_type
        self.id = sensor_id
        self.pin_input = None
        self.gpio_mode = "BOARD"
        self.polling_seconds = 1

    def fetch(self):
        return gpio.get(self.gpio_mode, self.pin_input)
