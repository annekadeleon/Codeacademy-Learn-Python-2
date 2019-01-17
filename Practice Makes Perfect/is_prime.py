def is_prime(x):
	x = int(x)
	#numbers less than 2 are not prime
	if x < 2:
		return False
	else:
		for n in range(2, x - 1):
			if x % n == 0:
				return False
		return True

num = raw_input("Enter an integer to know if it is a prime number: ")
print is_prime(num)
