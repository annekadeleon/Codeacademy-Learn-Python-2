grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#prints all grades in new line
def print_grades(grades_input):
	for grade in grades_input:
		print grade

#calls print_grades function with grades as input
print_grades(grades)

#calculates and returns total of all grades
def grades_sum(grades_input):
	total = 0
	for grade in grades_input:
		total += grade
	return total

#calls grades_sum function with grades as input
print grades_sum(grades)

#calculates and returns average of grades
def grades_average(grades_input):
	#calls grades_sum with grades_input and divides it by the number of grades
	average = grades_sum(grades_input) / float(len(grades_input))
	return average

#calls grades_avaerage with grades as input
print grades_average(grades)

#calculates and returns variance of grades
def grades_variance(scores):
	#gets average of grades from grades_average
	average = grades_average(scores)
	variance = 0
	#calculates variance
	for score in scores:
		variance += (average - score) ** 2
	return variance / len(scores)

#calls grades_variance with grades as input
print grades_variance(grades)

#calculates and returns standard deviation with variance as input
def grades_std_deviation(variance):
	return variance ** 0.5

#calls grades_variance with grades as input
variance = grades_variance(grades)

#calls grades_std_deviation with grades as input
print grades_std_deviation(grades)
