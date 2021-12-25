import paho.mqtt.client as mqtt
from helpers import broker
from helpers import topic
import logging



def handle_moisture(value, threshold):
	# if the ground is dry, it is ime to water else stop the water
	command = "off"
	if value < int(threshold):
		command = 'on'
	return command

def handle_meteo(value, threshold):
	# if it is raining, stop the water
	command = None
	if value == 'Clouds' or value == 'Rain':
		command = 'off'
	return command		
	

def on_connect(client, userdata, flags, rc):
	logging.info("Connected with result code "+str(rc))
	logging.info("Subscribing to: {0}".format(userdata['topic_sub']))
	client.subscribe(userdata['topic_sub'])


def on_message(client, userdata, msg):

	value = float(msg.payload.decode())
	topic_pub = userdata['topic_pub']
	threshold = userdata['threshold']
	sector, category, sensor_type, sensor_id = topic.extract(msg.topic)

	command = None
	if sensor_type == "moisture":
		command = handle_moisture(value, threshold)

	if sensor_type == "meteo":
		command = handle_meteo(value, threshold)

	if command:
		client.publish(topic_pub, command)
		logging.info("{0}:{1} -> {2}:{3}".format(msg.topic, value, topic_pub, command))
	else:
		logging.info("{0}:{1} -> None".format(msg.topic, value))



class Watering(object):
	def __init__(self, topic_sub, topic_pub, threshold):
		self.config = dict()
		self.config['topic_sub'] = topic_sub
		self.config['topic_pub'] = topic_pub
		self.config['threshold'] = threshold
		self.name = 'watering'

	def run(self):
		logging.info("Watering")
		client = broker.connect()
		client.on_connect = on_connect
		client.on_message = on_message
		client.user_data_set(self.config)
		client.loop_forever()

