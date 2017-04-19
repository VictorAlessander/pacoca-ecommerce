from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Product

class Index(TemplateView):
	template_name = 'index.html'


def category_list(request):

	categories = Category.objects.all()

	return render(request, 'categories.html', {'categories': categories})


def product_list(request, category):

	products = Product.objects.filter(category__name=category)

	return render(request, 'products.html', {'products': products})