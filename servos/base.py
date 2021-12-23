class Base(object):
	def __init__(self, type, id):
		self.type = type
		self.id = id
		self.status = 'off' # very dangerous, read the actual value

	def on(self):
		self.status = 'on'

	def off(self):
		self.status = 'off'

	def status(self):
		return self.status