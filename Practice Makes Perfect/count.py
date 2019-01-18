def count(sequence, item):
	count = 0
	for num in sequence:
		if num == item:
			count += 1
	return count
