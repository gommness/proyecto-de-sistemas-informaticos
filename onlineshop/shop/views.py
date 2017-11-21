# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from models import Category, Product

# Create your views here.

def base(request):
	"""
	Vista para el fichero base.html
	Author: Carlos Li
	"""
	return render(request, 'shop/base.html')

def product_list(request, catSlug=None):	
	"""
	queries that fill category, categories and products
	Author: Carlos Li
	"""
	categories = Category.objects.values()

	if catSlug == None :
		category = None
		products = Product.objects.values()
	else:
		try:
			category=Category.objects.get(catSlug = catSlug)
			products=Product.objects.filter(category = category)
		except Category.DoesNotExist:
			category = None
			products = None
	return render(request,'shop/list.html',
		{'category': category,
		'categories': categories,
		'products': products})

def product_detail(request, id, prodSlug):
	"""
	query that returns a product with id=prodId
	Author: Carlos Li
	"""	
	try:
		product=Product.objects.get(id = id, prodSlug = prodSlug)
	except Product.DoesNotExist:
		print("producto " + " inexistente")
	return render(request, 'shop/detail.html', {'product': product})
