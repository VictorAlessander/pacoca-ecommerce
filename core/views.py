from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category

class Index(TemplateView):
	template_name = 'index.html'


def category_list(request):

	categories = Category.objects.all()

	return render(request, 'categories.html', {'categories': categories})