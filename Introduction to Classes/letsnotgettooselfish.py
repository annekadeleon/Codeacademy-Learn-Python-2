class Animal(object):
	#first parameter, self, refers to object being created - gives object its identity
	def __init__(self, name):
		#lets function know that name refers to object's name
		self.name = name
