import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from controller import controller
from sensors import sensors
from servos import servos


import argparse

DEFAUL_CONGIF_FILE = "pollicino.yaml"

def parse_input():
	parser = argparse.ArgumentParser(allow_abbrev=False)
	parser.add_argument('-m','--mode', action='store', choices=['servos', 'sensors', 'ctrl'], required=True)
	parser.add_argument('-c','--config', action='store', default=DEFAUL_CONGIF_FILE)
	args = parser.parse_args()
	return args.mode, args.config


def run(mode, config):
	if mode == "servos":
		# subscribe for each topic and apply the relative action
		print("Run Servos")
		servos.run(config) 

	if mode == "sensors":
		# multi threads: polls sensor status and 
		# publish the status via MQQT protocol to the MQTT broker 
		# one topic per sensor type
		print("Run Sensors")
		sensors.run(config)

	if mode == "ctrl":
		# multi threads: polls sensor status and 
		# publish the status via MQQT protocol to the MQTT broker 
		# one topic per sensor type
		print("Run Controller")
		controller.run(config)

if __name__ == "__main__":
	mode, config = parse_input()
	run(mode, config)
