from decimal import Decimal
from shop.models import Product

class ShoppingCart (object):
	cartKey = 'shoppingCart'
	def __init__(self, request):
		"""
		Initialize the cart:
			if request.session['self.cartKey'] does not exist, create one
			Important: Make a copy of request.session['self.cartKey']
				do not manipulate it directly
				request.session is not a proper dictionary and
				direct manipulation will produce weird results
		"""
		self.session = request.session
		cart = self.session.get(self.cartKey)
		if not cart:
			#save an empty cart in session
			cart = self.session[self.cartKey] = {}
		self.cart = cart
	def addProduct(self, product, units=1, update_units=False):
		"""
		Add a product to the cart or update its units.
		"""
		#dictionary keys as product.id should be strings,		
		#otherwise they are not serialized properly
		product_id = str(product.id)
		#your code goes here
		#implement two different cases:
		#new product and update of units
		self.saveCart()

	def saveCart(self):
		#update the session cart
		self.session[self.cartKey] = self.cart
		#mark the session as "modified"	 to make sure it is saved
		#By default, Django only saves to the session database
		#when the session has been modified - that is if any of its
		#dictionary values have been assigned or deleted
		#but this will not work for 'units' or 'price' which are values
		#of a dictionary not a new dictionary
		self,session.modified = True

	def removeProduct(self,product):
		"""
		Remove a product from the cart.
		"""
		#your code goes here
		

	def __iter__(self):
		"""
		This function allows you to iterate through the shopping cart
		shoppingCart = Shoppingcart(request)
		for i in shoppingCart:
		"""	
		products_ids = self.cart.keys()
		#get the product objects and add them to the cart
		#products themselves will not be stored in the session variable
		#so we need to recreate them each time
		#We can not store the Product in the session variable because 
		#classes with pointers to object are not properly
		#serialized
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product']=product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['units']
			yield item

	def __len__(self):
		"""
		Count all items in the cart. By default it counts the number of 
		different products
		"""		 	
		return #your code goes here


	def get_total_price(self):
		return #your code goes here


	def clear(self):
		#remove cart from session
		del self.session[self.cartKey]
		self.session.modified = True
		