#class called ShoppingCart
class ShoppingCart(object):
	"""Creates shopping cart objects
	for users of our fine website."""
	
	#__init__() method
	def __init__(self, customer_name):
		#initialises customer's name
		self.customer_name = customer_name
		#initialises empty dictionary
		self.items_in_cart = {}
	
	#add_item() method
	def add_item(self, product, price):
		"""Add product to the cart."""
		if product not in self.items_in_cart:
			self.items_in_cart[product] = price
			print product + "added."
		else:
			print product + " is already in the cart."
	
	#remove_item() method
	def remove_item(self, product):
		"""Remove product from the cart."""
		if produce in self.items_in_cart:
			del self.items_in_cart[product]
			print product + " removed."
		else:
			print product + " is not in the cart."

my_cart = ShoppingCart("Anneka")
my_cart.add_item("Bananas", 19)
