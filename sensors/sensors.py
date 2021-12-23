import time
from helpers import broker
from sensors import loader

def read_and_publish(sensor, client):
	s_instance = sensor['instance']
	measure = s_instance.fetch()
	s_topic = sensor['topic']	
	client.publish(s_topic, str(measure))
	print("{0} -> {1}".format(s_topic , str(measure)))
	time.sleep(s_instance.polling_seconds)

def run(configuration_file):
	list_of_sensors, polling_seconds = loader.load(configuration_file)
	client = broker.connect()

	while(True):
		for sensor in list_of_sensors:
			read_and_publish(sensor, client)

	client.disconnect();
