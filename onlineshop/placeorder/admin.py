# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from placeorder.models import Order, OrderLine

class OrderAdmin(admin.ModelAdmin):
	prepopulated_fields = {}
	list_display = ('firstName','familyName', 'email', 'address', 'zip', 'city', 'created', 'updated','paid')

# Add in this class to customise the Admin Interface
class OrderLineAdmin(admin.ModelAdmin):
	prepopulated_fields = {}
	list_display = ('order', 'product','units','pricePerUnit')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)

# Register your models here.
