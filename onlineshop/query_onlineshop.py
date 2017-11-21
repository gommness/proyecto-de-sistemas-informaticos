import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','onlineshop.settings')
import django
django.setup()
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Category, Product
from django.core.files import File
from onlineshop.settings import MEDIA_ROOT

PRODUCT_IMAGES = os.path.join(os.path.join(MEDIA_ROOT, 'images'), 'products')

# Start execution here!
if __name__ == '__main__':
	print("Starting Shop query script...")
	categoriaOferta = Category.objects.get_or_create(catName="ofertas")[0]
	categoriaGanga = Category.objects.get_or_create(catName="gangas")[0]

	#obtenemos o creamos los productos de categoria oferta
	try:
		oferta1 = Product.objects.get(category=categoriaOferta, prodName="oferta 1")
	except ObjectDoesNotExist:
		try:
			oferta1 = Product.objects.create(category=categoriaOferta, prodName="oferta 1",image=os.path.join(PRODUCT_IMAGES,"oferta-1"),description="es la oferta 1",price=1)
		except IntegrityError:
			print("unable to create oferta1")

	try:
		oferta2 = Product.objects.get(category=categoriaOferta, prodName="oferta 2")
	except ObjectDoesNotExist:
		try:
			oferta2 = Product.objects.create(category=categoriaOferta, prodName="oferta 2",image=os.path.join(PRODUCT_IMAGES,"oferta-2"),description="es la oferta 2",price=1)
		except IntegrityError:
			print("unable to create oferta2")

	try:
		oferta3 = Product.objects.get(category=categoriaOferta, prodName="oferta 3")
	except ObjectDoesNotExist:
		try:
			oferta3 = Product.objects.create(category=categoriaOferta, prodName="oferta 3",image=os.path.join(PRODUCT_IMAGES,"oferta-3"),description="es la oferta 3",price=1)
		except IntegrityError:
			print("unable to create oferta3")

	#obtenemos o creamos los productos de categoria ganga
	try:
		ganga1 = Product.objects.get(category=categoriaGanga, prodName="ganga 1")
	except ObjectDoesNotExist:
		try:
			ganga1 = Product.objects.create(category=categoriaGanga, prodName="ganga 1",image=os.path.join(PRODUCT_IMAGES,"ganga-1"),description="es la ganga 1",price=1)
		except IntegrityError:
			print("unable to create ganga1")

	try:
		ganga2 = Product.objects.get(category=categoriaGanga, prodName="ganga 2")
	except ObjectDoesNotExist:
		try:
			ganga2 = Product.objects.create(category=categoriaGanga, prodName="ganga 2",image=os.path.join(PRODUCT_IMAGES,"ganga-2"),description="es la ganga 2",price=1)
		except IntegrityError:
			print("unable to create ganga2")

	try:
		ganga3 = Product.objects.get(category=categoriaGanga, prodName="ganga 3")
	except ObjectDoesNotExist:
		try:
			ganga3 = Product.objects.create(category=categoriaGanga, prodName="ganga 3",image=os.path.join(PRODUCT_IMAGES,"ganga-3"),description="es la ganga 3",price=1)
		except IntegrityError:
			print("unable to create ganga3")

	#fin del bloque de creacion de objetos
	#realizamos una consulta de todos los productos asociados a la categoria gangas
	print("--------query1--------")
	query1 = Product.objects.filter(category=categoriaGanga)
	for element in query1:
		print("{0} ".format(str(element)))

	#realizamos una consulta de las categorias cuyos productos tienen asociado el slug "oferta-1"
	print("--------query2--------")
	try:
		query2 = Product.objects.get(prodSlug="oferta-1").category.catSlug
		print(query2)
	except ObjectDoesNotExist:
		print("no existe un objeto con prodSlug ''oferta1''")

	#realizamos una consulta de las categorias cuyos productos tienen asociado el slug "oferta_10"
	print("--------query3--------")
	try:
		query3 = Product.objects.get(prodSlug="oferta_10").category.catSlug
		print(query3)
	except ObjectDoesNotExist:
		print("producto " + "oferta_10" + " inexistente")

