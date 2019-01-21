grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
	for grade in grades_input:
		print grade

def grades_sum(scores):
	total = 0
	for score in scores:
		total += score
	return total

def grades_average(grades_input):
	avg = grades_sum(grades_input) / float(len(grades_input))
	return avg

def grades_variance(scores):
	average = grades_average(scores)
	variance = 0
	for score in scores:
		variance += (average - score) ** 2
	return variance / len(score)

print grades_variance(grades)

def grades_std_deviation(variance):
	return variance ** 0.5

variance = grades_variance(grades)

print grades_std_deviation(variance)
