# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from placeorder.forms import OrderCreateForm
from shoppingcart.shoppingcart import ShoppingCart

# Create your views here.
def createOrder(request):
	form = OrderCreateForm()
	_shoppingcart = ShoppingCart(request)
	return render(request,'placeorder/createOrder.html',
		{'shoppingcart': _shoppingcart,
		'form' : form})

#def confirmOrder(request):
	#TODO
	#comprobar que el order esta bien
	#crea una variable de tipo Order
	#tantas variables de tipo OrderLine como productos haya en el carrito
	#inicializa dichas variables con datos del carrito y del formulario con el que se ha llegado aqui (?)
	#hace save de ambas
	#limpia carrito
	#render confirmOrder.html