import yaml

from pollicino.helpers import topic
from pollicino.sensors.meteo import Meteo
from pollicino.sensors.moisture import Moisture
from pollicino.sensors.photoresistor import Photoresistor

DEFAULT_POLLING_SECONDS = 1

SENSORS_MAP = {'moisture': Moisture,
               'photoresistor': Photoresistor,
               'meteo': Meteo}


def load_sensor(s_id, s_config, sector):
    s_type = s_config['type']
    s_polling_seconds = s_config['polling_seconds'] or DEFAULT_POLLING_SECONDS
    s_pin_input = None
    try:
        s_pin_input = s_config['pin_input']
    except:
        pass
    s_class = SENSORS_MAP[s_type.lower()]
    s_instance = s_class(s_id)
    s_instance.polling_seconds = s_polling_seconds or None
    s_instance.pin_input = s_pin_input
    s_topic = topic.status(s_instance.id, s_instance.type, 'sensors', sector)
    return s_instance, s_topic


def load(configuration_file):
    list_of_sensors = list()
    with open(configuration_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            for sector in config:
                sector_config = config[sector]
                sensors_config = sector_config['sensors']
                for s_id in sensors_config:
                    s_config = sensors_config[s_id]
                    s_instance, s_topic = load_sensor(s_id, s_config, sector)
                    list_of_sensors.append({'instance': s_instance, 'topic': s_topic})
        except yaml.YAMLError as exc:
            logging.info(exc)
    return list_of_sensors
