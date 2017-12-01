# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shoppingcart import ShoppingCart
from forms import CartAddProductForm
from shop.models import Product

# Create your views here.
def shoppingcart_list(request):
	form = CartAddProductForm()
	_shoppingcart = ShoppingCart(request)
	return render(request,'shoppingcart/list.html',
		{'shoppingcart': _shoppingcart,
		'form' : form})

def shoppingcart_add(request,product_id):
	try:
		product = Product.objects.get(id=product_id)
	except ObjectDoesNotExist:
		return redirect('product_list')

	shoppingcart=ShoppingCart(request)
	form = CartAddProductForm()
	if request.method == 'POST':
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			units = form.cleaned_data['units']
			update = form.cleaned_data['update']
		else: print(form.errors)
	else:
		print(form.errors)

	#your code goes here
	#process the form to get units, update_quantity
	#use product_id to get the product
	shoppingcart.addProduct(product=product,
		units=units,
		update_units=update)
	return redirect('shoppingcart_list')

def shoppingcart_remove(request,product_id):
	try:
		product = Product.objects.get(id=int(product_id))
	except ObjectDoesNotExist:
		return redirect('product_list')
	shoppingcart=ShoppingCart(request)
	shoppingcart.removeProduct(product)

	return redirect('shoppingcart_list')	