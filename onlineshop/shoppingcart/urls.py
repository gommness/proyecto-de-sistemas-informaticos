from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.shoppingcart_list, name="shoppingcart_list"),
	url(r'^list/$', views.shoppingcart_list, name="shoppingcart_list"),
	url(r'^add/(?P<product_id>\d+)/$', views.shoppingcart_add, name = "shoppingcart_add"),
	url(r'^remove/(?P<product_id>\d+)/$', views.shoppingcart_remove, name = "shoppingcart_remove"),
	]