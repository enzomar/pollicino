import re
MOSQUITTO_CONF="broker/mosquitto.conf"
REGEX='^listener ([0-9]+) ([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)'
import paho.mqtt.client as mqtt



def connect():
	client = mqtt.Client()
	host, port = host_port()
	print("Host: {0}".format(host))
	print("Port: {0}".format(port))
	client.connect(host,port,60)
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
					port = found_host_port.group(1)
					host = found_host_port.group(2)		
	except FileNotFoundError:
		print("Filenotfound")

	if not (host or port):
		host = "localhost"
		port = 1883

	return host, port

def host():
	# read mosquitto configuration file
	# and extract the ip:port
	return host_port()[0]

def port():
	# read mosquitto configuration file
	# and extract the ip:port
	return int(host_port()[1])

if __name__ == "__main__":
	print(host_port())
	#print(host())
	#print(port())
