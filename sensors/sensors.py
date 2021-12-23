from helpers import broker
from sensors import loader
from multiprocessing import Pool, Process
import signal, time

def read_and_publish(sensor):
	client = broker.connect()
	try:
		while True:
			s_instance = sensor['instance']
			measure = s_instance.fetch()
			s_topic = sensor['topic']	
			client.publish(s_topic, str(measure))
			print("{0} -> {1}".format(s_topic , str(measure)))
			time.sleep(int(s_instance.polling_seconds))
	except Exception as ex:
		print(ex)
		client.disconnect()
		raise ex


def init_worker():
	signal.signal(signal.SIGINT, signal.SIG_IGN)

def run(configuration_file):
	list_of_sensors = loader.load(configuration_file)
	pool = Pool(len(list_of_sensors), init_worker)
	try:
		for each in list_of_sensors:
			pool.apply_async(read_and_publish, args=(each,))
		pool.close()
		pool.join()

	except KeyboardInterrupt:
	  print("Caught KeyboardInterrupt, terminating workers")
	  pool.terminate()
	  pool.join()




