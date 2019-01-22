#takes integers from 1-10, takes its cube, and puts it in the list cubes_by_four if it is a multiple of 4
cubes_by_four = [i ** 3 for i in range(1, 11) if (i ** 3) % 4 == 0]

#prints [8, 64, 216, 512, 1000]
print cubes_by_four
