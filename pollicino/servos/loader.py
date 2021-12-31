import logging

import yaml

from pollicino.helpers import topic
from pollicino.servos.fogger import Fogger
from pollicino.servos.waterpump import Waterpump

SERVO_MAP = {'waterpump': Waterpump, 'fogger': Fogger}


def load_servos(s_id, s_config, sector):
    s_type = s_config['type']
    s_class = SERVO_MAP[s_type.lower()]
    s_instance = s_class(s_id)
    s_topic = topic.cmd_sub('servos', sector)
    return s_instance, s_topic


def load(configuration_file):
    servos_pool = dict()
    with open(configuration_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            for sector in config:
                sector_config = config[sector]
                servos_config = sector_config['servos']
                for s_id in servos_config:
                    s_config = servos_config[s_id]
                    s_instance, s_topic = load_servos(s_id, s_config, sector)
                    servos_pool[s_id] = {'instance': s_instance, 'topic': s_topic}
        except yaml.YAMLError as exc:
            logging.info(exc)
    return servos_pool
