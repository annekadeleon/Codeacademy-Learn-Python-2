def product(list_of_ints):
	product = 1
	for num in list_of_ints:
		product *= num
	return product

int_list = []

numbers = raw_input("Enter a list of integers separated by a comma to find the product of every number: ")

for num in numbers.split(","):
	num = int(num)
	int_list.append(num)

print product(int_list)
