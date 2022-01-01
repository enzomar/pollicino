import logging

from pollicino.helpers import broker


def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code " + str(rc))
    logging.info("Subscribing to: {0}".format(userdata['topic_sub']))
    client.subscribe(userdata['topic_sub'])


def on_message(client, userdata, msg):
    pass


class Brightness(object):
    def __init__(self, topic_sub, topic_pub, threshold):
        self.config = dict()
        self.config['topic_sub'] = topic_sub
        self.config['topic_pub'] = topic_pub
        self.config['threshold'] = threshold
        self.name = 'brightness'

    def run(self):
        logging.info("Brightness")
        client = broker.Broker().connect()
        client.on_connect = on_connect
        client.on_message = on_message
        client.user_data_set(self.config)
        client.loop_forever()
