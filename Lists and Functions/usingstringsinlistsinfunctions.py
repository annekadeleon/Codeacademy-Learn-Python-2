n = ["Michael", "Lieberman"]

def join_strings(words):
	result = ""
	for word in words:
		result += word
	return result

#prints MichaelLieberman
print join_strings(n)
