# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shop.models import Product
from django.utils.timezone import now

# Create your models here.

class Order(models.Model):
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
		total = 0
		collection = self.orderLines.all()
		for order in collection:
			total += order.getProductCost()
		return total

	def __str__(self): # For Python 2, use __unicode__ too
		return self.firstName+" "+self.familyName+" ("+self.email+") "+" @ "+self.address+" ("+self.zip+" "+self.city+") STATUS: "+self.paid

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.__str__()

	def save(self, *args, **kwargs):
		super(Order, self).save(*args, **kwargs)



class OrderLine(models.Model):
	order = models.ForeignKey(Order, null=False, related_name='orderLines')
	product = models.ForeignKey(Product, null=False, related_name='productLines')
	units = models.IntegerField(null=False)#ponerle minimo?
	pricePerUnit = models.DecimalField(max_digits=10 ,decimal_places=2)

	def __str__(self):
		return "product: "+self.product+" order: "+self.order + " units: " +self.units+" price: "+self.pricePerUnit

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.__str__()

	def getProductCost(self):
		return self.units * self.pricePerUnit

	def save(self, *args, **kwargs):
		super(OrderLine, self).save(*args, **kwargs)