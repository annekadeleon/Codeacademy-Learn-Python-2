#empty list
threes_and_fives = []

#iterate through numbers 1-15
for x in range(1,16):
	#if number is divisible by 3 or 5
	if (x % 3 == 0) or (x % 5 == 0):
		#add number to list
		threes_and_fives.append(x)
