#class Point3D inherits object
class Point3D(object):
	#method __init__() initialises member variables
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	#method __repr__() represents objects in the format (x, y, z)
	def __repr__(self):
		return "(%d, %d, %d)" % (self.x, self.y, self.z)

#my_point is an instance of class Point3D with input 1, 2, 3
my_point = Point3D(1, 2, 3)

#outputs (1, 2, 3)
print my_point
