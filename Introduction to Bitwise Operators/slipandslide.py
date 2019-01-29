def flip_bit(number, n):
	#want to flip the (n-1)th bit from the right
	mask = 0b1 << (n-1)
	#stores number with (n-1th) bit flipped
	result = number ^ mask
	return bin(result)
