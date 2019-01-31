class Animal(object):
	"""Makes cute animals."""
	#initialises instance objects
	def __init__(self, name, age, is_hungry):
		self.name = name
		self.age = age
		self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

#outputs Jeffrey 2 True
print zebra.name, zebra.age, zebra.is_hungry
#outputs Bruce 1 False
print giraffe.name, giraffe.age, giraffe.is_hungry
#outputs Chad 7 True
print panda.name, panda.age, panda.is_hungry
