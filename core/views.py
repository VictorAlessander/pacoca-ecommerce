from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Category, Product, MCart
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

	if MCart.objects.filter(name=item.name).exists():
		increase_item = MCart.objects.get(cod=item_cod, name=item.name)
		increase_item.quantity = increase_item.quantity + 1
		increase_item.save()

	else:
		add = MCart.objects.create(
			cod=item.cod,
			name=item.name,
			price=item.price,
			)

	return redirect('core:cart')


@login_required
def cart(request):

	item_list = MCart.objects.all()
	total_price = MCart()
	total_price = total_price.total()

	return render(request, 'cart.html', {'item_list': item_list, 'total_price': total_price})