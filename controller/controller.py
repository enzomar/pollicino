from controller import watering
from controller import loader
from multiprocessing import Pool
import signal
import logging


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def run(configuration_file):
  list_of_ctrl = loader.load(configuration_file)

  pool = Pool(len(list_of_ctrl), init_worker)
  try:
      for each in list_of_ctrl:
          pool.apply_async(each.run)

      pool.close()
      pool.join()

  except KeyboardInterrupt:
      logging.info("Caught KeyboardInterrupt, terminating workers")
      pool.terminate()
      pool.join()



