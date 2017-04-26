from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.conf import settings


class Category(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Product(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to='core', null=True, blank=True)

	def __str__(self):
		return self.name


class MCart(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	quantity = models.PositiveIntegerField(default=1)

	def total(self):
		aggregate_queryset = MCart.objects.all().aggregate(
			total_price=Sum(models.F('price') * models.F('quantity'), 
				output_field=models.DecimalField(decimal_places=2, max_digits=8)
				)
			)

		return aggregate_queryset['total_price']


class Order(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	quantity = models.PositiveIntegerField(default=1)
	date = models.DateTimeField(blank=True, null=True)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário')
	order_id = models.CharField(max_length=40)

	def save_order(self):
		self.date = timezone.now()
		self.save()

	def total(self, session, user):
		aggregate_queryset = Order.objects.filter(order_id=session, owner=user).aggregate(
			total_price=Sum(models.F('price') * models.F('quantity'),
				output_field=models.DecimalField(decimal_places=2, max_digits=8)
				)
			)

		return aggregate_queryset['total_price']