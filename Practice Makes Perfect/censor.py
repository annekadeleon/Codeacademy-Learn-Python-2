def censor(text, word):
	new_text = []
	
	censor = "*" * len(word)
	
	for w in text.split(" "):
		new_text.append(w)
	
	count = 0
	while count < len(new_text):
		if new_text[count] == word:
			new_text[count] = censor
		count += 1
	
	return " ".join(new_text)
	
textr = raw_input("Text: ")
wordr = raw_input("Word: ")
print censor(textr, wordr), 
