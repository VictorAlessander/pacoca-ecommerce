from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Category(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=30)
	description = models.TextField()

	def __str__(self):
		return self.name


class Product(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.name


class MCart(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	quantity = models.PositiveIntegerField(default=1)
	date = models.DateTimeField(null=True, blank=True)

	def total(self):
		aggregate_queryset = MCart.objects.all().aggregate(
			total_price=Sum(models.F('price') * models.F('quantity'), 
				output_field=models.DecimalField(decimal_places=2, max_digits=8)
				)
			)

		return aggregate_queryset['total_price']

	#def save_order(self):
		#owner = models.ForeignKey('auth.User')
		#self.date = timezone.now()
		#self.save()