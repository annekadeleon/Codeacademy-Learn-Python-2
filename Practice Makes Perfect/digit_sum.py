def digit_sum(n):
	total = 0
	string_n = str(n)
	for char in string_n:
		total += int(char)
	return total

pos_int = raw_input("Enter a positive integer: ")

print digit_sum(pos_int)
