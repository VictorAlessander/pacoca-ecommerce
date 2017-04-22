from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Category, Product, Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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


@login_required
def add_to_cart(request, item_cod):

	item = get_object_or_404(Product, cod=item_cod)

	if Cart.objects.filter(name=item.name).exists():
		increase_item = Cart.objects.get(cod=item_cod, name=item.name)
		increase_item.quantity = increase_item.quantity + 1
		increase_item.save()

	else:
		add = Cart.objects.create(
			cod=item.cod,
			name=item.name,
			price=item.price,
			)

	return redirect('core:checkout')


@login_required
def checkout(request):

	item_list = Cart.objects.all()

	return render(request, 'checkout.html', {'item_list': item_list})