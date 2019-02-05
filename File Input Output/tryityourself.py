#opens file called text.txt which can be written on, stored in my_file
with file("text.txt", "w") as my_file:
	#writes to my_file
	my_file.write("Any data you like")
