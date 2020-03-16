from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    username = models.CharField(max_length=255, null=True, unique=True)
    password = models.CharField(max_length=255, null=True)
    cust_email = models.CharField(max_length=255, null=True)
    cust_fb_id = models.CharField(max_length=255, blank=True, null=True)
