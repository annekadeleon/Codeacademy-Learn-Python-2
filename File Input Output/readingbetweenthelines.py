#opens file called text.txt which can be read, and is stored in my_file
my_file = open("text.txt", "r")

#iterated 3 times
for i in range(3):
	#outputs one line of my_file
	print my_file.readline()

#closes my_file
my_file.close()
