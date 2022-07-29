from random import choices
from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import make_password


class UserManager(auth_models.BaseUserManager):
    def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str = None,
        is_staff=False,
        is_superuser=False,
    ) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        buyer = 'buyer'
        seller = 'seller'
        typ = [
            (buyer, 'buyer'),
            (seller,'seller'),
        ]
        user_type = models.CharField(max_length=100,blank=False, choices=typ, default=buyer)
        user.save()

        return user

    def create_superuser(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
  
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    USER_CHOICES =(
        ('buyer', 'BUYER'),
        ('seller','SELLER')
    )
    user_type = models.CharField(verbose_name="USER_TYPE", max_length=10, choices = USER_CHOICES)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]

    
    objects = UserManager()
     
   