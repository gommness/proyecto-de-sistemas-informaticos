# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def shoppingcart_list(request):
	_shoppingcart = shoppingCart(request)
	return render(request,'shoppingcart/list.html',
		{'shoppingcart': _shoppingcart})

def shoppingcart_add(request,product_id):
	shoppingcart=ShoppingCart(request)
	#your code goes here
	#process the form to get units, update_quantity
	#use product_id to get the product
	shoppingcart.addProduct(product=product,
		units=units,
		update_quantity=update_units)

def shoppingcart_remove(request,product_id):
	#your code goes here
	return redirect('shoppingcart_list')	