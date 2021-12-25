from servos import base
import logging

class Waterpump(base.Base):
	def __init__(self, servo_id):
		super().__init__('waterpump', servo_id)

	def _hw_set(self, state):
		logging.info('')

	def _hw_get(self):
		logging.info('')
		return 0