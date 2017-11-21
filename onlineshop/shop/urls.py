from django.conf.urls import url
from shop import views

urlpatterns = [
	url(r'^$', views.product_list, name = "product_list"),
	url(r'^(?P<catSlug>[-\w]+)/$', views.product_list, name = "product_list_by_category"),
	url(r'^(?P<id>\d+)/(?P<prodSlug>[-\w]+)/$', views.product_detail, name = "product_detail"),
]