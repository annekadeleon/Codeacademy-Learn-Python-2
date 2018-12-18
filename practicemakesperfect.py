def cube(number):
  return number ** 3

def by_three(number):
  if (number % 3) == 0:
    cube(number)
    return cube(number)
  else:
    return False
