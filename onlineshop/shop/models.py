# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.db import models
from django.utils.timezone import now

maxLen = 128;

# Create your models here.

class Category(models.Model):
	"""
	Modelo de Category
	Author: Carlos Li
	"""
	maxLen = 128;
	catName = models.CharField(max_length=maxLen, null=False, unique=True)
	catSlug = models.SlugField(max_length=maxLen, blank=True,unique=True) #blank=True creemos que no es necesario (?)
	#README hay que ver si catSlug tiene que ser hidden para el admin (?)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self): # For Python 2, use __unicode__ too
		return self.catName

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.catName

	def save(self, *args, **kwargs):
		self.catSlug = slugify(self.catName)
		super(Category, self).save(*args, **kwargs)

class Product(models.Model):
	"""
	Modelo de Product
	Author: Javier Gomez
	"""

	maxLen = 128;
	category = models.ForeignKey(Category, null=False)
	prodName = models.CharField(max_length=maxLen, null=False,unique=True)
	prodSlug = models.SlugField(max_length=maxLen, null=False,unique=True,blank=True) #blank=True creemos que no es necesario (?)
	image = models.ImageField(null=False,upload_to='images/products')#probablemente haya que modificar el parametro upload_to
	description = models.CharField(max_length=maxLen, null=False)
	price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
	stock = models.IntegerField(null=False, default=1)
	availability = models.BooleanField(null=False,default=True)
	created = models.DateTimeField(default=now)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.prodName

	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.prodName

	def save(self, *args, **kwargs):
		self.prodSlug = slugify(self.prodName)
		super(Product, self).save(*args, **kwargs)