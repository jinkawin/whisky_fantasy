from django.db import models

from app.tables.Delivery import Delivery
from app.tables.Customer import Customer
from app.tables.Merchant import Merchant
from app.tables.Whisky import Whisky


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    whisky = models.ForeignKey(Whisky, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    trans_status = models.CharField(max_length=1, default=1)
    trans_time = models.DateTimeField(editable=False)
    trans_price = models.DecimalField(max_digits=20,decimal_places=2, null=False, default=0.0)
    trans_quantity = models.PositiveIntegerField()
    trans_amount = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0.0)
    trans_address = models.ForeignKey(Delivery, on_delete=models.CASCADE)