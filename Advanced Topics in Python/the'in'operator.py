my_dict = {
"Name": "Anneka",
"Age": 19,
"BDFL": False
}

print my_dict.keys()
print my_dict.values()

#for every key in the dictionary
for key in my_dict:
	#print the key and it's value on the same line with a space inbetween
	print key, my_dict[key]
