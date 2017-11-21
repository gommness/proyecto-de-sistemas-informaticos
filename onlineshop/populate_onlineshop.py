import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','onlineshop.settings')
import django
django.setup()
from shop.models import Category, Product
from random import randint
from django.core.files import File
from onlineshop.settings import MEDIA_ROOT
PRODUCT_IMAGES = os.path.join(os.path.join(MEDIA_ROOT, 'images'), 'products')

"""
from django.core.files import File
imageObject = File(open(os.path.join(directory_with_images, image_name),'r'))
p = Product.objects.get_or_create(category = ...,
prodName = ...,
...)[0]
p.image.save(image_name, imageObject, save = True)
"""

def populate():
	"""
    Inserta categorias y productos en el proyecto
    Author: Javier Gomez
    """
	# First, we will create lists of dictionaries containing the pages
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.
	cologne_products = [
	{"prodName":"Phantom Blood", "image":"pf.jpg", "description":"scent of inmortal vamipe lord", "price":1, "stock":10, "availability":1},
	{"prodName":"Battle Tendency", "image":"pf.jpg", "description":"the feel of determination's power", "price":2, "stock":10, "availability":1},
	{"prodName":"Stardust Crusaders", "image":"pf.jpg", "description":"the arome of Egypt", "price":3, "stock":10, "availability":1},
	{"prodName":"Diamond Is Unbreakable", "image":"pf.jpg", "description":"fragance of a crazy, noisy, bizarre town", "price":4, "stock":10, "availability":1},
	{"prodName":"Vento Aureo", "image":"pf.jpg", "description":"smell of italian elegance", "price":5, "stock":10, "availability":1},
	{"prodName":"Stone Ocean", "image":"pf.jpg", "description":"fragance of satisfactory revenge", "price":6, "stock":10, "availability":1}
	]

	parfum_products = [
	{"prodName":"Onett", "image":"pf.jpg", "description":"fragance of adventure", "price":3., "stock":10, "availability":1},
	{"prodName":"Twoson", "image":"pf.jpg", "description":"feel of Autum", "price":3., "stock":10, "availability":1},
	{"prodName":"Threed", "image":"pf.jpg", "description":"Groovy Halloween-like", "price":3., "stock":10, "availability":1},
	{"prodName":"Fourside", "image":"pf.jpg", "description":"elegant city-men feel", "price":3., "stock":10, "availability":1},
	{"prodName":"Winters", "image":"pf.jpg", "description":"cold as the peak of a mountain", "price":3., "stock":10, "availability":1},
	{"prodName":"Summers", "image":"pf.jpg", "description":"relaxing as holidays on a beach", "price":3., "stock":10, "availability":1} ]

	toilette_products = [
	{"prodName":"Symetra", "image":"pf.jpg", "description":"fragance of order", "price":1., "stock":10, "availability":1},
	{"prodName":"Ana", "image":"pf.jpg", "description":"feel of home", "price":1., "stock":10, "availability":1},
	{"prodName":"Mercy", "image":"pf.jpg", "description":"god complex fragance", "price":1., "stock":10, "availability":1},
	{"prodName":"Zarya", "image":"pf.jpg", "description":"strong as the mountain", "price":1., "stock":10, "availability":1},
	{"prodName":"Mei", "image":"pf.jpg", "description":"freezing", "price":1., "stock":10, "availability":1},
	{"prodName":"Phara", "image":"pf.jpg", "description":"justice rains from above", "price":1., "stock":10, "availability":1} ]


	cats = {"Eau de Cologne": {"products":cologne_products},
	"Eau de Parfum": {"products":parfum_products},
	"Eau de Toilette": {"products":toilette_products} }
	# If you want to add more catergories or pages,
	#add them to the dictionaries above.
	#The code below goes through the cats dictionary, then adds each category,
	#and then adds all the associated pages for that category.
	#if you are using Python 2.x then use cats.iteritems() see
	#http://docs.quantifiedcode.com/python-anti-patterns/readability/
	#for more information about how to iterate over a dictionary properly.
	for cat, cat_data in cats.items():
		c = add_category(cat)
		for p in cat_data["products"]:
			add_product(c, p["prodName"], p["image"],p["description"],p["price"],p["stock"],p["availability"])
	# Print out the categories we have added.
	for c in Category.objects.all():
		for p in Product.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_product(category, prodName, image, description, price, stock, availability):
	p = Product.objects.get_or_create(category=category, prodName=prodName, price=price, description=description)[0]
	imageObject = File(open(os.path.join(PRODUCT_IMAGES, image),'r'))
	p.image =imageObject
	p.stock=stock
	p.availability = availability
	p.image.save(image, imageObject, save = True)
	p.save()
	return p

def add_category(name):
	c = Category.objects.get_or_create(catName=name)[0]
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print("Starting Shop population script...")
	populate()