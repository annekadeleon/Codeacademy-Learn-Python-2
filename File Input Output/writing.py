#creates a list of numbers from 1-10 and squares each number, putting the squares in my_list
my_list = [i ** 2 for i in range(1,11)]

#opens a file called output.txt that can be written on and stores it as my_file
my_file = open("output.txt", "w")

#iterates through values in my_list
for i in my_list:
	#adds the value into my_file and makes a new line
	my_file.write(str(i) + "\n")

#closes my_file
my_file.close()
