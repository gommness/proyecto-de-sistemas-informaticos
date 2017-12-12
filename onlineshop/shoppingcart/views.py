# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shoppingcart import ShoppingCart
from forms import CartAddProductForm
from shop.models import Product

# Create your views here.
def shoppingcart_list(request):
	"""
	Vista para el fichero list.html que muestra los contenidos el carrito de la compra
	Author: Carlos Li
	"""
	form = CartAddProductForm()
	_shoppingcart = ShoppingCart(request)
	return render(request,'shoppingcart/list.html',
		{'shoppingcart': _shoppingcart,
		'form' : form})

def shoppingcart_add(request,product_id):
	"""
	vista para procesar un formulario para meter un producto en el carrito de la compra
	Author: Javier Gomez
	"""
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
			if product.stock < units:
				return render(request, "shop/error.html", {'error' : "not enough stock left", 'product' : product})
		else: print(form.errors)
	else:
		print(form.errors)

	shoppingcart.addProduct(product=product,
		units=units,
		update_units=update)
	return redirect('shoppingcart_list')

def shoppingcart_remove(request,product_id):
	"""
	Vista para procesar un formulario para eliminar un producto del carrito de la compra
	Author: Carlos Li
	"""
	try:
		product = Product.objects.get(id=int(product_id))
	except ObjectDoesNotExist:
		return redirect('product_list')
	shoppingcart=ShoppingCart(request)
	shoppingcart.removeProduct(product)

	return redirect('shoppingcart_list')	