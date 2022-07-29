from django.db import models

from user.models import User
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="NAME", max_length=25)
    phone_no = models.CharField(max_length=12)
    pincode = models.CharField(verbose_name="PINCODE", max_length=6 )
    state = models.CharField(verbose_name="STATE", max_length=6 )
    city = models.CharField(verbose_name="CITY", max_length=20 )
    house_no =models.CharField(max_length=50)
    street_name =models.CharField(max_length=50)

    

    def __str__(self):
        return f"{self.name}"

