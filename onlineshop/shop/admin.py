# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop.models import Category, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'prodSlug':('prodName',)}
	list_display = ('prodName','prodSlug', 'price', 'stock', 'availability', 'created', 'updated')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'catSlug':('catName',)}
	list_display = ('catName', 'catSlug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)