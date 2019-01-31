#class Triangle inherits object
class Triangle(object):
	#member variable number_of_sides initialised to 3
	number_of_sides = 3
	#method __init__() initialises objects
	def __init__(self, angle1, angle2, angle3):
		self.angle = angle1
		self.angle = angle2
		self.angle = angle3
	
	#method check_angles() verifies that angles add up to 180
	def check_angles(self):
		if (self.angle1 + self.angle2 + self.angle3) == 180:
			return True
		else:
			return False

#my_triangle is an instance of the class Triangle with the angles 90, 30, 60
my_triangle = Triangle(90, 30, 60)
#outputs 3
print my_triangle.number_of_sides
#outputs True
print my_triangle.check_angles()

#new class Equilateral inherits Triangle
class Equilateral(Triangle):
	#member variable angle initialised to 60
	angle = 60
	#method __init__() initialises objects
	def __init__(self):
		self.angle1 = self.angle
		self.angle2 = self.angle
		self.angle3 = self.angle
