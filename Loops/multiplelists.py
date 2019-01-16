list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

#zip creates pairs of elements in lists
#stops making pairs at end of shorter list
for a, b in zip(list_a, list_b):
  #compares each pair of elements and prints the larger one
  if a > b:
    print a
  else:
    print b
