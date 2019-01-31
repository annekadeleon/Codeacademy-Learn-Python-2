#class called Triangle
class Triangle(object):
	#member variable number_of_sides initialised
	number_of_sides = 3
	#class objects initialised in method __init__()
	def __init__(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
	
	#method check_anges() verifies if sum of angles are 180
	def check_angles(self):
		if (self.angle1 + self.angle2 + self.angle3) == 180:
			return True
		else:
			return False
