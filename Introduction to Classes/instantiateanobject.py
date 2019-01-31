#class called  Triangle
class Triangle(object):
	#member variable number_of_sides
	number_of_sides = 3
	#method __init__() initialises objects
	def __init__(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
	
	#init check_angles() verifies if angles add up to 180
	def check_angles(self):
		if (self.angle1 + self.angle2 + self.angle3) == 180:
			return True
		else:
			return False

#my_triangle is an instance of class Triangle with angles 90, 30, 60
my_triangle = Triangle(90, 30, 60)
#outputs 3
print my_triangle.number_of_sides
#outputs True
print my_triangle.check_angles()
