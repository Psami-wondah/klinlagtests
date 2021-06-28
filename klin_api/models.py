from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    is_giver = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, verbose_name=None)
    last_name = models.CharField(max_length=50, verbose_name=None)
    phone = PhoneNumberField(null=False, blank=False,  unique=True, verbose_name=None)
    email = models.EmailField(max_length=254,  unique=True, verbose_name=None)
    location = models.CharField(max_length=300, verbose_name=None)
    signup_confirmation = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'email', 'location', 'is_giver', 'is_collector']
