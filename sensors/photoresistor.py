from sensors import base


class Photoresistor(base.Base):
    def __init__(self, sensor_id):
        super().__init__('photoresistor', sensor_id)
