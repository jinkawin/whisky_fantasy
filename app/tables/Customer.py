
from django.db import models



class Customer(models.Model):
    cust_username = models.CharField(max_length=255, null=False, unique=True)
    cust_password = models.CharField(max_length=255, null=False)
    cust_email = models.CharField(max_length=255, null=False)
