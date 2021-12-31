import logging

import yaml

from pollicino.controller.fogger import Fogger
from pollicino.controller.scheduler import Scheduler
from pollicino.controller.watering import Watering
from pollicino.helpers import topic

CTRL_MAP = {'watering': Watering, 'scheduler': Scheduler, 'fogger': Fogger}


def load_standard(sector, c_type, links):
    c_class = CTRL_MAP[c_type]
    list_of_ctrls = list()
    for each in links:
        servo_id = str(each['servo_id'])
        servo_type = each['servo_type']
        sensor_id = str(each['sensor_id'])
        sensor_type = each['sensor_type']
        threashold = each['threshold']
        topic_sub = topic.status(sensor_id, sensor_type, 'sensors', sector)
        topic_pub = topic.cmd_pub(servo_id, servo_type, 'servos', sector)
        c_instance = c_class(topic_sub, topic_pub, threashold)
        list_of_ctrls.append(c_instance)
    return list_of_ctrls


def load_scheduler(sector, c_type, links):
    c_class = CTRL_MAP[c_type]
    list_of_ctrls = list()
    for each in links:
        servo_id = str(each['servo_id'])
        servo_type = each['servo_type']
        start = each['start']
        seconds = each['duration_seconds'] or None
        state = each['state']
        topic_pub = topic.cmd_pub(servo_id, servo_type, 'servos', sector)
        c_instance = c_class(start, state, topic_pub, seconds)
        list_of_ctrls.append(c_instance)
    return list_of_ctrls


def load(configuration_file):
    list_of_ctrls = list()
    with open(configuration_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            for sector in config:
                sector_config = config[sector]
                ctrls_config = sector_config['controllers']
                for ctrl in ctrls_config:
                    c_type = ctrl['type']
                    if c_type == "scheduler":
                        list_of_ctrls.extend(load_scheduler(
                            sector, c_type, ctrl['links']))
                    else:
                        list_of_ctrls.extend(load_standard( sector, c_type, ctrl['links']))
        except yaml.YAMLError as exc:
            logging.info(exc)
    logging.debug(list_of_ctrls)
    return list_of_ctrls
