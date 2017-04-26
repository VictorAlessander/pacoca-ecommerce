from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^$', views.Index.as_view(), name='index'),
	url(r'^categories/$', views.category_list, name='category_list'),
	url(r'^products/(?P<category>\w+)/$', views.product_list, name='product_list'),
	url(r'^add/(?P<item_cod>\d+)/$', views.add_to_cart, name='add_to_cart'),
	url(r'^increment/(?P<item_cod>\d+)/$', views.increment_item, name='increment_item'),
	url(r'^remove/(?P<item_cod>\d+)/$', views.remove_of_cart, name='remove_of_cart'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^checkout/$', views.checkout, name='checkout'),
	url(r'^submit/$', views.submit_order, name='submit_order'),
	url(r'^order-list/$', views.order_list, name='order_list'),
]