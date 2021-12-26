import json
import logging

from helpers import broker
from helpers import topic
from servos import loader


def on_connect(client, userdata, flags, rc):
    logging.debug("Connected with result code " + str(rc))
    servos_pool = userdata['servos_pool']
    topics_sub = list()
    for each in servos_pool:
        topics_sub.append((servos_pool[each]['topic'], 0))
    logging.info("Subscribing to: {0}".format(topics_sub))
    client.subscribe(topics_sub)


def on_message(client, userdata, msg):
    logging.debug("on_message")
    sector, category, sensor_type, sensor_id = topic.extract(msg.topic)
    value = json.loads(msg.payload.decode())
    logging.info("{0}:{1}".format(msg.topic, value))
    servo_instance = userdata['servos_pool'][sensor_id]['instance']
    try:
        if value['mode'] == 'switch':
            if value['states'][0] == 1:
                servo_instance.on()
            else:
                servo_instance.off()
    except TypeError as ex:
        logging.error("{0}".format(str(ex)))


def run(configuration_file):
    servos_pool = loader.load(configuration_file)

    client = broker.connect()
    client.on_connect = on_connect
    client.on_message = on_message
    userdata = dict()
    userdata['servos_pool'] = servos_pool
    client.user_data_set(userdata)
    client.loop_forever()
