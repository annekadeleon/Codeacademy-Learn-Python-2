class Animal(object):
	"""Makes cute animals."""
	#member variable is_alive is only available to members of the Animal class
	is_alive = True
	#__init__() is a function in the class Animal, so it is a method
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def description(self):
		print self.name
		print self.age

#hippo is an instance variable of the Animal clas
hippo = Animal("Gloria", 20)
#calls description method
#outputs Gloria\n20
hippo.description()
