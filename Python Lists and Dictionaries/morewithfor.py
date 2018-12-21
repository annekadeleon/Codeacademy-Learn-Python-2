start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  #adds new items in square_list from start_list
  square_list.append(number ** 2)
square_list.sort()

print square_list
