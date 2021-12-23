from sensors import base

class Moisture(base.Base):
	def __init__(self, sensor_id):
		super().__init__('moisture', sensor_id)

