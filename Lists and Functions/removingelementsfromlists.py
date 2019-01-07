n = [1, 3, 5]

#removes 2nd item and returns it
n.pop(1)

#prints [1, 5]
print n

#removes item if found
n.remove(5)

#prints [1]
print n

#removes 1st item without returning it
del(n[0])

#prints nothing
print n
