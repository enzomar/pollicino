from sensors.moisture import Moisture
from sensors.photoresistor import Photoresistor
from helpers import topic

import yaml


DEFAULT_POLLING_SECONDS=1

SENSORS_MAP={'moisture': Moisture, 
			 'photoresistor':Photoresistor}

def load(configuration_file):
	list_of_sensors = list()
	with open(configuration_file, "r") as stream:
		try:
			config = yaml.safe_load(stream)
			for s in config['sensors']:
				sensor_class = SENSORS_MAP[s['type'].lower()]
				s_instance = sensor_class(s['id'])
				s_topic = topic.build(s_instance.id, s_instance.type, 'sensors')
				list_of_sensors.append({'instance':s_instance, 'topic':s_topic})
			try:
				polling_seconds = config['sensors_polling_seconds']
			except KeyError:
				polling_seconds = DEFAULT_POLLING_SECONDS
		except yaml.YAMLError as exc:
			print(exc)
	return list_of_sensors, polling_seconds
