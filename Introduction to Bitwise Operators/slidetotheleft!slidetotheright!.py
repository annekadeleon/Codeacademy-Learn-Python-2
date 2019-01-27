#12
shift_right = 0b1100
#1
shift_left = 0b1

#shifts 1100 two slots to the right (11 = 3)
shift_right >> 2
#shifts 1 two slots to the left (100 = 4)
shift_left << 2

#prints 0b11
print bin(shift_right)
#prints 0b100
print bin(shift_left)
