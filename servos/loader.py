from servos.waterpump import Waterpump
from helpers import topic
import yaml

SERVO_MAP={'waterpump': Waterpump}

def load(configuration_file):
	servos_pool = dict()
	with open(configuration_file, "r") as stream:
		try:
			config = yaml.safe_load(stream)
			for s in config['servos']:
				s_id = s['id']
				s_type = s['type'].lower()
				servo_class = SERVO_MAP[s_type]
				s_instance = servo_class(s['id'])
				if s_type not in servos_pool:
					servos_pool[s_type]=dict()
				servos_pool[s_type][s_id] = s_instance
		except yaml.YAMLError as exc:
			print(exc)
	return servos_pool
