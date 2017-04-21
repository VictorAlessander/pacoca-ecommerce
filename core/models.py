from django.db import models


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