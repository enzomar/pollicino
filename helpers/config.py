import json

import yaml


def _parse_yaml_to_dict(values):
    output = dict()

    # print(values)
    for sector in values['sectors']:
        sec_id = sector['id']
        output[sec_id] = dict()
        output[sec_id]['sensors'] = dict()
        for sensor in sector['sensors']:
            sensor_id = sensor['id']
            output[sec_id]['sensors'][sensor_id] = dict()
            for each in sensor:
                output[sec_id]['sensors'][sensor_id][each] = sensor[each]

    return output


def load(configuration_file):
    output = dict()
    with open(configuration_file, "r") as stream:
        try:
            values = yaml.safe_load(stream)
            return values
        except yaml.YAMLError as exc:
            logging.error(exc)


if __name__ == "__main__":
    print(json.dumps(load("../pollicino.yaml")))

"""
sectors: 
  - id: pollicino
    sensors:
        - id: 0
          type: moisture
          gpio:
            pin: 10
            mode: BMD
          polling_seconds: 1
        - id: 1
          type: photoresistor
          gpio:
            pin: 10
            mode: BMD
          polling_seconds: 2
        - id: 2
          type: meteo
          polling_seconds: 4
    servos:
      - id: 0
        type: waterpump
        gpio:
          pin: 10
          mode: BMD
        off_after_min: 60

    controllers:
      - type: watering
      	links:
        	- sensors_id: 0 
        	  servo_id: 0
        	  threshold: 5

"""
