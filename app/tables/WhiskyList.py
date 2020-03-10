from django.db import models

class WhiskyList(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    whisky_name = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(default=0)