import paho.mqtt.client as mqtt
from helpers import broker
from helpers import topic
import logging



def on_connect(client, userdata, flags, rc):
	logging.info("Connected with result code "+str(rc))
	logging.info("Subscribing to: {0}".format(userdata['topic_sub']))
	client.subscribe(userdata['topic_sub'])
	logging.info("Done")


def on_message(client, userdata, msg):
	value = float(msg.payload.decode())
	topic_pub = userdata['topic_pub']
	command = "off"
	if value < 5:
		command = 'on'
	
	client.publish(topic_pub, command)
	logging.info("{0}:{1} -> {2}:{3}".format(msg.topic, value, topic_pub, command))

class Watering(object):
	def __init__(self, topic_sub, topic_pub):
		self.config = dict()
		self.config['topic_sub'] = topic_sub
		self.config['topic_pub'] = topic_pub
		self.name = 'watering'

	def run(self):
		logging.info("Watering")
		client = broker.connect()
		client.on_connect = on_connect
		client.on_message = on_message
		client.user_data_set(self.config)
		client.loop_forever()

