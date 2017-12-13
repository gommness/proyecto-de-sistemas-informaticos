# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shop.models import Product
from django.utils.timezone import now

# Create your models here.

class Order(models.Model):
	"""
	el modelo de un order
	Author: Javier Gomez
	"""
	maxLen = 128
	firstName = models.CharField(max_length=maxLen, null=False)
	familyName = models.CharField(max_length=maxLen, null=False)
	email = models.EmailField(max_length=maxLen, null=False)
	address = models.CharField(max_length=maxLen, null=False)
	zip = models.CharField(max_length=maxLen, null=False)
	city = models.CharField(max_length=maxLen, null=False)
	created = models.DateTimeField(default=now)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False) #not null (?)

	def getTotalCost(self):
		"""
		metodo para obtener el precio total de un order
		Author: Carlos Li
		"""
		total = 0
		collection = self.orderLines.all()
		for order in collection:
			total += order.getProductCost()
		return total

	@classmethod
	def create(cls, firstName, familyName, email, address, zip, city, paid):
		"""
		metodo estatico para crear un order a partir de los datos introducidos
		Author: Javier Gomez
		"""
		order = cls()
		order.firstName = firstName
		order.familyName = familyName
		order.email = email
		order.address = address
		order.zip = zip
		order.city = city
		order.paid = paid
		order.save()
		return order

	def __str__(self): # For Python 2, use __unicode__ too
		return ""+str(self.firstName)+" "+str(self.familyName)+" ("+str(self.email)+") "+" STATUS: "+str(self.paid)

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.__str__()

	def save(self, *args, **kwargs):
		super(Order, self).save(*args, **kwargs)



class OrderLine(models.Model):
	"""
	clase que representa un producto dentro de un pedido
	Author: Carlos Li
	"""
	order = models.ForeignKey(Order, null=False, related_name='orderLines')
	product = models.ForeignKey(Product, null=False, related_name='productLines')
	units = models.IntegerField(null=False)#ponerle minimo?
	pricePerUnit = models.DecimalField(max_digits=10 ,decimal_places=2)

	def __str__(self):
		return "product: "+str(self.product)+" order: "+str(self.order.id) + " units: " +str(self.units)+" price: "+str(self.pricePerUnit)

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.__str__()

	@classmethod
	def create(cls, order, product, units, pricePerUnit):
		"""
		metodo para crear un producto perteneciente a un pedido
		Author: Javier Gomez
		"""
		orderLine = cls()
		orderLine.order = order
		orderLine.product = product
		orderLine.units = units
		orderLine.pricePerUnit = pricePerUnit
		orderLine.save()
		return orderLine

	def getProductCost(self):
		"""
		metodo para obtener el coste del producto
		Author: Carlos Li
		"""
		return self.units * self.pricePerUnit

	def save(self, *args, **kwargs):
		super(OrderLine, self).save(*args, **kwargs)