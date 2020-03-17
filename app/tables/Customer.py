
from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(models.Model):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    cust_email = models.CharField(max_length=255, null=False)
    # cust_fb_id = models.CharField(max_length=255, blank=True, null=True)