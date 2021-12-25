import json, os
from jsonschema import validate
import jsonschema
import logging


def _get_schema():
	"""This function loads the given schema available"""
	file_path = os.path.dirname(os.path.abspath(__file__))
	with open(file_path+'/command.json', 'r') as file:
		schema = json.load(file)
	return schema

def _build(mode, states, repetition):
	json_data = dict()
	json_data['mode']=mode
	json_data['states']=states
	json_data['repetition']=repetition
	schema = _get_schema()

	try:
		validate(instance=json_data, schema=schema)
	except jsonschema.exceptions.ValidationError as err:
		logging.error(err)
		print(err)
		return None
	return json.dumps(json_data)

def switch(value):
	return _build("switch", [{"value":str(value), "seconds": 0}], 1)

def square(value, seconds):
	return _build("square", [{"value":str(value), "seconds": seconds}], 1)

def pulse(on, seconds_on, off, seconds_off, repetition):
	state = list()
	state.append({"value":str(on), "seconds": seconds_on})
	state.append({"value":str(off), "seconds": seconds_off})
	return _build("pulse", state, repetition)

if __name__ == "__main__":
	print(switch(3))
	print(square(3,5))
	print(pulse(3,5,0,10,5))

