from django.db import models
from user.models import User
from my_cart.models import Cart
from My_Addresses.models import Address
# Create your models here.


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Address, on_delete=models.CASCADE)
    # amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    PAYMENT_CHOICES = (
        ('upi', 'upi'),
        ('credit/debit/ATM Card', 'credit/debit/ATM Card'),
        ('net banking', 'netbanking'),
        ('cash on delivery', 'cash on delivery')
    )
    payment_options = models.CharField(max_length=30, choices=PAYMENT_CHOICES)


class OrderedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)


def __str__(self):
    return str(self.shipping)
