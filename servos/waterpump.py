from servos import base

class Waterpump(base.Base):
	def __init__(self, servo_id):
		super().__init__('waterpump', servo_id)
