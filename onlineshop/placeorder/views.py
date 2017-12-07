# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from placeorder.forms import OrderCreateForm
from shoppingcart.shoppingcart import ShoppingCart
from placeorder.models import Order, OrderLine

# Create your views here.
def createOrder(request):
	form = OrderCreateForm()
	_shoppingcart = ShoppingCart(request)
	return render(request,'placeorder/createOrder.html',
		{'shoppingcart': _shoppingcart,
		'form' : form})

def confirmOrder(request):
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			firstName = form.cleaned_data['firstName']
			familyName = form.cleaned_data['familyName']
			email = form.cleaned_data['email']
			address = form.cleaned_data['address']
			zip = form.cleaned_data['zip']
			city = form.cleaned_data['city']
		else: print(form.errors)
	else:
		print(form.errors)
	order = Order.create(firstName, familyName, email, address, zip, city, True)
	shoppingcart=ShoppingCart(request)
	if len(shoppingcart) <= 0:
		return redirect('product_list')
	for prod in shoppingcart:
		product = prod["product"]
		units = prod["units"]
		pricePerUnit = prod["price"]
		OrderLine.create(order, product, units, pricePerUnit)
	shoppingcart.clear()
	return render(request, "placeorder/confirmOrder.html",{"orderid" : order.id})
	#TODO
	#comprobar que el order esta bien//DONE
	#crea una variable de tipo Order//done
	#tantas variables de tipo OrderLine como productos haya en el carrito//done
	#inicializa dichas variables con datos del carrito y del formulario con el que se ha llegado aqui (?)//done
	#hace save de ambas//done
	#limpia carrito
	#render confirmOrder.html