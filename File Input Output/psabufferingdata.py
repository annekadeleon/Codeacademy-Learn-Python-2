#opens a file called text.txt which can be written on, stored in write_file
write_file = open("text.txt", "w")

#opens a file called text.txt which can be read, stored in read_file
read_file = open("text.txt", "r")

#writes to the file
write_file.write("Not closing files is VERY BAD.")

#closes write_file
write_file.close()

#outputs read_file
print read_file.read()

#closes file
read_file.close()
