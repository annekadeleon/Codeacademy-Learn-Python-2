#opens a file called text.txt which can be written on, stored in my_file
with file("text.txt", "w") as my_file:
	#writes "Any text you like" on my_file
	my_file.write("Any text you like")

#my_file.closed checks if my_file is closed
if my_file.closed == False:
	#closes file
	my_file.close()

#outputs True since my_file is closed
print my_file.closed
