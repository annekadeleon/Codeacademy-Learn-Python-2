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
	
	#method drive_car() changes member variable condition to "used"
	def drive_car(self):
		self.condition = "used"

#new class called ElectricCar inherits Car
class ElectricCar(Car):
	#method __init() initialises new input variable battery_type as well as input variables from class Car
	def __init__(self, battery_type, model, colour, mpg):
		self.battery_type = battery_type
		self.model = model
		self.colour = colour
		self.mpg = mpg
	
	#method drive_car() changes member variable condition to "like new"
	def drive_car(self):
		self.condition = "like new"

#object my_car is an instance of Car
my_car = Car("DeLoran", "silver", 88)

#outputs new
print my_car.condition
#calls method drive_car() from class Car
my_car.drive_car()
#outputs used
print my_car.condition

#object my_car is an instance of ElectricCar
my_car = ElectricCar("molten salt", "Tesla Model S", "white", 125)
#outputs new
print my_car.condition
#calls method drive_car() from class ElectricCar
my_car.drive_car()
#outputs like new
print my_car.condition
