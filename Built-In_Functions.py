#function distance_from_zero takes one argument args
def distance_from_zero(args):
	#if args is an integer or float type
	if (type(args) == int) or (type(args) == float):
		#returns absolute value (distance from zero) of args
		return abs(args)
	#if args is not an integer or float type
	else:
		#returns "Nope"
		return("Nope")
