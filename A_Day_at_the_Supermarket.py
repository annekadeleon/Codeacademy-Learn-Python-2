#list called shopping_list
shopping_list = ["banana", "orange", "apple"]

#dictionary called stock
stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

#dictionary called prices
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

#function called compute_bill takes one argument, a list called food
def compute_bill(food):
	#initialise variable total to zero
	total = 0
	#for every item in food
	for item in food:
		#if item is available in stock list
		if stock[item] > 0:
			#add priceo of item from prices list to total
			total += prices[item]
			#remove one from item's stock number
			stock[item] -= 1
	#returns total
	return total

#returns 5.5
print compute_bill(shopping_list)
