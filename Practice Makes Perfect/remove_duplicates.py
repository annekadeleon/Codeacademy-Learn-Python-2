def remove_duplicates(a_list):
	new_list = []
	for item in a_list:
		if item not in new_list:
			new_list.append(item)
	return new_list

input_list = [1,1,2,2]

#prints [1, 2]
print remove_duplicates(a_list)
