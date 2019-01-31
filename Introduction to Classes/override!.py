class Employee(object):
	"""Models real-life employees!"""
	def __init__(self, employee_name):
		self.employee_name = employee_name
	
	def calculate_wage(self, hours):
		self.hours = hours
		#full time employees get $20 per hour
		return hours * 20.00

#new class PartTimeEmployee inheritss class Employee
class PartTimeEmployee(Employee):
	#overridea calculate_wage of Employee
	def calculate_wage(self, hours):
	self.hours = hours
	#part time employees get $12 per hour
	return hours * 12.00
