from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.Index.as_view()),
	url(r'^categories/', views.category_list, name='category_list'),
	url(r'^products/(?P<category>\w+)/', views.product_list, name='product_list'),
]