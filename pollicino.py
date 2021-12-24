import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from controller import controller
from sensors import sensors
from servos import servos
from helpers import broker
import argparse
import logging

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(process)d - %(processName)s - %(levelname)s - %(message)s')


DEFAUL_CONGIF_FILE = "pollicino.yaml"



def parse_input():
	parser = argparse.ArgumentParser(allow_abbrev=False)
	parser.add_argument('-m','--mode', action='store', choices=['servos', 'sensors', 'ctrl'], required=True)
	parser.add_argument('-c','--config', action='store', default=DEFAUL_CONGIF_FILE)
	parser.add_argument('-b','--brokerhost', action='store', default="0.0.0.0:1883")
	args = parser.parse_args()
	return args.mode, args.config, args.brokerhost


def run(mode, config, brokerhost):
	broker.write(brokerhost)
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
	mode, config, brokerhost = parse_input()
	run(mode, config, brokerhost)
