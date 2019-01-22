#takes integers from 1-5, multiplies it by 2, if the product is a multiple of 3, it is put into doubles_by_3 list
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

#takes integers from 1-11, takes its square, and if the square is divisible by 2, it is put into even_sqaures list
even_squares = [i ** 2 for i in range(1, 12) if i % 2 == 0]

#prints [4, 16, 36, 64, 100]
print even_squares
