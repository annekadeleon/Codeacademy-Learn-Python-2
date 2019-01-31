#class named Animal
class Animal(object):
	def __init__(self, name):
		self.name = name

zebra = Animal("Jeffrey")
#prints Jeffrey
print zebra.name
