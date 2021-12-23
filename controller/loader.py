from controller.watering import Watering 
from helpers import topic
import yaml


CTRL_MAP={'watering': Watering}

"""
  - type: watering
    sensor: moisture/0
    servo: waterpump/0
    threshold: 5
"""

def load(configuration_file):
	list_of_ctrls = list()

	with open(configuration_file, "r") as stream:
		try:
			config = yaml.safe_load(stream)
			for c in config['controllers']:
				c_type = c['type'].lower()
				ctrl_class = CTRL_MAP[c_type]
				c_sensor_type = c['sensor_type']
				c_sensor_id = c['sensor_id']
				c_servo_type = c['servo_type']
				c_servo_id = c['servo_id']
				topic_sub = topic.build(c_sensor_id, c_sensor_type, 'sensors')
				topic_pub = topic.build(c_servo_id, c_servo_type, 'servo')
				c_instance = ctrl_class(topic_sub, topic_pub)
				list_of_ctrls.append(c_instance)
		except yaml.YAMLError as exc:
			print(exc)
	return list_of_ctrls
