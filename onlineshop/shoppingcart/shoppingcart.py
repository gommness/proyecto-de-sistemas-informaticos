from decimal import Decimal
from shop.models import Product
from shop.exceptions import StockException

class ShoppingCart (object):
	cartKey = 'shoppingCart'
	def __init__(self, request):
		"""
		constructor del carrito
		Author: Carlos Li
		"""
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

	def has(self, product):
		return str(product.id) in self.cart

	def unitsOf(self, product):
		return self.cart[str(product.id)]['units'] if str(product.id) in self.cart else 0

	def isEmpty(self):
		return not self.cart

	def addProduct(self, product, units=1, update_units=False):
		"""
		metodo para meter un producto en el carrito
		Author: Javier Gomez
		"""
		"""
		Add a product to the cart or update its units.
		"""
		#dictionary keys as product.id should be strings,		
		#otherwise they are not serialized properly
		product_id = str(product.id)
		#your code goes here
		#implement two different cases:
		#new product and update of units

		if (units > product.stock) or (product_id in self.cart and update_units == False and units + self.cart[product_id]['units'] > product.stock):
			raise StockException()


		if product_id in self.cart:#caso de que existe
			if update_units == True:
				self.cart[product_id]['units']=units
			else:
				self.cart[product_id]['units']+=units	
		else:
			self.cart[product_id]={
			'units':units,
			'price':str(product.price)
			}


		self.saveCart()

	def saveCart(self):
		"""
		metodo para guardar el carrito
		Author: Carlos Li
		"""
		#update the session cart
		self.session[self.cartKey] = self.cart
		#mark the session as "modified"	 to make sure it is saved
		#By default, Django only saves to the session database
		#when the session has been modified - that is if any of its
		#dictionary values have been assigned or deleted
		#but this will not work for 'units' or 'price' which are values
		#of a dictionary not a new dictionary
		self.session.modified = True

	def removeProduct(self,product):
		"""
		metodo para eliminar un producto del carrito
		Author: Carlos Li
		"""
		"""
		Remove a product from the cart.
		"""
		#your code goes here
		product_id = str(product.id)
		del self.cart[product_id]
		self.session.modified = True



	def __iter__(self):
		"""
		This function allows you to iterate through the shopping cart
		shoppingCart = Shoppingcart(request)
		for i in shoppingCart:
		"""	
		product_ids = self.cart.keys()
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
		metodo obtener el numero de unidades de productos que hay en el carrito
		Author: Javier Gomez
		"""
		"""
		Count all items in the cart. By default it counts the number of 
		different products
		"""
		units = 0
		for prod in self:
			units += prod['units']

		return units


	def get_total_price(self):
		"""
		metodo para obtener el precio total del carrito
		Author: Carlos Li
		"""
		total=0
		for prod in self:
			total += prod['total_price']
		return total


	def clear(self):
		#remove cart from session
		del self.session[self.cartKey]
		self.session.modified = True
		