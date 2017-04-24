from tastypie.resources import ModelResource
from .models import Category, Product
from tastypie import fields


class CategoryResource(ModelResource):

	class Meta:
		queryset = Category.objects.all()
		resource_name = 'category'
		excludes = ['id']


class ProductResource(ModelResource):
	category_cod = fields.IntegerField(attribute='category__cod')

	class Meta:
		queryset = Product.objects.all()
		resource_name = 'product'
		excludes = ['id', 'image']