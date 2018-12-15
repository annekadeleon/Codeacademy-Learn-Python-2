# False or ((not True) and True)
bool_one = False or not True and True

# (False and (not True)) or True
bool_two = False and not True or True

#True and (not (False or False))
bool_three = True and not (False or False)

# (not (not True)) or (False and (not True))
bool_four = not not True or False and not True

#False or (not (True and True))
bool_five = False or not (True and True)
