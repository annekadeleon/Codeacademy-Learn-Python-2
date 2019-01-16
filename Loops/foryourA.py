phrase = "A bird in the hand..."

#prints "X   b i r d   i n   t h e   h X n d . . ."
for char in phrase:
  #filters out letter A from string
  if char.lower() == "a":
    #comma after print statement means next print is on the same line
    print "X",
  else:
    print char,
