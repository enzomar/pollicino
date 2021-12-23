PATTERN='{0}/{1}/{2}'

def build_sensor(id,type,area='pollicino'):
	return PATTERN.format(area,type,id)

def build(id,type,area='pollicino'):
	return PATTERN.format(area,type,id)

def extract(topic):
	splitted = topic.split('/')
	# area, type, id
	return splitted[0], splitted[1], int(splitted[2])