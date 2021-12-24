from servos import loader
from helpers import broker
from helpers import topic
import logging


TOPIC = 'servos/#'

def on_connect(client, userdata, flags, rc):
  logging.debug("Connected with result code "+str(rc))
  logging.info("Subscribing to: {0}".format(TOPIC))
  client.subscribe(TOPIC)

def on_message(client, userdata, msg):
  area, sensor_type, sensor_id = topic.extract(msg.topic)
  value = msg.payload.decode()

  servo_instance = userdata[sensor_type][sensor_id]
  if value == 'on':
    # to check this check is really usefull
    if servo_instance.status == 'off':
      servo_instance.on()
  else: 
    servo_instance.off()


def run(configuration_file):
  servos_pool = loader.load(configuration_file)

  client = broker.connect()
  client.on_connect = on_connect
  client.on_message = on_message
  client.user_data_set(servos_pool)
  client.loop_forever()

