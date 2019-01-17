def reverse(text):
	chars_in_string = []
	reverse = ""
	for char in text:
		chars_in_string.append(char)
	
	last = len(chars_in_string) - 1
	
	while last >= 0:
		reverse += chars_in_string[last]
		last -= 1
	return reverse

word = raw_input("Enter a word to see it in reverse: ")
print reverse(word)
