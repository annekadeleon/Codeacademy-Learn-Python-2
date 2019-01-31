class Animal(object):
	"""Makes cute animals."""
	#member variables, is_alive and health, are available to all members of Animal class
	is_alive = True
	health = "good"
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def description(self):
		print self.name
		print self.age

#three instances of Animal
hippo = Animal("Gloria", 20)
sloth = Animal("Anneka", 19)
ocelot = Animal("Clemi", 18)

#outputs Gloria\n20
hippo.description()

#outputs "good" 3x
print hippo.health
print sloth.health
print ocelot.health
