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

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(process)d - %(processName)s - %(levelname)s - %(message)s')


DEFAUL_TOPOLOGY_FILE = "pollicino.yaml"



def parse_input():
	parser = argparse.ArgumentParser(allow_abbrev=False)
	parser.add_argument('-m','--mode', action='store', choices=['servos', 'sensors', 'ctrl'])
	parser.add_argument('-t','--topology', action='store', default=DEFAUL_TOPOLOGY_FILE)
	parser.add_argument('-b','--broker', action='store', default='0.0.0.0')

	args = parser.parse_args()
	return args.mode, args.topology, args.broker


def run(mode, topology, broker_host):
	broker.Broker().set_host(broker_host)

	if mode == "servos":
		# subscribe for each topic and apply the relative action
		logging.info("Run Servos")
		servos.run(topology) 

	if mode == "sensors":
		# multi threads: polls sensor status and 
		# publish the status via MQTT protocol to the MQTT broker 
		# one topic per sensor type
		logging.info("Run Sensors")
		sensors.run(topology)

	if mode == "ctrl":
		# multi threads: polls sensor status and 
		# publish the status via MQTT protocol to the MQTT broker 
		# one topic per sensor type
		logging.info("Run Controller")
		controller.run(topology)

if __name__ == "__main__":
	mode, topology, broker_host = parse_input()
	run(mode, topology, broker_host)

