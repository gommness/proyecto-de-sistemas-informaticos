from django.conf.urls import url
from shoppingcart import views
urlpatterns = [
	url(r'^add/(?P<product_id>\d+)/$', views.shoppingcart_add, name = "shoppingcart_add"),
	url(r'^remove/(?P<product_id>\d+)/$', views.shoppingcart_remove, name = "shoppingcart_remove"),
	]