#function, check_bit4, takes in input, an integer, as one argument
def check_bit4(input):
	#fourth bit from the right is on
	check = 0b1000
	#compares input and check
	desired = input & check
	#if the fourth bit from the right in the input was on, output "on", if not, output "off"
	if desired > 0:
		return "on"
	else:
		return "off"
