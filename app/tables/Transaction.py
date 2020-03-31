from django.contrib.auth.models import User
from django.db import models

from app.tables.Delivery import Delivery
from app.tables.Customer import Customer
from app.tables.Merchant import Merchant
from app.tables.Whisky import Whisky

from datetime import datetime


class Transaction(models.Model):
    '''
        Variables:
            // Initial Plan:    Transaction Record will only be added when Customer Successfully Purchased the Item
            trans_status:       1, success/product_unavilable
            trans_price:        price of the Whisky when being brought
            trans_quantity:     1, default value; >=1, quantity of Whisky which user brought
            trans_amount:       trans_price * trans_quantity
            trans_time:         current transaction date as default
    '''
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    whisky = models.ForeignKey(Whisky, on_delete=models.CASCADE)
    merchant = models.CharField(max_length=255)
    trans_status = models.CharField(max_length=1, default=1)
    trans_time = models.DateTimeField()
    trans_price = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0.00)
    trans_quantity = models.PositiveIntegerField()
    trans_amount = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0.00)
    trans_address = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True)
