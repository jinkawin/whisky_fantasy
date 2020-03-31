from django.contrib.auth.models import User
from django.db import models

from app.tables.Customer import Customer


class PaymentInfo(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name_card = models.CharField(max_length=40)
    cardNo = models.PositiveIntegerField()
    expiryYear = models.PositiveIntegerField()
    expiryMonth = models.PositiveIntegerField()
    cvv = models.PositiveIntegerField()