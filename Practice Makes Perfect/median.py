def median(a_list):
	a_list = sorted(a_list)
	list_len = len(a_list) - 1
	if list_len % 2 == 0:
		middle1 = (list_len + 1)/2 - 1
		middle2 = middle1 + 1
		median1 = a_list[middle1]
		median2 = a_list[middle2]
		return ((float(median1) + float(median2)) / 2.0
	else:
		median = a_list[list_len / 2]
		return median
