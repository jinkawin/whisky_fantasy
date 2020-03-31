from django.db import models

from app.tables.Customer import Customer


class PaymentInfo(models.Model):
    '''
    Variables:
        name_card:      Owner Name of the Payment Card
        cardNo:         Payment Card Number
        expiryMonth:    Expiry Month of the Payment Card
        expiryYear:     Expiry Year of the Payment Card
        cvv:            Secret Code of the Payment Card
    '''
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name_card = models.CharField(max_length=40)
    cardNo = models.PositiveIntegerField(max_length=16)
    expiryDate = models.DateField()
    cvv = models.PositiveIntegerField(max_length=3)
