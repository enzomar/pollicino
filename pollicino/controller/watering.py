import logging

from pollicino.helpers import broker
from pollicino.helpers import command
from pollicino.helpers import topic


def handle_humidity(value, threshold):
    # if the ground is dry, it is ime to water else stop the water
    cmd = command.switch(0)
    if value < int(threshold):
        cmd = command.square(1, 10)
    return cmd


def handle_moisture(value, threshold):
    # if the ground is dry, it is ime to water else stop the water
    cmd = command.switch(0)
    if value < int(threshold):
        cmd = command.square(1, 10)
    return cmd


def handle_meteo(value, threshold):
    # if it is raining, stop the water
    cmd = None
    if value == 'Clouds' or value == 'Rain':
        cmd = command.switch(0)
    return cmd


def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code " + str(rc))
    logging.info("Subscribing to: {0}".format(userdata['topic_sub']))
    client.subscribe(userdata['topic_sub'])


def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    topic_pub = userdata['topic_pub']
    threshold = userdata['threshold']
    sector, category, sensor_type, sensor_id = topic.extract(msg.topic)
    cmd = None
    if sensor_type == "moisture":
        cmd = handle_moisture(value, threshold)
    if sensor_type == "meteo":
        cmd = handle_meteo(value, threshold)
    if sensor_type == "humidity":
        cmd = handle_humidity(value, threshold)
    if cmd:
        client.publish(topic_pub, cmd)
        logging.info("{0}:{1} -> {2}:{3}".format(msg.topic, value, topic_pub, str(cmd)))
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
        client = broker.Broker().connect()
        client.on_connect = on_connect
        client.on_message = on_message
        client.user_data_set(self.config)
        client.loop_forever()
