def factorial(x):
	num = int(x)
	factorial = 1
	while num > 0:
		factorial *= num
		num -= 1
	return factorial

integ = raw_input("Enter an integer to calculate its factorial: ")
print factorial(integ)
