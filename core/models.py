from django.db import models
from django.utils import timezone


class Category(models.Model):

	name = models.CharField(max_length=30)
	description = models.TextField()

	def __str__(self):
		return self.name


class Product(models.Model):

	cod = models.IntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.name


class Cart(models.Model):

	cod = models.PositiveIntegerField()
	name = models.CharField(max_length=150)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	quantity = models.PositiveIntegerField(default=1)
	date = models.DateTimeField(null=True, blank=True)

	def save_order(self):
		owner = models.ForeignKey('auth.User')
		self.date = timezone.now()
		self.save()