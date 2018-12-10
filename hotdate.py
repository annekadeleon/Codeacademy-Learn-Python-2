from datetime import datetime
now = datetime.now()

#Prints current date as mm/dd/yyy
print ('%02d/%02d/%04d') % (now.month, now.day, now.year)
