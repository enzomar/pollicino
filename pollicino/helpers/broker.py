import paho.mqtt.client as mqtt
import time
import logging
MOSQUITTO_CONF = "broker/mosquitto.conf"
REGEX = '^listener ([0-9]+) ([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Broker(metaclass=Singleton):
    __metaclass__ = Singleton

    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 1883

    def set_host(self, host):
        self.host = host
        logging.info("Broker host set to {0}".format(host))

    def set_port(self, port):
        self.port = port

    def connect(self):
        client = mqtt.Client()
        logging.info("Connecting to {0}:{1}".format(self.host, self.port))
        connected = False
        while not connected:
            try:
                client.connect(self.host, self.port, 60)
                connected = True
            except ConnectionRefusedError as ex:
                logging.error(ex)
                logging.info("Retring in {0} seconds".format(5))
                time.sleep(5)
        return client
