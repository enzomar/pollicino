from multiprocessing import Process
import time
import functools
import sys
import logging


class Base(object):
	def __init__(self, type, id):
		self.type = type
		self.id = id
		self.state = 'off' # very dangerous, read the actual value
		self.process = None


	def on(self):
		self._set(1)


	def off(self):
		self._set(0)


	def _set(self, state):
		if state == 0:
			if self.process:
				self.process.terminate()
				self.process = None
		if state == self.state:
			return
		initial_state = self._hw_get()
		if initial_state != state:
			self._hw_set(state)

	def pulse(self, state_a, seconds_a, state_b, seconds_b, num_of_run):
		if self.process:
			if self.process.is_alive():
				return

		self.process = Process(target=self._update, args=(state_a, seconds_a, state_b, seconds_b, num_of_run))
		self.process.start()

	def square(self, state_a, seconds_a):
		self.pulse(state_a, seconds_a, 0,  0, 1)

	def _hw_set(self, state):
		logging.error("Implement me")

	def _hw_get(self):
		logging.error("Implement me")



	def _update(self, state_a, seconds_a, state_b, seconds_b, num_of_run):
		#update the sensor to amplitude 
		initial_state = self._hw_get()
		for n in range(num_of_run):
			logging.debug("[{0}] set {1} for {2}s".format(n, state_a, seconds_a), flush=True)
			self._hw_set(state_a)
			time.sleep(seconds_a)
			logging.debug("[{0}] set {1} for {2}s".format(n, state_b, seconds_b), flush=True)
			self._hw_set(state_b)
			time.sleep(seconds_b) 
		self._hw_set(initial_state)


if __name__ == "__main__":
	b = Base(0,0)
	b.square(1,5)
	b.pulse(1,5,0,3,2)
	print('going on...', flush=True)
	time.sleep(2)
	b.off()


		
