#class called Car inherits objects
class Car(object):
	#member variable condition initialised to "new"
	condition = "new"
	
	#method __init__() initialises input variables
	def __init__(self, model, colour, mpg):
		self.model = model
		self.colour = colour
		self.mpg = mpg
	
	#returns the string "This is a [colour] [model] with [mpg] MPG." when called
	def display_car(self):
		return ("This is a " + self.colour + " " + self.model + " with " + str(self.mpg) + " MPG.")
	
	def drive_car(self):
		self.condition = "used"

#object my_car is an instance of Car
my_car = Car("DeLoran", "silver", 88)

#outputs new
print my_car.condition
#overrides the member variable condition and changes its value to "used
print my_car.drive_car()
#outputs used
print my_car.condition
