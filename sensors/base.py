from helpers import item 
import random


class Base(object):
	def __init__(self, sensor_type, sensor_id):
		self.type = sensor_type
		self.id = sensor_id
		self.gpio = None
		self.polling_seconds = 1

	def fetch(self):
		return random.randint(1, 10)