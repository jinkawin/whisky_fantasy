
from django.db import models



class Customer(models.Model):
    cust_username = models.CharField(max_length=255, null=True, unique=True)
    cust_password = models.CharField(max_length=255, null=True)
    cust_email = models.CharField(max_length=255, null=True)
