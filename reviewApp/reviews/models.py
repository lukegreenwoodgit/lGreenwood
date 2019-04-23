from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(default = '', max_length = 255)
	brand = models.CharField(default = '', max_length = 255)
	avg_cost = models.DecimalField(default = 00.00, max_digits = 4, decimal_places = 2)
	category = models.ForeginKey(Category, on_delete = models.CASCADE)
	date_released = models.DateField(default = timezone.now)
	description = models.TextField()
	photo = models.ImageField(default = 'default.jpg', upload_to = 'product_pics')

class Category(models.Model):
	name = models.CharField(default = '', max_length = 255)
	description = models.TextField()

class Review(models.Model):
	author = models.ForeginKey(User, on_delete = models.CASCADE)
	product = models.ForeginKey(Product, on_delete = models.CASCADE)
	review_text = models.TextField()
	date = models.DateField(default = timezone.now)
