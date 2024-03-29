from getmac import get_mac_address as gma

PATTERN_STATUS_PUB = '{sector}/{category}/{dev_name}/{dev_id}'
PATTERN_STATUS_SUB = '{sector}/{category}/{dev_name}/{dev_id}'
PATTERN_CMD_PUB    = '{sector}/{category}/{dev_name}/{dev_id}/set'
PATTERN_CMD_SUB    = '{sector}/{category}/{dev_name}/{dev_id}/set'


def status_pub(dev_id, dev_name, category, sector):
    return PATTERN_STATUS_PUB.format(
        sector=sector,
        category=category,
        dev_name=dev_name,
        dev_id=dev_id)

def status_sub(dev_id, dev_name, category, sector):
    return PATTERN_STATUS_SUB.format(
        sector=sector,
        category=category,
        dev_name=dev_name,
        dev_id=dev_id)


def cmd_pub(dev_id, dev_name, category, sector):
    return PATTERN_CMD_PUB.format(
        sector=sector,
        category=category,
        dev_name=dev_name,
        dev_id=dev_id)


def cmd_sub(dev_id, dev_name, category, sector):
    return PATTERN_CMD_SUB.format(
        sector=sector, 
        category=category, 
        dev_name=dev_name,
        dev_id=dev_id)


def extract(topic):
    splitted = topic.split('/')
    # sector, category, sensor_type, sensor_id
    return splitted[0], splitted[1], splitted[2], splitted[3]
