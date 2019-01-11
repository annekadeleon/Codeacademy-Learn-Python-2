def my_function(x):
	for i in range(0, len(x)):
		x[i] = x[i]
	return x

#returns list containing [0, 1, 2]
print my_function(range(3))
