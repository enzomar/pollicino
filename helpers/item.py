import json

class Item(object):
	def __init__(self):
		self.topic = "default" # moisture
		self.value = 0
		self.sensor_id = 0

	def __str__(self):
		return json.dumps(self.__dict__)

	
