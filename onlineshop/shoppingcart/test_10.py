from unittest import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from shop.models import Product, Category
from shoppingcart import ShoppingCart
from PIL import Image
from StringIO import StringIO
from django.core.files.base import File

from decimal import Decimal

from views import shoppingcart_list
from forms import CartAddProductForm

DEBUG = False


class shoppingCartTest_10(TestCase):
    """
    clase de test
    Author: Javier Gomez
    """
    def setUp(self):
        self._client   = Client()
        # self.clean_database()
        # self.populate_data_base()

    # def clean_database(self):
    #     Product.objects.all().delete()
    #     Category.objects.all().delete()

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def add_cat(self, name):
        c = Category.objects.get_or_create(catName=name)[0]
        return c

    def add_product(self,cat, name, description, price, stock):
        from django.core.files import File
        products = Product.objects.filter(prodName=name)
        if products.exists():
            p = products[0]
            p.delete()
        p = Product.objects.get_or_create(category=cat,
                                          prodName=name,
                                          description=description,
                                          price=price,
                                          stock=stock,
                                          image=self.get_image_file())[0]

        return p

    def test(self):
        """
        funcion para realizar el test
        Author: Javier Gomez
        """
    	price = 1.1
        stock = 10
        units1 = 1
        units5 = 5
        cat      = self.add_cat("cat_1")
        prod     = self.add_product(cat, "prod", "descript", price, stock)

        response = self._client.get(reverse('product_list'))
        request = response.wsgi_request

        #create shopping cart
        _shoppingcart =  ShoppingCart(request)
        _shoppingcart.addProduct(prod,units=units1)
        _price    = request.session[_shoppingcart.cartKey][str(prod.id)]['price']
        _units = request.session[_shoppingcart.cartKey][str(prod.id)]['units']

        cart = request.session.get('shoppingCart')
        self.assertEquals(_shoppingcart.cart, cart)
        _shoppingcart.clear()
        self.assertFalse('shoppingCart' in request.session)

