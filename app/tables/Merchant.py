from django.db import models

class Merchant(models.Model):
    merchant_username = models.CharField(max_length=255, null=False, unique=True)
    merchant_password = models.CharField(max_length=255, null=False)
    merchant_email = models.EmailField(max_length=254, null=False)


