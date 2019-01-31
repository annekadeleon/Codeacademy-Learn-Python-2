#class called Employee
class Employee(object):
	"""Models real-life employees!"""
	#method __init__() initialises employee's name
	def __init__(self, employee_name):
		self.employee_name = employee_name
	
	#method calculate_wage() calculates hours worked, and therefore wage of full time employee
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 20.00

#new class PartTimeEmployee inherits class Employee
class PartTimeEmployee(Employee):
	#overrides method calculate_wage() from parent class Employee
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 12.00
	
	#method full_time_wage calculates part time employee's wage as a full time employee
	def full_time_wage(self, hours):
		#accesses method calculate_wage() from parent class Employee without overriding
		return super(PartTimeEmployee, self).calculate_wage(hours)

#instance of PartTimeEmployee
milton = PartTimeEmployee("Miltion")
#outputs 200.00
print milton.full_time_wage(10)
