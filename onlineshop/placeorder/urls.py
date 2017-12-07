from django.conf.urls import url
from placeorder import views

urlpatterns = [
	url(r'^create_order/$', views.createOrder, name="create_order"),
	url(r'^confirm_order/$', views.confirmOrder, name="confirm_order")#README wtf
	]