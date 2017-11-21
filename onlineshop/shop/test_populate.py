#Para ejecutar los tests hay que ejecutar en SQLITE
#export SQLITE=1
#python database_cleaner.py
#python manage.py migrate
#python create_super_user.py
#
#python ./manage.py test shop.test_populate.viewsTests --keepdb

# Uncomment if you want to run tests in transaction mode with a final rollback
#from django.test import TestCase
#uncomment this if you want to keep data after running tests
from unittest import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from shop.models import Product, Category

import os
from populate_onlineshop import populate
base_path   = os.getcwd()
static_path = os.path.join(base_path,"static")


#python ./manage.py test shop.test_populate.viewsTests --keepdb

DEBUG = False
from PIL import Image
from StringIO import StringIO
from django.core.files.base import File


class viewsTests(TestCase):
    """
    Llama a populate_onlineshop.py para poblar la base de datos
    y comprueba que ha sido correcto
    Author: Javier Gomez
    """
    def setUp(self):
        self._client = Client()
        self.clean_database()
        populate()

    @staticmethod
    def get_image_file(name='pf.jpg', ext='jpg', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def clean_database(self):
        Product.objects.all().delete()
        Category.objects.all().delete()


    def test_produnct_list(self):
        categories = Category.objects.all()
        products = Product.objects.all()
        response = self._client.get(reverse('product_list'), follow=True)
        for counter in categories:
            self.assertIn(b'%s'%counter.catName, response.content)
        for counterProd in products:
            self.assertIn(b'%s'%counterProd.image, response.content)

    def test_produnct_list_cat_0(self):
        response = self._client.get(reverse('product_list_by_category',
                                            kwargs={'catSlug':'eau-de-parfum'}), follow=True)
        prodNameList = ["Onett", "Twoson", "Threed", "Fourside", "Summers", "Winters"]#lista de nombre de productos que deberian estar en la cat eau-de-parfums
        categories = Category.objects.all()
        productos = Product.objects.all()
        for counter in categories:
            self.assertIn(b'%s' % counter.catName, response.content)
        for counterProd in productos:
            if counterProd.prodName in prodNameList:
                self.assertIn(b"%s" % counterProd.prodName, response.content)
        for counterCat in categories:
            for counterProd in productos:
                if counterProd.category == counterCat and counterCat.catSlug != "eau-de-parfum":
                    self.assertNotIn(b"%s" % counterProd.prodName, response.content)

    def test_product_detail_fileName_0_0(self):
        prodName='Onett'
        p = Product.objects.get(prodName = prodName)
        notP = Product.objects.get(prodName = "Phantom Blood")
        response = self._client.get(reverse('product_detail',
                                            kwargs={'id':p.id,
                                                    'prodSlug':p.prodSlug}), follow=True)
        self.assertIn   (b'%s'%p.category.catName, response.content)
        self.assertNotIn(b'Eau de Cologne', response.content)

        self.assertIn(b'%s'%p.description, response.content)
        self.assertNotIn(b'%s'%notP.description, response.content)