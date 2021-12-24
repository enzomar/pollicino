from servos import loader
from helpers import broker
from helpers import topic
import logging



def on_connect(client, userdata, flags, rc):
  logging.debug("Connected with result code "+str(rc))
  servos_pool = userdata['servos_pool']
  topics_sub = list()
  for each in servos_pool:
    topics_sub.append( (servos_pool[each]['topic'], 0))
  logging.info("Subscribing to: {0}".format(topics_sub))
  client.subscribe(topics_sub)

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
  userdata = dict()
  userdata['servos_pool'] = servos_pool
  client.user_data_set(userdata)
  client.loop_forever()

