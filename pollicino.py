import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from pollicino.controller import controller
from pollicino.sensors import sensors
from pollicino.servos import servos
from pollicino.helpers import broker
import argparse
import logging
import socket


LOG_FORMAT_1 = '[%(asctime)s - %(process)d - %(processName)s - %(levelname)s - %(pathname)s:%(lineno)d] %(message)s'
LOG_FORMAT_2 = '[%(asctime)s] p%(process)s %(pathname)s:%(lineno)d} %(levelname)s - %(message)s , %m-%d %H:%M:%S'


logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT_1)


DEFAUL_CONFIG_FILE = "config/pollicino.yaml"
AUTO_CONFIG = 'config/{0}.yaml'.format(socket.gethostname())



def parse_input():
	parser = argparse.ArgumentParser(allow_abbrev=False)
	parser.add_argument('-m','--mode', action='store', choices=['servos', 'sensors', 'ctrl'])
	parser.add_argument('-b','--broker', action='store', default='0.0.0.0')
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-c','--config', action='store', default=DEFAUL_CONFIG_FILE)
	group.add_argument('-a','--autoconfig', action='store_true')

	args = parser.parse_args()

	config = args.config
	if args.autoconfig:
		config = AUTO_CONFIG
	
	return args.mode, config, args.broker


def run(mode, config, broker_host):
	logging.info("MODE: {0}".format(mode))
	logging.info("CONFIG: {0}".format(config))
	logging.info("BROKER HOST: {0}".format(broker_host))

	broker.Broker().set_host(broker_host)

	if mode == "servos":
		# subscribe for each topic and apply the relative action
		logging.info("Run Servos")
		servos.run(config) 

	if mode == "sensors":
		# multi threads: polls sensor status and 
		# publish the status via MQTT protocol to the MQTT broker 
		# one topic per sensor type
		logging.info("Run Sensors")
		sensors.run(config)

	if mode == "ctrl":
		# multi threads: polls sensor status and 
		# publish the status via MQTT protocol to the MQTT broker 
		# one topic per sensor type
		logging.info("Run Controller")
		controller.run(config)


if __name__ == "__main__":
	mode, config, broker_host = parse_input()
	run(mode, config, broker_host)

