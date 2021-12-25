from controller.watering import Watering 
from helpers import topic
import logging
import yaml


CTRL_MAP={'watering': Watering}


def load(configuration_file):
	list_of_ctrls = list()
	with open(configuration_file, "r") as stream:
		try:
			config = yaml.safe_load(stream)
			for sector in config:
				sector_config = config[sector]
				ctrls_config = sector_config['controllers']
				for ctrl in ctrls_config:
					c_type = ctrl['type']
					c_class = CTRL_MAP[c_type]
					for each in ctrl['links']:
						
						servo_id = str(each['servo_id'])
						servo_type = sector_config['servos'][servo_id]['type']
						sensor_id = str(each['sensor_id'])
						sensor_type = sector_config['sensors'][sensor_id]['type']
						threashold = each['threshold']
						topic_sub = topic.status(sensor_id, sensor_type, 'sensors', sector)
						topic_pub = topic.cmd_pub(servo_id, servo_type, 'servos', sector)
						c_instance = c_class(topic_sub, topic_pub, threashold)
						list_of_ctrls.append(c_instance)
		except yaml.YAMLError as exc:
			logging.info(exc)
	return list_of_ctrls

