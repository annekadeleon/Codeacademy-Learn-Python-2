def purify(list_of_numbers):
	even_list = []
	for num in list_of_numbers:
		if num % 2 == 0:
			even_list.append(num)
	return even_list

print("Enter a bunch of numbers, then enter 'x' when you're done.\n
This will return the even numbers among the numbers you entered.")

numbers = []
number = ""

while number != "x":
	number = raw_input()
	number = number.lower()
	if number == "x":
		break
	else:
		number = int(number)
		numbers.append(number)

print purify(numbers)
