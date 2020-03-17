from django.db import models

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    whisky = models.ForeignKey(Whisky, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    trans_status = models.CharField(max_length=1, default=1)
    trans_time = models.DateTimeField(editable=False)
    trans_price = models.CharField(max_digits=20, decimal_places=2, null=False, default=0.0)