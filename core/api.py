from tastypie.resources import ModelResource
from .models import Category, Product
from tastypie import fields


class CategoryResource(ModelResource):

	class Meta:
		queryset = Category.objects.all()
		resource_name = 'category'


class ProductResource(ModelResource):
	category = fields.CharField(attribute="category")

	class Meta:
		queryset = Product.objects.all()
		resource_name = 'product'
		excludes = ['id']