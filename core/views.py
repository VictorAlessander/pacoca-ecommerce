from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Product
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
	template_name = 'index.html'


@login_required
def category_list(request):

	categories = Category.objects.all()

	return render(request, 'categories.html', {'categories': categories})


@login_required
def product_list(request, category):

	products = Product.objects.filter(category__name=category)

	return render(request, 'products.html', {'products': products})