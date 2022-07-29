from unittest.util import _MAX_LENGTH
from django.db import models
from user.models import User


# Create your models here.

"""
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
"""


class Product(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=35)

    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name
