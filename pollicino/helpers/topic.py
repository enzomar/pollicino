PATTERN_STATUS = '{sector}/{category}/{dev_name}/{dev_id}'
# PATTERN_STATUS_SUB    ='{sector}/{category}/#'
PATTERN_CMD_PUB = '{sector}/{category}/{dev_name}/{dev_id}/set'
PATTERN_CMD_SUB = '{sector}/{category}/{dev_name}/+/set'


def status(dev_id, dev_name, category, sector):
    return PATTERN_STATUS.format(
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


def cmd_sub(dev_name, category, sector):
    return PATTERN_CMD_SUB.format(sector=sector, category=category, dev_name=dev_name)


def extract(topic):
    splitted = topic.split('/')
    return splitted[0], splitted[1], splitted[2], splitted[3]
