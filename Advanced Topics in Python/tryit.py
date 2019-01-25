#list of squares of numbers 1-10
squares = [x ** 2 for x in range(1,11)]

#prints [36, 49, 64]
print filter(lambda x: x >= 30 and x <= 70, squares)
