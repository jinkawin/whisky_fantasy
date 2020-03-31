from django.contrib.auth.models import User
from django.db import models

"""
    Variables:
        name_card:  Payment Person Name
        cardNo:     Payment Card Number
        expiryYear + expiryMonth:   Expiry Date of the Payment Card
        cvv:        3-pin Security Code behind the Card
"""

class PaymentInfo(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name_card = models.CharField(max_length=40)
    cardNo = models.PositiveIntegerField()
    expiryYear = models.PositiveIntegerField()
    expiryMonth = models.PositiveIntegerField()
    cvv = models.PositiveIntegerField()