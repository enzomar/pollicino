import re
MOSQUITTO_CONF="broker/mosquitto.conf"
REGEX='^listener ([0-9]+) ([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)'
import paho.mqtt.client as mqtt
import logging

def write(brokerhost):
	content = "\
allow_anonymous true \n\
listener {0} {1}"
	host_port = brokerhost.split(':')
	host=host_port[0]
	try:
		port=host_port[1]
	except:
		port=1883
		pass

	content = content.format(port, host).strip()
	with open(MOSQUITTO_CONF, 'w') as conffile:
		conffile.write(content)

	logging.debug("Wrote {0}".format(content))



def connect():
	client = mqtt.Client()
	host, port = host_port()
	logging.info("Connecting to {0}:{1}".format(host, port))
	try:
		client.connect(host,port,60)
	except ConnectionRefusedError as ex:
		logging.info(ex)
		raise ex
	return client

def host_port():
	# read mosquitto configuration file
	# and extract the ip:port
	# ie.listener 1883 192.168.1.195

	# default
	host = None
	port = None
	
	try:
		with open(MOSQUITTO_CONF) as conffile:
			for each in conffile:
				found_host_port = re.search(REGEX, each)
				if found_host_port:
					port = int(found_host_port.group(1))
					host = found_host_port.group(2)		
	except FileNotFoundError:
		logging.info("Filenotfound")

	if not (host or port):
		host = "localhost"
		port = 1883

	return host, port


if __name__ == "__main__":
	logging.info(host_port())
	#logging.info(host())
	#logging.info(port())
