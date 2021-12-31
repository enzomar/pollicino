import logging

from . import base

try:
    import RPi.GPIO as GPIO
except BaseException:
    pass


class Fogger(base.Base):
    def __init__(self, servo_id):
        super().__init__('fogger', servo_id)

    def _hw_set(self, state):
        logging.info('')

    def _hw_get(self):
        logging.info('')
        return 0
